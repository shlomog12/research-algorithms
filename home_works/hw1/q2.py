from queue import Empty
from typing import Callable, Any

def four_neighbor_function(node:Any)->list:
    (x,y) = node
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]


# breadth_first_search(start=(0,0), end=(2,2), neighbor_function= four_neighbor_function)


def breadth_first_search(start: Any, end: Any, neighbor_function: Callable):
    visiable = []
    queue = neighbor_function(start)
    while queue is not Empty:
        v = queue.pop()
        


    