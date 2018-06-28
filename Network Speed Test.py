#Baseline test of loading data from an SQL database to a map.
#Feature Types: 10,000 Spot Eleveation Points, 10,000 Elevation Contour lines, and 10,000 wetland polygons.

import arcpy
import time
import datetime
import pandas as pd
import os.path

#measure connection time to enterprise database
connect_false = datetime.datetime.now()
database = r"C:FILEPATH"
connect_true = datetime.datetime.now()
connect_time = connect_true - connect_false

#declare paths to test layers
#spot elevation points
testLayer1 = r"C:FILEPATH\Spot_Elevation_Points"
#contour lines
testLayer2 = r"C:FILEPATH\Contour_Lines"
#wetlands polygons
testLayer3 = r"C:FILEPATH\Wetlands_Polygons"

#prepare map document for data
workspace = r"C:FILEPATH\BlankMap.mxd"
workspaceActive = arcpy.mapping.MapDocument(workspace)
dataframe = arcpy.mapping.ListDataFrames(workspaceActive)[0]

#add and time first test layer
layer1_false = datetime.datetime.now()
addTestLayer1 = arcpy.mapping.Layer(testLayer1)
arcpy.mapping.AddLayer(dataframe, addTestLayer1,"BOTTOM")
layer1_true = datetime.datetime.now()
layer1_time = layer1_true - layer1_false

#add and time second test layer
layer2_false = datetime.datetime.now()
addTestLayer2 = arcpy.mapping.Layer(testLayer2)
arcpy.mapping.AddLayer(dataframe, addTestLayer2, "BOTTOM")
layer2_true = datetime.datetime.now()
layer2_time = layer2_true - layer2_false

#add and time third test layer
layer3_false = datetime.datetime.now()
addTestLayer3 = arcpy.mapping.Layer(testLayer3)
arcpy.mapping.AddLayer(dataframe, addTestLayer3, "BOTTOM")
layer3_true = datetime.datetime.now()
layer3_time = layer3_true - layer3_false

#output results to .csv
csv_path = 'C:FILEPATH\Output Log.csv'

#check for existence of output log
file_exists =os.path.exists(csv_path)

#store new results as dataframe
results = {'Date': [datetime.datetime.today()], 'Time': [datetime.datetime.now()], 'Connection Time': [connect_time],'Layer 1': [layer1_time], 'Layer 2': [layer2_time], 'Layer 3': [layer3_time]}
out_dataframe = pd.DataFrame(data=results, columns = ['Date','Time','Connection Time', 'Layer 1', 'Layer 2','Layer 3'])

#test to see if output file exists
if file_exists==True:
#read existing csv
    in_dataframe = pd.read_csv(csv_path, encoding='utf-8')

#append new line and output csv
    with open(csv_path, 'a') as new:
        out_dataframe.to_csv(new, encoding='utf-8', index=False, header=False)
else:
#if file does not exist, create a new one
    out_dataframe.to_csv(csv_path, encoding ='utf-8', index=False)


