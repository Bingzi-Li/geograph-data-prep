from google_matrix_api import get_distance
import json

coordinates = []
distance = []
id_list = []
with open('../data/libraries.json') as json_file:  
    libraries = json.load(json_file)
    for library in libraries['features']:
        coor = {"ID":library['properties']['OBJECTID'], 'coord':library['geometry']['coordinates'] }
        coordinates.append(coor)
        id_list.append(library['properties']['OBJECTID'])
    for i in range(0,len(coordinates)-1):
        for j in range(i+1, len(coordinates)):
            s = str(coordinates[i]['coord'][0]) + ',' + str(coordinates[i]['coord'][1])
            d = str(coordinates[j]['coord'][0]) + ',' + str(coordinates[j]['coord'][1])
            dist = get_distance(s,d)
            distance.append({'origin':coordinates[i]['ID'], 'destination':coordinates[j]['ID'], 'distance':dist})

with open('../data/distance.json', 'w') as fp:
    json.dump(distance, fp)
    
with open('../data/id_list.json', 'w') as fp:
    json.dump(id_list, fp)
    
        
    