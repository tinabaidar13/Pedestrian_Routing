"""
Script to implement hausdorff distance metric for comaprison between computed and oberved routes.
    Author      : Tina Baidar
    Email       : tina.baidar13@gmail.com
    Date        : June 2019
"""
import arcpy
import os
import csv

def hausdorff_distance(observed_route, computed_route, file_path):

    arcpy.env.overwriteOutput = True
    target_dir = r'C:\Users\Tina Baidar\Documents\Geotech\IFGI_2nd_Sem\Routing Algorithm\project\June6\shapefiles\geometric_similarity_output'
    target_dir = r'C:\temp_data'

    rows = arcpy.SearchCursor(observed_route)

    #store row id and print
    rownumber = []

    for item in rows:
        value = item.getValue('FID')
        rownumber.append(value)
    print(rownumber)

    #export rows to individual layer
    try:
        for i in rownumber:
            obj = "FID = %s" %(i)
            arcpy.MakeFeatureLayer_management(observed_route, 'route1lyr')#change shp to lyr file
            arcpy.SelectLayerByAttribute_management('route1lyr', 'NEW_SELECTION', obj)
            arcpy.CopyFeatures_management('route1lyr', '{}/route1_{}'.format(target_dir, i))
            arcpy.SelectLayerByAttribute_management('route1lyr', "CLEAR_SELECTION")
    except:
        print(arcpy.GetMessages())

    print('extracted successfully')


    import numpy as np
    from scipy.spatial.distance import directed_hausdorff

    arcpy.env.workspace = target_dir
    featureclasses = arcpy.ListFeatureClasses()
    n=0
    haus_values = []
    
    #export each layer to points and calculate haudorff distance
    for fc in featureclasses:
        arraycomputed = arcpy.da.FeatureClassToNumPyArray(computed_route, ('Shape@XY'), explode_to_points= True, spatial_reference = arcpy.Describe(computed_route).spatialReference)
        array1 = arcpy.da.FeatureClassToNumPyArray(fc, ('Shape@XY'), explode_to_points= True, spatial_reference = arcpy.Describe(fc).spatialReference)
        haus1 = directed_hausdorff(arraycomputed['Shape@XY'], array1['Shape@XY'])[0]
        
        if len(array1) > len(arraycomputed):
            diff = int(len(array1) - len(arraycomputed))
            arraycomputed = np.append(arraycomputed, arraycomputed[0:diff], axis = 0)
            
        else:
            diff = int(len(arraycomputed) - len(array1))
            array1 = np.append(array1, array1[0:diff], axis = 0)

        haus1 = directed_hausdorff(arraycomputed['Shape@XY'], array1['Shape@XY'])[0]
        haus_values.append(haus1)

    # write to CSV
    #######change csv file name here
    #csv_file_path = 'Angular_change_landmark_dist1.csv'
    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['haus1'])
        for haus_value in haus_values:
            print(haus_value)
            writer.writerow([haus_value])
    print('done '+ file_path)


