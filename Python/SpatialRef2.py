import arcpy
import os

workspace = r"C:\Users\Jameson\Documents\Jameson\ArcGIS\Training\PythEveryone"

walk = arcpy.da.Walk(workspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        print (desc.path + "___" + desc.spatialReference.name)

print ("Script completed")


import arcpy
import os

workspace = r"C:\Users\Jameson\Documents\Jameson\ArcGIS\Training\PythEveryone"

walk = arcpy.da.Walk(workspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        print (desc.name + "___" + desc.spatialReference.name)

print ("Script completed")