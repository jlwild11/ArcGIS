#import modules
import arcpy

#set workspace
arcpy.env.workspace = r"C:\Users\Jameson\Documents\Jameson\ArcGIS\Training\PythEveryone\RunningScripts\Oregon_Polk.gdb"

#set up a describe object for each fc in gdb
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    desc = arcpy.Describe(fc)
    print (desc.name + "___" + desc.spatialReference.name)

print ("Script completed")