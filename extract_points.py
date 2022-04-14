import numpy as np
import random
from shapely.geometry import Polygon, Point
import json

class Extractor:
    """Extract points from polygons"""
    in_file_path: str
    out_file_name: str
    
    def __init__(self, in_file_path, out_file_name, points_number):
        """Constructor"""
        self.in_file_path = in_file_path
        self.out_file_name = out_file_name
        self.points_number = points_number
        
    def is_valid_json(self):
        """Check if json file"""
        if self.in_file_path.lower().endswith(".json") or self.in_file_path.lower().endswith(".geojson"):
            return True
        
        print("[ERROR]: This is not a Valid Json")     
        return False
    
    def read_json_file(self):
        # Get json Object 
        file = open(self.in_file_path)
        json_object = json.load(file)
        return json_object
    
    def is_valid_feature(self):
        # Check if valid json object
        if self.is_valid_json():
            # define json object
            json_object = self.read_json_file()
            if json_object["type"] == "FeatureCollection" and json_object["features"]:
                return True
            
        print("[ERROR]: This is not a Valid Feature")
        return False
    
    def random_points_within(self, poly):
        min_x, min_y, max_x, max_y = poly.bounds

        points = []

        while len(points) < self.points_number:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)

        return points
    
    def extract_points(self):
        # define json object
        if self.is_valid_feature():
            json_object = self.read_json_file()
            for f in json_object["features"]:
                poly = Polygon(f["geometry"]["coordinates"][0])
                points = self.random_points_within(poly)
                print("######################")
                print(points)
               
        return False
            


def main():
    file_path = "E:\projects\python\scripts\extract_point\infile.json"
    out_name = "out.json"
    points_number = 5
    extractor: Extractor = Extractor(file_path, out_name, points_number)
    extractor.extract_points()



    
if __name__ == "__main__":
    main()       


# poly = Polygon([(23.789642, 90.354714), (23.789603, 90.403000), (23.767688, 90.403597),(23.766510, 90.355448)])

# def random_points_within(poly, num_points):
#     min_x, min_y, max_x, max_y = poly.bounds

#     points = []

#     while len(points) < num_points:
#         random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
#         if (random_point.within(poly)):
#             points.append(random_point)

#     return points


# points = random_points_within(poly,1000)

# for p in points:
#     print(p.x,",",p.y)