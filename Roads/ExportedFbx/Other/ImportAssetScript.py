#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#It will import into Unreal Engine all the assets of type StaticMesh, SkeletalMesh, Animation and Pose
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython

import os.path
import unreal_engine as ue
from unreal_engine.classes import PyFbxFactory
from unreal_engine.enums import EFBXImportType, EMaterialSearchLocation

#Prepare var and process import
UnrealImportLocation = r'/Game/ImportedFbx'
ImportedAsset = []

print('========================= Import started ! =========================')



################[ Import Road_Barrier as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = False
fbx_factory.ImportUI.StaticMeshImportData.bGenerateLightmapUVs = True
FbxLoc = os.path.join(r'D:\Users\etudiant\Documents\GitHub\REKT_Assets\Roads\ExportedFbx\StaticMesh\SM_Road_Barrier.fbx')
AssetImportLocation = os.path.join(UnrealImportLocation, r'').replace('\\','/')
AssetImportLocation = AssetImportLocation.rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Road_Barrier" ')



print('========================= Imports completed ! =========================')

for asset in ImportedAsset:
	print(asset)

print('=========================')
