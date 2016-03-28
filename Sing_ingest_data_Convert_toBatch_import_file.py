# -*- coding: utf-8 -*-
"""Created on Thu Dec 04 17:11:30 2014@author: Saurabh"""
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import cluster
import pandas as pd

##d1 =pd.read_csv("F:\\Data3\\Unix\\Python_on_Singtel\\merged2.csv")
k1 =pd.read_csv("G:\\Singtel\\SNA\\snap1.csv",sep='\t',  header=None)
k1.head()
k1.columns = ['name','Child','N','T']
k1.head()

k1name= pd.DataFrame(k1.name)
k1name.columns=['name']
k1Child= pd.DataFrame(k1.Child)
k1Child.columns=['name']

k1nameChild = k1name.append(k1Child)
## remove duplicates
k1nameChild = k1nameChild.drop_duplicates(['name'])

#### nodes.csv
##   name    l:label       age works_on
#    Michael Person,Father 37  neo4j
#    Selina  Person,Child  14
#    Rana    Person,Child  6
#    Selma   Person,Child  4

#Convert the column to dataframe
x = pd.DataFrame(k1nameChild['name'])

#Concat the two Dataframes
node_df = pd.concat([x,x] , axis=1)
node_df.columns = ['name','l:label']

node_dict = dict(zip(node_df.name , node_df.index))

rels_df = k1.copy()

#    start	end	type	    since   counter:int
#    0     1   FATHER_OF	1998-07-10  1
#    0     2   FATHER_OF 2007-09-15  2
#    0     3   FATHER_OF 2008-05-03  3
#    2     3   SISTER_OF 2008-05-03  5
#    1     2   SISTER_OF 2007-09-15  7

rels_df.columns = ['start','end','reltype','totalMins']
rels_df['NumCalls'] = rels_df.reltype
rels_df.reltype = 'CallerToCalle'
rels_df.columns = ['start','end','reltype','totalMins','NumCalls']


for i in range(len(rels_df)):
    rels_df.start[i]=  node_dict[rels_df.start[i]]
    rels_df.end[i]=  node_dict[rels_df.end[i]]



#Write the two dataframe to tab delimited dataframe
#node_df.to_csv('nodes_with.csv' , sep='\t' , index=True)

node_df.to_csv('nodes.csv' , sep='\t' , index=False)
rels_df.to_csv('rels.csv' , sep='\t', index=False)



from sklearn.cross_decomposition import CCA
cca = CCA(n_components=1)
cca.fit(d1.n_hrs_News_All, d1.n_hrs_Educational_All)





