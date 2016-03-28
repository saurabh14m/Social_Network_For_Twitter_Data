# -*- coding: utf-8 -*-
"""
Created on Sat Nov 01 18:55:14 2014

@author: Saurabh
"""
import sys
sys.path.append('C:\\anaconda\\lib\\site-packages') 
sys.path.append('C:\\Users\\Saurabh\\Anaconda\\Scripts')
import networkx as nx
#import neonx 

#G = nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply_links3.csv", delimiter=',' , create_using=nx.DiGraph(), encoding="utf-8")
#G1=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\retweet_network2.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
#G2=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))
G3=nx.read_gexf("e:\\Data2\\Web_Analytics\\photoviz dynamic.gexf")
#############################################
G01 = nx.compose(G,G1)
G012 = nx.compose(G,G2)
G0123 = nx.compose(G012,G3)
len(G0123)
#G0123=G01
G1.number_of_nodes()
G1.number_of_edges()
G1.number_of_selfloops()
##
G2.number_of_nodes()
G2.number_of_edges()
##
G3.number_of_nodes()
G3.number_of_edges()
##
### So FINAL IS G0123
import pylab as plt
import sys
this = sys.modules[nx]
###
N,K = G0123.order() , G0123.size()
avg_deg = float(K)/N
print "Nodes: ", N
print "Edges: ", K
print "Average degree: ", avg_deg

import igraph
from igraph import *
#### Create the PAJEK FIle
nx.write_pajek(G012, "test4.net")

G0123=G3
######### ANALYSIS

G0123_ud = G0123.to_undirected()
# Clustering coefficient of node 0
#print nx.clustering(G0123_ud, 0)

# Clustering coefficient of all nodes (in a dictionary)
clust_coefficients = nx.clustering(G0123_ud)

# Average clustering coefficient
#ccs = nx.clustering(G0123_ud)
ccs =clust_coefficients 
avg_clust = sum(ccs.values()) / len(ccs)


nx.write_pajek(G0123, "testxx.net")
nx.write_gml(G0123, "mentionsxx.gml")


######### ANALYSIS

nx.draw_networkx(G0123) 

### Igraphs
import igraph
g = igraph.read("F:\\Data3\\mentions2.net" , format="pajek")


G = nx.complete_graph(5)
K5 = nx.convert_node_labels_to_integers(G,first_label=2)
G.add_edges_from(K5.edges())
c = list(nx.k_clique_communities(G, 4))
list(c[0])
list(nx.k_clique_communities(G, 6))


#node centrality measures.
G0123_components = nx.connected_component_subgraphs(G0123_ud)

[len(s) for s in G0123_components]
## Hence we take the largest connected component
G0123_mc = G0123_components[0]
G0123_mc_ud = G0123_mc.to_undirected()



graphs = list(nx.connected_component_subgraphs(G0123_ud))
#####Find the connected componnets only
G01234_ud = nx.connected_components(G0123_ud)

### Find Number of Strongly connected components in the graph
strongly_num = nx.number_strongly_connected_components(G0123)

G6 = nx.strongly_connected_component_subgraphs(G0123)

### Create a Subgraph of all the Strongly connected components with recursive algorithm
G7 = nx.strongly_connected_components_recursive(G0123)
 
### Create a Subgraph kosaraju_strongly_connected_components
G9 = nx.kosaraju_strongly_connected_components(G0123, source=None)

nx.draw_networkx(G9) 

### The condensation of G is the graph with each of the strongly connected components contracted into a single node.
G8 = nx.condensation(G0123, scc=None)
nx.draw_networkx(G8) 

#Return the number of connected components in G. For directed graphs only.
G10=nx.number_weakly_connected_components(G0123)

#Returns the number of attracting components in G
G11=nx.number_attracting_components(G0123)

subgraphs = list(nx.biconnected_component_subgraphs(G0123_ud))

articulate = list(nx.articulation_points(G0123_ud))

## Average connectivity
### takes a lot of time
G14=nx.average_node_connectivity(G0123_ud)

#Returns a set of edges of minimum cardinality that disconnects G.
G15 = len(nx.minimum_edge_cut(G0123_mc))


##Returns the weighted minimum edge cut using the Stoer-Wagner algorithm.
cut_value, partition = nx.stoer_wagner(G0123)

####################################################################################
no_of_core=nx.core_number(G0123)

def attack(graph, centrality_metric):
    graph = graph.copy()
    steps = 0
    ranks = centrality_metric(graph)
    nodes = sorted(graph.nodes(), key=lambda n: ranks[n])
    while nx.is_connected(graph):
        graph.remove_node(nodes.pop())
        steps += 1
    else:
        return steps

####################################################################################
nx.radius(G0123_mc), nx.diameter(G0123_mc)

####################################################################################
nx.center(G0123_mc)

####################################################################################
center = [node for node in G0123_mc.nodes() if nx.eccentricity(G0123_mc, node) == nx.radius(G0123_mc)]

####################################################################################
nx.draw_networkx(G0123_mc, node_size=15, edge_color='y', with_labels=False, alpha=.4, linewidths=0)

#Find k-clique communities in graph using the percolation method.
G16 = nx.k_clique_communities(G0123_mc, 3)
list(G16[0])

