

import networkx as nx
import random
import os

def generateGraph (n,m,q,filename=''):

    if filename:
        with open(filename, 'w+') as f:
            f.write('%s %s%s' %(n+m,q, os.linesep))
            for i in range(q):
                v1=random.randint(0,n)
                v2=random.randint(0,m)
                f.write('%s %s%s' %(v1, v2, os.linesep))

if __name__ == '__main__':
    generateGraph(300,300*500/20,300*500, 'bi_graph.txt')