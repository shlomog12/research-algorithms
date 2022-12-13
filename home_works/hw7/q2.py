import networkx as nx
import networkx.algorithms.approximation as nx_app
from typing import List
from utils import bounded_subsets, draw_graph_by_array

def is_cover(G:nx.Graph, candidates:set):
    """
    :param G: graph
    :param candidates: set of nodes
    Returns true if the candidates are graph covering. otherwise returns false
    """
    for u, v in G.edges():
        if u not in candidates and v not in candidates:
            return False
    return True

def sum_weights_of_set(G:nx.Graph,nodes:List):
    """
    :param G: graph
    :param nodes: list of nodes
    Returns sum (v['weight'] for all v in nodes) 
    """
    sum = 0
    nodes_data = dict(G.nodes(data='weight', default=1))
    for v in nodes:
        sum += nodes_data[v]
    return sum

def approximation_vertex_coverage(G, cover_nx):
    """
    Calculating the approximation ratio of vertex coverage using complete search
    """
    sum_w = lambda s: sum_weights_of_set(G,s)
    if (len(G.edges()) == 0) and (sum_w(cover_nx) == 0):
        return 1
    for s in bounded_subsets(G.nodes, sum_w(cover_nx), sum_func=sum_w):
        if is_cover(G,set(s)):
            ans = float(sum_w(s))/float(sum_w(cover_nx))
            return ans





def draw_graph_of_approximation(p):
    val_of_approx = []
    for n in range(1,20):
        G = nx.gnp_random_graph(n,p)
        cover_nx = nx_app.min_weighted_vertex_cover(G,weight="weight")
        val = approximation_vertex_coverage(G, cover_nx)
        val_of_approx.append(val)
    draw_graph_by_array(val_of_approx, title=f"approximation p={p}", label_X="n", label_Y="approximation ratio")
    
draw_graph_of_approximation(0.5)
draw_graph_of_approximation(0.3)
draw_graph_of_approximation(0.7)
draw_graph_of_approximation(0.2)
draw_graph_of_approximation(1)