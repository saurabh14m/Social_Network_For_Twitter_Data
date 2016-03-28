# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 14:37:56 2014

@author: Saurabh
"""
import sys
sys.path.append('c:\\anaconda\\lib\\site-packages') 
sys.path.append('C:\\Users\\Saurabh\\Anaconda\\Scripts')
import networkx as nx
import neonx 

G=nx.Graph()
G.add_node("spam")
G.add_edge(1,2)
print(G.nodes())

print(G.edges())

import math
G.add_edge('y','x',function=math.cos)
G.add_node(math.cos) # any hashable can be a node

elist=[('a','b',5.0),('b','c',3.0),('a','c',1.0),('c','d',7.3)]
G.add_weighted_edges_from(elist)
G=nx.Graph()
e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2)]

G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G,'a','d'))

G=nx.cubical_graph()
nx.draw(G)   # default spring_layout
nx.draw(G,pos=nx.spectral_layout(G), nodecolor='r',edge_color='b')

G=nx.Graph()
G.add_edge('A','B')
G.add_edge('B','C')
print(G.adj)

import snap

#################################
from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime

class Person(Node):
       
    element_type = "person"
    
    name = String(nullable=False)
    age = Integer()
    
class Knows(Relationship):

    label = "knows"

    created = DateTime(default=current_datetime, nullable=False)    
    
from bulbs.neo4jserver import Graph

g = Graph()
g.add_proxy("people", Person)
g.add_proxy("knows", Knows)
james = g.p
eople.create(name="James")
julie = g.people.create(name="Julie")

g.knows.create(james, julie)

G=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\social_network.edgelist",create_using=nx.DiGraph())

G1=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\retweet_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
G1.number_of_nodes()
G1.number_of_edges()
G1.number_of_selfloops()

G2=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
G2.number_of_nodes()
G2.number_of_edges()

G3=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\mention_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
G3.number_of_nodes()
G3.number_of_edges()

G3.edges(data = True)

G1.add_weighted_edges_from(G2.)

nx.to_numpy_matrix(G2)

G3.add_weighted_edges_from(nx.to_dict_of_lists(G2))

union(G2,G3)
##
data = neonx.get_geoff(G2, "LINKS_TO")
results = neonx.write_to_neo("http://localhost:7474/db/data/", G2, 'LINKS_TO')

data = neonx.get_geoff(G3, "LINKS_TO_G3")
results = neonx.write_to_neo("http://localhost:7474/db/data/", G3, 'LINKS_TO_G3')

##############################

G = nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply_links.csv", delimiter=',' , create_using=nx.DiGraph(), encoding="utf-8")
G1=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\retweet_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
G1.number_of_nodes()
G1.number_of_edges()
G1.number_of_selfloops()

G2=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
G2.number_of_nodes()
G2.number_of_edges()

G3=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\mention_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
G3.number_of_nodes()
G3.number_of_edges()

G01 = nx.compose(G,G1)
G012 = nx.compose(G01,G2)
G0123 = nx.compose(G012,G3)

len(G0123)

nx.write_edgelist(G0123,'F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\Two_stage.edgelist',comments='#',delimiter=' ',data=(('weight',float),),encoding='utf-8')
G01234=nx.read_edgelist('F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\Two_stage.edgelist', create_using=nx.DiGraph(), data=(('weight',float),))

###
import pylab as plt
import sys
this = sys.modules[nx]

#SELECT *
#  FROM links where parent in (select distinct(parent) from reply );

############### ANALYSIS begins here:
N,K = G01234.order() , G01234.size()
avg_deg = float(K)/N
print "Nodes: ", N
print "Edges: ", K
print "Average degree: ", avg_deg

G01234_ud = G01234.to_undirected()

# Clustering coefficient of node 0
print nx.clustering(G01234_ud, 0)

# Clustering coefficient of all nodes (in a dictionary)
clust_coefficients = nx.clustering(G01234_ud)

# Average clustering coefficient
#ccs = nx.clustering(G01234_ud)
ccs =clust_coefficients 
avg_clust = sum(ccs.values()) / len(ccs)

#node centrality measures.
G01234_components = nx.connected_component_subgraphs(G01234_ud)
G01234_mc = G01234_components[0]

# Betweenness centrality
bet_cen = nx.betweenness_centrality(G01234_mc)
# Closeness centrality
clo_cen = nx.closeness_centrality(G01234_mc)
# Eigenvector centrality
eig_cen = nx.eigenvector_centrality(G01234_mc)

##
def highest_centrality(cent_dict): 
    """Returns a tuple (node,value) with the node 
    with largest value from Networkx centrality dictionary.""" 
    # Create ordered tuple of centrality data
    cent_items=[(b,a) for (a,b) in cent_dict.iteritems()]
    # Sort in descending order 
    cent_items.sort() 
    cent_items.reverse() 
    return tuple(reversed(cent_items[0]))

results = [(k,bet_cen[k],clo_cen[k],eig_cen[k]) for k in G01234_mc]

f = open('G01234_mc.txt','w')
for item in results:
    f.write(','.join(map(str,item)))
    f.write('\n')
f.close()

#### Create the PAJEK FIle
nx.write_pajek(G0123, "test.net")

