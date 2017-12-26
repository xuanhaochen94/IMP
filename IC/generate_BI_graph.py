__author__ = 'qio'
import networkx as nx
import random
import os

def generateGraph (n,m,q,filename=''):

    if filename:
        with open(filename, 'w+') as f:
            f.write('%s %s%s' %(n+m,q, os.linesep))
            for i in range(q):
                v1=random.randint(0,n)
                v2=random.randint(n,m)
                f.write('%s %s%s' %(v1, v2, os.linesep))

if __name__ == '__main__':
    generateGraph(300,300*500/20,300*500, 'big_bi_graph.txt')
# these function will make a bi_graph which
# include 30 key nodes and 30*50/20 user nodes
#and 30*50 edges and there are maybe some same edges.
