__author__ = 'ivanovsergey'

from priorityQueue import PriorityQueue as PQ
from IC import runIC
import os, sys

def generalGreedy(G, k, p=.01):
    ''' Finds initial seed set S using general greedy heuristic
    Input: G -- networkx Graph object
    k -- number of initial nodes needed
    p -- propagation probability
    Output: S -- initial set of k nodes to propagate
    '''
    import time
    start = time.time()
   # R = 20 # number of times to run Random Cascade
    R = 20
    S = [] # set of selected nodes
    # add node to S if achieves maximum propagation for current chosen + this node
    for i in range(k):
        s = PQ() # priority queue
        for v in G.nodes():
            if v not in S:
                s.add_task(v, 0) # initialize spread value
                for j in range(R): # run R times Random Cascade
                    [priority, count, task] = s.entry_finder[v]
                    s.add_task(v, priority - float(len(runIC(G, S + [v], p)))/R) # add normalized spread value
        task, priority = s.pop_item()
        S.append(task)
        print task,i, k, time.time() - start
    return S