from graph import Graph
import json

g = Graph()

# add vertices
with open('../data/id_list.json') as json_file:
    id_list = json.load(json_file)
    for id in id_list:
        g.add_vertex(id)
    
# add edges
with open('../data/distance.json') as json_file:
    dist_list = json.load(json_file)
    for dist in dist_list:
        g.add_edge(dist['origin'], dist['desitination'], float(dist['distance']))

# clean unwanted edges
