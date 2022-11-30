import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways

import queue
n, l, e = [int(i) for i in input().split()]
edges = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    edges.setdefault(n1,[]).append(n2)
    edges.setdefault(n2,[]).append(n1)

gateways = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)
    
visited = set()
stack = []



def shortest_path_dfs(src, dest, edges):
    q = queue.PriorityQueue()
    fathers = {src: -1}
    dis = {}
    dis[src] = 0
    q.put(src)
    
    while len(q.queue) != 0:
        current = q.get()
        dis_current = dis[current] + 1
        for nei in edges[current]:
            if nei not in dis or dis[nei] > dis_current:
                dis[nei] = dis_current
                fathers[nei] = current
                q.put(nei)
    path = []
    if dest not in fathers:
        return []       
    while dest != src:
        path.append(dest)
        dest = fathers[dest]
    return path+[src]


while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    
    zz = []
    
    for g in gateways:
        xxx = shortest_path_dfs(si, g,edges)     
        if len(xxx) > 1:
            zz.append(xxx)
    xmin = min(zz, key=lambda p: len(p))
    
    counter = {}
    for x in zz:
        k = str(x[-2:])
        if k in counter:
            counter[k]+=1
        else:
            counter[k] = 1
    t = min(zz, key=lambda p: [len(p),-1*counter[str(p[-2:])]])

    print(f'{t[0]} {t[1]}', file=sys.stderr, flush=True)
    print(f'{t[0]} {t[1]}')
    edges[t[0]].remove(t[1])
    edges[t[1]].remove(t[0])
    if len(edges[t[0]]) == 0:
        if t[0] in gateways:
            gateways.remove(t[0])
        del edges[t[0]]
    if len(edges[t[1]]) == 0:
        if t[1] in gateways:
            gateways.remove(t[1])
        del edges[t[1]]