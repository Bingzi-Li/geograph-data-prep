from graph import Graph, dijkstra
import json

g = Graph()
edge_list = []

# add vertices
with open('../data/vertex_list.json') as json_file:
    vertex_list = json.load(json_file)
    for id in vertex_list:
        g.add_vertex(id)
    
# add edges
with open('../data/distance.json') as json_file:
    dist_list = json.load(json_file)
    for dist in dist_list:
        g.add_edge(dist['origin'], dist['desitination'], float(dist['distance']))

# clean unwanted edges
for dist in dist_list:
    # find shortest path without that edge
    g.delete_edge(dist['origin'], dist['desitination'])
    shortest = dijkstra(g, dist['origin'], dist['desitination'])
    # if there is no anther shortest, add that edge back
    if shortest != float(dist['distance']):
        g.add_edge(dist['origin'], dist['desitination'], float(dist['distance']))
        edge_list.append({dist['origin'], dist['desitination'], dist['distance']})


# export the graph to final csv file we need
with open('../data/edge_list.json', 'w') as fp:
    json.dump(edge_list, fp)