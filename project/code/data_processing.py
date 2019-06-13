#from google_matrix_api import get_distance
import json

coordinates = {}
with open('../data/libraries.json') as json_file:  
    libraries = json.load(json_file)
    for library in libraries['features']:
        coordinates.update({library['properties']['OBJECTID']: library['geometry']['coordinates'] })
    print(coordinates)
    