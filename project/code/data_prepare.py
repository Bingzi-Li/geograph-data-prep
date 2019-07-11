from google_matrix_api import get_distance
import json

coordinates = []
distance = []
vertex_list = []
id = 0

with open('../data/Libraries.json') as json_file:  
    libraries = json.load(json_file)
with open('../data/Colleges__Universities.json') as json_file:
    colleges = json.load(json_file)
    
for library in libraries['features']:
    coor = {"ID": id, 'coord':library['geometry']['coordinates']}
    coordinates.append(coor)
    vertex_list.append({"ID": id,  'type':'library', 'name':library['properties']['DESCRIPTION']})
    id += 1
for college in colleges['features']:
    coor = {"ID": id, 'coord':college['geometry']['coordinates']}
    coordinates.append(coor)
    vertex_list.append({"ID":id ,  'type':'college', 'name':college['properties']['DESCRIPTION']})
    id += 1
    
for i in range(0,len(coordinates)-1):
    for j in range(i+1, len(coordinates)):
        # origin and destination pairs
        try:
            dist = get_distance(coordinates[i]['coord'],coordinates[j]['coord'])
            distance.append({'origin':coordinates[i]['ID'], 'destination':coordinates[j]['ID'], 'distance':dist})
        except:
            print("No bicycle lanes.\n")
        try:
            dist = get_distance(coordinates[j]['coord'],coordinates[i]['coord'])
            distance.append({'origin':coordinates[j]['ID'], 'destination':coordinates[i]['ID'], 'distance':dist})
        except:
            print("No bicycle lanes.\n")

with open('../data/distance.json', 'w') as fp:
    json.dump(distance, fp)
    
with open('../data/vertex_list.json', 'w') as fp:
    json.dump(vertex_list, fp)
    
        
    