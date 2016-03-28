# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 02:33:54 2014

@author: Saurabh
"""
import sys
sys.path.append('c:\\anaconda\\lib\\site-packages') 
sys.path.append('C:\\Users\\Saurabh\\Anaconda\\Scripts')
import networkx as nx
import neonx 

G2=nx.read_edgelist("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply_network.edgelist", create_using=nx.DiGraph(), data=(('weight',float),))

import igraph
from igraph import *
#### Create the PAJEK FIle

G0123=G2
nx.write_pajek(G0123, "test4.net")

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


######### ANALYSIS
### Igraphs
import igraph
#g = igraph.read("F:\\Data3\\test4.net" , format="pajek")

import community
import networkx as nx
import matplotlib.pyplot as plt

#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure
G = G0123
#nx.erdos_renyi_graph(30, 0.05)

#first compute the best partition
partition = community.best_partition(G)

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


nx.draw_networkx_edges(G,pos=None, alpha=0.5)
plt.show()


