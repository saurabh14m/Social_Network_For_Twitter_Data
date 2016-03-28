import sys
sys.path.append('c:\\users\\saurab;h\\anaconda\\lib\\site-packages\\') 
sys.path.append('c:\\Users\\Saurabh\\Anaconda\\Scripts')
from bulbs.neo4jserver import Graph
#from bulbs.neo4jserver import Graph
g = Graph()

from bulbs.neo4jserver import Graph, Config, NEO4J_URI
#config = Config(NEO4J_URI, "james", "secret")
#g = Graph(config)
g = Graph() 
g.gremlin.execute(query1)


print NEO4J_URI

james = g.vertices.create(name="James")


import org.neo4j.kernel.EmbeddedReadOnlyGraphDatabase
import neomodel

from neo4j import GraphDatabase

###############################################################################

from py2neo import Graph
from py2neo import Node, Relationship , neo4j
from py2neo import cypher 
from py2neo_gremlin import Gremlin
graph = Graph()

graph_db = neo4j.Graph

remote_graph = Graph("F:\Singtel\SNA\batch_importer_20\test.db")

query1 = "START n=node(*) return count(n)"
eid=123
query2 = "start a = relationship({eid}) return a"
inrels = graph.cypher.execute(query2)

print(graph.nodes())

graph.saveGraphML("abc.xml")

g.loadGraphML('data/graph-example-1.xml')                

g.gremlin.execute(graph.saveGraphML("abc.xml"))


