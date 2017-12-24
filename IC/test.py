'''
File for testing different algorithm
'''
__author__ = 'qio'

import networkx as nx

from IC import runIC
from IC import irunIC
from degreeDiscount import degreeDiscountIC
from generalGreedy import generalGreedy
from BI_graph_greedy import BI_graph_greedy
import os

if __name__ == '__main__':
    import time
    start = time.time()

    # read in graph
    G = nx.Graph()
    with open('bi_graph.txt') as f:
        n, m = f.readline().split()
        for line in f:
            u, v = map(int, line.split())
            try:
                G[u][v]['weight'] += 1
            except:
                G.add_edge(u,v, weight=1)
    print 'Built graph G'
    print time.time() - start

    #calculate initial set
    seed_size = 10


    #S = degreeDiscountIC(G, seed_size)
    S = generalGreedy(G, seed_size)
    #S=BI_graph_greedy(G,30,30*50/20,seed_size)
    print 'Initial set of', seed_size, 'nodes chosen'
    print time.time() - start

    # write results S to file
    with open('the_nodes_found.txt', 'w') as f:
        for node in S:
            f.write(str(node) + os.linesep)

    # calculate average activated set size
    iterations = 100 # number of iterations
    avg = 0
    for i in range(iterations):
        T = runIC(G, S)
        avg += float(len(T))/iterations
        # print i, 'iteration of IC'
    print 'Avg. Targeted', int(round(avg)), 'nodes out of', len(G)
    print time.time() - start

    with open('the_nodes_affected.txt', 'w') as f:
        f.write(str(len(S)) + os.linesep)
        for node in T:
            f.write(str(node) + os.linesep)
    console = []