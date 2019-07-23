"""
Script to generate csv files that store results from hausdorff distance metric for comaprison between computed and oberved routes.
    Author      : Tina Baidar
    Email       : tina.baidar13@gmail.com
    Date        : June 2019
"""

import os
from calculate_hausdorff_distance import hausdorff_distance


def generate_name(computed_route):
    return os.path.basename(computed_route)[:-3] + 'csv'
# define path for all the computed and observed routes 
if __name__ == '__main__':
    parent_directory = r'C:\Users\Tina Baidar\Documents\Geotech\IFGI_2nd_Sem\Routing Algorithm\project\June6'
    computed_routes_1 = [
        os.path.join(parent_directory, r'computed_routes-20190623T165528Z-001\computed_routes\a_star_A.shp'),
        os.path.join(parent_directory, r'from ismail\a_star_landmark_part_2\a_star_landmark_A.shp'),
        os.path.join(parent_directory, r'from Ben\angular change with landmark\Angular_change_landmark_A.shp'),
        os.path.join(parent_directory, r'from Ben\angular change without landmark\Angular_change_A.shp'),
    ]

    computed_routes_2 = [
        os.path.join(parent_directory, r'computed_routes-20190623T165528Z-001\computed_routes\a_star_B.shp'),
        os.path.join(parent_directory, r'from ismail\a_star_landmark_part_2\a_star_landmark_B.shp'),
        os.path.join(parent_directory, r'from Ben\angular change with landmark\Angular_change_landmark_B.shp'),
        os.path.join(parent_directory, r'from Ben\angular change without landmark\Angular_change_B.shp'),
    ]

    computed_routes_3 = [
        os.path.join(parent_directory, r'computed_routes-20190623T165528Z-001\computed_routes\a_star_C.shp'),
        os.path.join(parent_directory, r'from ismail\a_star_landmark_part_2\a_star_landmark_C.shp'),
        os.path.join(parent_directory, r'from Ben\angular change with landmark\Angular_change_landmark_C.shp'),
        os.path.join(parent_directory, r'from Ben\angular change without landmark\Angular_change_C.shp'),
    ]

    computed_routes = [
        computed_routes_1,
        computed_routes_2,
        computed_routes_3,  
    ]

    observed_routes=[
    r'C:\Users\Tina Baidar\Documents\Geotech\IFGI_2nd_Sem\Routing Algorithm\project\June6\shapefiles\Route_1_proj.shp',
    r'C:\Users\Tina Baidar\Documents\Geotech\IFGI_2nd_Sem\Routing Algorithm\project\June6\shapefiles\Route_2_proj.shp',
    r'C:\Users\Tina Baidar\Documents\Geotech\IFGI_2nd_Sem\Routing Algorithm\project\June6\shapefiles\Route_3_proj.shp',
    ]

    #Loop to generate the csv files at each run 
    for i in range(len(observed_routes)):
        computed_route_list = computed_routes[i]
        observed_route = observed_routes[i]
        for computed_route in computed_route_list:
            csv_file_name = generate_name(computed_route)
            print('write to ', csv_file_name)
            hausdorff_distance(observed_route, computed_route, csv_file_name)

