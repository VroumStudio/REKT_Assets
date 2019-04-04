#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#It will import into Unreal Engine all the assets of type StaticMesh, SkeletalMesh, Animation and Pose
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython
#Use this command : unreal_engine.py_exec(r"D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\ImportAssetScript.py")

import os.path
import configparser
import ast
import unreal_engine as ue
from unreal_engine.classes import PyFbxFactory, StaticMesh, Skeleton, SkeletalMeshSocket
from unreal_engine.enums import EFBXImportType, EMaterialSearchLocation
from unreal_engine.structs import StaticMeshSourceModel, MeshBuildSettings
from unreal_engine import FVector, FRotator

#Prepare var and def
UnrealImportLocation = r'/Game/ImportedFbx'
ImportedAsset = []

def GetOptionByIniFile(FileLoc, OptionName, literal = False):
	Config = configparser.ConfigParser()
	Config.read(FileLoc)
	Options = []
	for option in Config.options(OptionName):
		if (literal == True):
			Options.append(ast.literal_eval(Config.get(OptionName, option)))
		else:
			Options.append(Config.get(OptionName, option))
	return Options


#Process import
print('========================= Import started ! =========================')



################[ Import Rolling_Drawer as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Rolling_Drawer.fbx')
AdditionalParameterLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Rolling_Drawer_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Rolling_Drawer" ')



################[ Import Desk_Complex as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Desk_Complex.fbx')
AdditionalParameterLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Desk_Complex_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Desk_Complex" ')



################[ Import CeilingPipes as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_CeilingPipes.fbx')
AdditionalParameterLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_CeilingPipes_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "CeilingPipes" ')



################[ Import Workstation as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Workstation.fbx')
AdditionalParameterLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Workstation_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Workstation" ')



################[ Import Armature as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Armature.fbx')
AdditionalParameterLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Armature_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Armature" ')



################[ Import Window_Structure as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Window_Structure.fbx')
AdditionalParameterLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Window_Structure_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Window_Structure" ')



################[ Import Walls as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Walls.fbx')
AdditionalParameterLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Garage\ExportedFbx\StaticMesh\SM_Walls_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Walls" ')



print('========================= Imports completed ! =========================')

for asset in ImportedAsset:
	print(asset)

print('=========================')
