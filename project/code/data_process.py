#from graph import Graph, Vertex, dijkstra
from debug import Graph, dijkstra
import json, copy

edge_list = []

# add edges
with open('../data/distance.json') as json_file:
    dist_list = json.load(json_file)
    g = Graph(len(dist_list))
    for dist in dist_list:
        g.add_edge(dist['origin'], dist['destination'], float(dist['distance']))

# clean unwanted edges
for dist in dist_list:
    # find shortest path without that edge
    g.delete_edge(dist['origin'], dist['destination'], float(dist['distance']))
    shortest = dijkstra(g, dist['origin'], dist['destination'])
    # if there is no anther shortest, add that edge back
    if shortest > float(dist['distance']):
        g.add_edge(dist['origin'], dist['destination'], float(dist['distance']))
        edge_list.append({'origin':dist['origin'], 'destination':dist['destination'], 'distance':dist['distance']})


# export the graph to final json file we need
with open('../data/edge_list.json', 'w') as fp:
    json.dump(edge_list, fp)