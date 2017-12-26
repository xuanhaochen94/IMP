''' Implements greedy algorithm for IC model
'''
__author__ = 'qio'

from priorityQueue import PriorityQueue as PQ
from IC import irunIC

import os, sys

def new_BI_graph_greedy(G,n,m,k,p=.01):
    ''' Finds initial seed set S using general greedy algorithm
    Input: G -- networkx Graph object
    n--the number of key nodes
    m--the number of user nodes
    k -- number of initial nodes needed
    p -- propagation probability
    Output: S -- initial set of k nodes to propagate
    '''
    import time
    start = time.time()
    S = [] # set of selected nodes
    # add node to S if achieves maximum propagation for current chosen + this node
    s = PQ() # priority queue
    dict={}
    for v in G.nodes():
        if (v not in S) and (v<=n):#find the key nodes add them to s
            dict[v] = 0;
            s.add_task(v, 0) # initialize spread value
            [priority, count, task] = s.entry_finder[v]
            s.add_task(v, priority - float(irunIC(G, S + [v],n,m ,p))) # add normalized spread value

    while(len(S)<=k):

        task, priority = s.pop_item()
        if(dict[task]==1):
            S.append(task)#find the maximum nodes
            print("The nodes is %d,after find it the time is "%(task),time.time() - start)

        else:
            s.add_task(task,-1* float(irunIC(G, S + [task],n,m ,p)))
            dict[task]=1;



        #print 'the nodes is:'+task,i, k, time.time() - start
    return S


