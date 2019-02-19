#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#This script will import in unreal all camera in target sequencer
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython

import os.path
import configparser
import unreal_engine as ue
from unreal_engine.classes import MovieSceneCameraCutTrack, MovieScene3DTransformSection, MovieScene3DTransformTrack, MovieSceneAudioTrack, CineCameraActor
from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID, FrameRate
from unreal_engine import FTransform, FVector, FColor
from unreal_engine.enums import EMovieSceneObjectBindingSpace

def AddSequencerSectionKeysByIniFile(SequencerSection, SectionFileName, FileLoc):
	Config = configparser.ConfigParser()
	Config.read(FileLoc)
	for option in Config.options(SectionFileName):
		frame = float(option)/24 #FrameRate
		value = float(Config.get(SectionFileName, option))
		SequencerSection.sequencer_section_add_key(frame,value)
seq = ue.find_asset("LevelSequence'/Game/ImportedFbx/MySequence.MySequence'")
if seq:
	print("Sequencer reference found")
	ImportedCamera = [] #(CameraName, CameraGuid)
	print("========================= Import started ! =========================")
	
	#Set frame rate
	myFFrameRate = FrameRate()
	myFFrameRate.Denominator = 1.0
	myFFrameRate.Numerator = 24
	seq.MovieScene.DisplayRate = myFFrameRate
	
	#Set playback range
	seq.sequencer_set_playback_range(0.041666666666666664, 10.416666666666666)
	camera_cut_track = seq.sequencer_add_camera_cut_track()
	world = ue.get_editor_world()
else:
	print("Sequencer reference not valid !")


if seq:
	print('========================= Imports completed ! =========================')
	
	for cam in ImportedCamera:
		print(cam[0])
	
	print('=========================')
	seq.sequencer_changed(True)
