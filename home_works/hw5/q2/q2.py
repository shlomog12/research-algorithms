from typing import Callable, Any
import outputtypes as out
from algo import DFS,BFS

def serch_in_graph(algorithm: Callable, graph: int, src: int, outputtype: out.OutputType=out.ListOfNodes):
    if isinstance(graph, dict):
        get_neigbors = lambda v: graph[v]
    else:
        get_neigbors = lambda v: filter(lambda i: (graph[v][i]==1) , range(len(graph)))
    return outputtype.extract_output_from_list_of_nodes(algorithm(get_neigbors, src))



graph1 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0],]

graph2 = {'A': ['B', 'C'],
             'B': ['A','C','D'],
             'C': ['A','D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


print(serch_in_graph(BFS,graph1,0))
print(serch_in_graph(BFS,graph1,0, out.Count))
print(serch_in_graph(DFS,graph1,0))
print(serch_in_graph(DFS,graph1,0, out.Count))
print(serch_in_graph(DFS,graph1,0, out.SortedNodes))