# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 18:04:58 2014

@author: Saurabh
"""
import pandas as pd
G=pd.read_csv("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\social_network.edgelist", sep=" " , header=None)

G1=pd.read_csv("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\retweet_network.edgelist", sep=" " , header=None)
G2=pd.read_csv("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply_network.edgelist", sep=" " , header=None)
G3=pd.read_csv("F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\mention_network.edgelist",  sep=" " , header=None)

G1.to_csv('F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\retweet.csv', index_label=None , index=False)
G2.to_csv('F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\reply.csv', index_label=None , index=False)
G3.to_csv('F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\mentions.csv', index_label=None , index=False)
G.to_csv('F:\\Data2\\Web_Analytics\\Assignment\\higgs-retweet_network_edgelist\\links.csv', index_label=None , index=False)

G1[[0]]

G1x = pd.unique(G1[[0]])

G1.groupby([0])

np.unique(G1[[0]])

def df2sqlite(dataframe, db_name = "import.sqlite", tbl_name = "import"):
  import sqlite3
  conn=sqlite3.connect(db_name)
  cur = conn.cursor()                                 
  wildcards = ','.join(['?'] * len(dataframe.columns))              
  data = [tuple(x) for x in dataframe.values]
 
  cur.execute("drop table if exists %s" % tbl_name)
  col_str = '"' + '","'.join(dataframe.columns) + '"'
  cur.execute("create table %s (%s)" % (tbl_name, col_str))
  cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)
 
  conn.commit()
  conn.close()

G1.columns=['Parent','Child','Weight']
G2.columns=['Parent','Child','Weight']
G3.columns=['Parent','Child','Weight']
G.columns=['Parent','Child']


df2sqlite(G1,'knowe','retweet')
df2sqlite(G2,'knowe','reply')
df2sqlite(G3,'knowe','mentions')
df2sqlite(G,'knowe','link')

import sqlite3
conn=sqlite3.connect('knowe')
cur = conn.cursor()                                 
cur.execute("PRAGMA table_info(retweet)")
cur.execute("PRAGMA table_info(reply)")
cur.execute("PRAGMA table_info(mentions)")
cur.execute("PRAGMA table_info(link)")
print cur.description  



