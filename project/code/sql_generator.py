'''
create schema:
CREATE SCHEMA <schema_name>;
SET SCHEMA <schema_name>;

CREATE COLUMN TABLE "NODES"(
	"node_id" INTEGER NOT NULL,
	"name" NVARCHAR(32),
	PRIMARY KEY (
		"node_id"
	)
);

CREATE COLUMN TABLE "EDGES"(
	"edge_id" INTEGER NOT NULL,
	"length" INTEGER,
	"start" INTEGER NOT NULL,
	"end" INTEGER NOT NULL,
	PRIMARY KEY (
		"edge_id"
	)
);

ALTER TABLE "EDGES" ADD FOREIGN KEY ( "start" ) REFERENCES "NODES" ("node_id") ON UPDATE CASCADE ON DELETE CASCADE ENFORCED VALIDATED
;
ALTER TABLE "EDGES" ADD FOREIGN KEY ( "end" ) REFERENCES "NODES" ("node_id") ON UPDATE CASCADE ON DELETE CASCADE ENFORCED VALIDATED
;
'''
import json

def sql_generator():
    vertex_id = 0
    edge_id = 0
    with open('../data/vertex_list.json') as list_file:
        vertex_list = json.load(list_file)
    with open('../data/edge_list.json') as edge_file:
        edge_list = json.load(edge_file)
    sql_file = open('../data/sql_code.txt', 'w')
    for vertex in vertex_list:
        sql_file.write('INSERT INTO "NODES" VALUES ('+ str(vertex_id) + ',' + vertex['name'] + ') ;\n')
        vertex_id += 1
    for edge in edge_list:
        sql_file.write('INSERT INTO "EDGES" VALUES (' + str(edge_id) + ',' + str(edge['distance']) + ',' + str(edge['origin']) + ',' + str(edge['destination']) + ') ;\n')
        edge_id += 1
    sql_file.close()
if __name__ == '__main__':
    sql_generator()