import mystruct
from typing import Any, List, Callable
def DFS(get_neigbors:Callable ,v:Any) -> List[Any]:
    """
    Depth-first search Algorithem - https://en.wikipedia.org/wiki/Depth-first_search
    """
    s = mystruct.Stack()
    return serch_in_graph(get_neigbors=get_neigbors ,v=v,s=s)

def BFS(get_neigbors:Callable ,v:Any) -> List[Any]:
    """
    Breadth-first search Algorithem - https://en.wikipedia.org/wiki/Breadth-first_search
    """
    s = mystruct.Queue()
    return serch_in_graph(get_neigbors=get_neigbors ,v=v,s=s)

def serch_in_graph(get_neigbors:Callable, v:Any, s:mystruct.Struct) -> List[Any]: 
    """
    Sertch by struct
    """
    visited = set()
    visited.add(v)
    s.add(v)
    ans = []
    while not s.is_empty():
        current = s.get()
        ans.append(current)
        visited.add(current)
        for nei in get_neigbors(current):
            if not nei in visited:
                s.add(nei)
                visited.add(nei)
    return ans