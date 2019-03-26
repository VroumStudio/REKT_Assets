#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#This script will import in unreal all camera in target sequencer
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython
#Use this command : unreal_engine.py_exec(r"D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\ImportSequencerScript.py")


import os.path
import time
import configparser
import unreal_engine as ue
from unreal_engine.classes import MovieSceneCameraCutTrack, MovieScene3DTransformSection, MovieScene3DTransformTrack, MovieSceneAudioTrack, CineCameraActor, LevelSequenceFactoryNew
if ue.ENGINE_MINOR_VERSION >= 20:
	from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID, FrameRate
else:
	from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID
from unreal_engine import FTransform, FVector, FColor
from unreal_engine.enums import EMovieSceneObjectBindingSpace
from unreal_engine.structs import MovieSceneObjectBindingID


seqLocation = r'/Game/ImportedFbx/Sequencer'
seqName = r'MySequence'
seqTempName = r'MySequence'+str(time.time())
mustBeReplace = False
startFrame = 1
endFrame = 41
frameRateDenominator = 1.0
frameRateNumerator = 25
secureCrop = 0.0001 #add end crop for avoid section overlay


def AddSequencerSectionFloatKeysByIniFile(SequencerSection, SectionFileName, FileLoc):
	Config = configparser.ConfigParser()
	Config.read(FileLoc)
	for option in Config.options(SectionFileName):
		frame = float(option)/frameRateNumerator #FrameRate
		value = float(Config.get(SectionFileName, option))
		SequencerSection.sequencer_section_add_key(frame,value)


def AddSequencerSectionBoolKeysByIniFile(SequencerSection, SectionFileName, FileLoc):
	Config = configparser.ConfigParser()
	Config.read(FileLoc)
	for option in Config.options(SectionFileName):
		frame = float(option)/frameRateNumerator #FrameRate
		value = Config.getboolean(SectionFileName, option)
		SequencerSection.sequencer_section_add_key(frame,value)


if ue.find_asset(seqLocation+'/'+seqName):
	print("Warning this file already exists")
	factory = LevelSequenceFactoryNew()
	seq = factory.factory_create_new(seqLocation+'/'+seqTempName.replace('.',''))
	mustBeReplace = True
else:
	factory = LevelSequenceFactoryNew()
	seq = factory.factory_create_new(seqLocation+'/'+seqName.replace('.',''))

if seq:
	print("Sequencer reference created")
	print(seq)
	ImportedCamera = [] #(CameraName, CameraGuid)
	print("========================= Import started ! =========================")
	
	#Set frame rate
	if ue.ENGINE_MINOR_VERSION >= 20:
		myFFrameRate = FrameRate()
		myFFrameRate.Denominator = frameRateDenominator
		myFFrameRate.Numerator = frameRateNumerator
		seq.MovieScene.DisplayRate = myFFrameRate
	else:
		seq.MovieScene.FixedFrameInterval = frameRateDenominator/frameRateNumerator
	
	#Set playback range
	seq.sequencer_set_playback_range(startFrame/frameRateNumerator, (endFrame-secureCrop)/frameRateNumerator)
	camera_cut_track = seq.sequencer_add_camera_cut_track()
	world = ue.get_editor_world()
else:
	print("Fail to create Sequencer")


#Import camera cut section
if seq:
	camera_cut_section = camera_cut_track.sequencer_track_add_section()
	#Not camera found for this section
	camera_cut_section.sequencer_set_section_range(1/frameRateNumerator, (41-secureCrop)/frameRateNumerator)
if mustBeReplace == True:
	OldSeq = seqLocation+'/'+seqName.replace('.','')+'.'+seqName.replace('.','')
	NewSeq = seqLocation+'/'+seqTempName.replace('.','')+'.'+seqTempName.replace('.','')
	print(OldSeq)
	print(NewSeq)
	print("LevelSequence'"+OldSeq+"'")
	ue.delete_asset(OldSeq)
if seq:
	print('========================= Imports completed ! =========================')
	
	for cam in ImportedCamera:
		print(cam[0])
	
	print('=========================')
	seq.sequencer_changed(True)
