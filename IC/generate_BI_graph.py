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
    generateGraph(30,30*50/20,30*50, 'bi_graph.txt')
   #生成了一个二分图,左边有30个节点,右边有30*50/20个节点,整个图之中,一共有30*50条边
    #边之中可能会有重复的边存在