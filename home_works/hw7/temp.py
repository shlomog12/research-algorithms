
import networkx as nx
import networkx.algorithms.approximation as nx_app
from itertools import powerset



# u = 3
# v = 2
# node_cover = [1,2,3,5]
# if {u, v} & node_cover:
#     print('aaaa')




G = nx.gnp_random_graph(30,0.1)
u = 3
v = 2
print({u,v} & G.edges())

# def is_cover(G, node_cover):
    # print(G.edges())
    # return all({u, v} & node_cover for u, v in G.edges())



import networkx as nx
from itertools import powerset

# create a graph
G = nx.Graph()

# add some nodes and edges
G.add_node(1, weight=2)
G.add_node(2, weight=3)
G.add_node(3, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(2, 3, weight=2)

# compute the weight of each subset of nodes
node_weights = {frozenset(subset): sum(G.node[node]['weight'] for node in subset)
                for subset in powerset(G.nodes)}

# sort the subsets by weight
sorted_subsets = sorted(node_weights, key=node_weights.get)

# print the sorted subsets
for subset in sorted_subsets:
    print(subset)
