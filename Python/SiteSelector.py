# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# SiteSelector.py
# Author: Jameson Wilder
# Created on: 2018-07-18
# 
# Description: Site Selection based on SF Bus Stops
# ---------------------------------------------------------------------------

arcpy.AddMessage("Loading ArcPy")

# Import arcpy module
import arcpy
arcpy.AddMessage("Loaded ArcPy")

arcpy.env.overwriteOutput = True

# Local variables:
arcpy.AddMessage("Loading Local Variables")
Bus_Stops = arcpy.GetParameterAsText(0)
where_clause1 = arcpy.GetParameterAsText(1) ## NAME = '21 OB'
where_clause2 = arcpy.GetParameterAsText(2) ## NAME = '5 OB'
distance = arcpy.GetParameterAsText(3)

Bus_Stops_Select1 = Bus_Stops + "_Select1"
Bus_Stops_Select2 = Bus_Stops + "_Select2"
Bus_Stops_Select1_Buffer = Bus_Stops_Select1 + "_Buffer"
Bus_Stops_Select2_Buffer = Bus_Stops_Select2 + "_Buffer"

Bus_Stops_Select_12_Buffer_Intersect = Bus_Stops + "_Select_12_Buffer_Intersect"

arcpy.AddMessage("Initial feature classes loaded")


# Process: Select
arcpy.AddMessage("Starting Select Analysis")
arcpy.Select_analysis(Bus_Stops, Bus_Stops_Select1, where_clause1)
arcpy.Select_analysis(Bus_Stops, Bus_Stops_Select2, where_clause2)
arcpy.AddMessage("Select Analysis Complete")


### Process: Buffer
arcpy.AddMessage("Starting Buffer Analysis")
arcpy.Buffer_analysis(Bus_Stops_Select1, Bus_Stops_Select1_Buffer,
                      distance, "FULL", "ROUND", "NONE", "", "PLANAR")
arcpy.Buffer_analysis(Bus_Stops_Select2, Bus_Stops_Select2_Buffer,
                      distance, "FULL", "ROUND", "NONE", "", "PLANAR")
arcpy.AddMessage("Buffer Analysis Complete")




# Process: Intersect
arcpy.AddMessage("Starting Intersect Analysis")
arcpy.Intersect_analysis([Bus_Stops_Select1_Buffer, Bus_Stops_Select2_Buffer],
                         Bus_Stops_Select_12_Buffer_Intersect, "ALL", "", "INPUT")

arcpy.AddMessage("Intersect Analysis Complete")

