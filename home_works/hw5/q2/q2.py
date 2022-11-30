from typing import Callable, Any
import outputtypes as out
from algo import DFS,BFS


graph_to_tests = [[0, 1, 1, 0, 0, 0],[1, 0, 1, 1, 0, 0],[1, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 1, 0],]
graph_to_tests2 = {0: [1, 2],1: [0,2,3],2: [0,3],3: [2],4: [5],5: [2]}
def serch_in_graph(algorithm: Callable, graph: int, src: int, outputtype: out.OutputType=out.ListOfNodes):
    """
    >>> serch_in_graph(BFS,graph_to_tests,0)
    [0, 1, 2, 3]
    >>> serch_in_graph(BFS,graph_to_tests,0, out.Count)
    4
    >>> serch_in_graph(DFS,graph_to_tests,0)
    [0, 2, 3, 1]
    >>> serch_in_graph(DFS,graph_to_tests,0, out.Count)
    4
    >>> serch_in_graph(DFS,graph_to_tests,0, out.SortedNodes)
    [0, 1, 2, 3]
    >>> serch_in_graph(BFS,graph_to_tests,0)
    [0, 1, 2, 3]


    >>> serch_in_graph(BFS,graph_to_tests2,0)
    [0, 1, 2, 3]
    >>> serch_in_graph(BFS,graph_to_tests2,0, out.Count)
    4
    >>> serch_in_graph(DFS,graph_to_tests2,0)
    [0, 2, 3, 1]
    >>> serch_in_graph(DFS,graph_to_tests2,0, out.Count)
    4
    >>> serch_in_graph(DFS,graph_to_tests2,0, out.SortedNodes)
    [0, 1, 2, 3]
    >>> serch_in_graph(BFS,graph_to_tests2,0)
    [0, 1, 2, 3]

    >>> serch_in_graph(BFS,[[0]],0)
    [0]
    """
    
    
    if isinstance(graph, dict):
        get_neigbors = lambda v: graph[v]
    else:
        get_neigbors = lambda v: filter(lambda i: (graph[v][i]==1) , range(len(graph)))
    return outputtype.extract_output_from_list_of_nodes(algorithm(get_neigbors, src))








def main():
    import doctest
    print(doctest.testmod())


if __name__ == "__main__":
    main()