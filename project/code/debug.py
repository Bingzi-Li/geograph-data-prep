import json

coordinates = []
distance = []
vertex_list = []

with open('../data/Libraries.json') as json_file:  
    libraries = json.load(json_file)
with open('../data/Colleges__Universities.json') as json_file:
    colleges = json.load(json_file)
    
for library in libraries['features']:   
    vertex_list.append({"ID":'lib'+ str(library['properties']['OBJECTID']), 'coor':library['geometry']['coordinates'], 'type':'library', 'name':library['properties']['DESCRIPTION']})
for college in colleges['features']:
    vertex_list.append({"ID":'col'+ str(college['properties']['OBJECTID']), 'coor':college['geometry']['coordinates'],  'type':'college', 'name':college['properties']['DESCRIPTION']})

with open('../data/vertex_list.json', 'w') as fp:
    json.dump(vertex_list, fp)