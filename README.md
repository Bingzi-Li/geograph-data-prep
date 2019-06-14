# geograph-data-prep
The code in this repository aims to use data from Faifax County Open Geospatial Data(https://data-fairfaxcountygis.opendata.arcgis.com/)
to build a business use case to be used in SAP HANA Graph Viewer.

The steps include:
1. Use Google Matrix API to get edge weight between any two vertices
2. Use Dijkstra Algorithm to eliminate necessary edges
3. Export the graph data to vertex/edge json file. May convert to csv later.
