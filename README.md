# geograph-data-prep

The code in this repository aims to use data from Faifax County Open Geospatial Data(https://data-fairfaxcountygis.opendata.arcgis.com/)
to build a business use case to be used in SAP HANA Graph Viewer.

#### keywords: json data, Google Matrix API, Graph, Dikjstra, sql
----------
### The steps include:
1. Use Google Matrix API to get edge weight between any two vertices
2. Use Dijkstra Algorithm to eliminate necessary edges
3. Export the graph data to vertex/edge json file. 
4. generate insert sql statement for later purposes

### Sequence of generating data:
1. Have a json file of correctly formatted geospatial points in /data
2. run data_prepare.py
3. run data_process.py
4. If you need the sql code for building the graph, run sql_generator.py

If you find this is somehow a little tiny bit useful. I am glad.

### Issues occurred with Google Distance Matrix API:
The API cannot return any results according to sets of geospatial coordinates. 
The problem may be:
The data provided by Fairfax county is slightly different to the coordinates in Google Matrix. Therefore, Google API cannot located the place. In a word, Google Map API is not as smart as you think. Sad.

#### My solution:
Since my dataset is small. I just settled on manually retrieve the place ID, and use that to request. If you have a large dataset and face the same problem with google api, ooops, poor you. You may need to try other methods. Good luck.
