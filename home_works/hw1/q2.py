"""
 Author: Shlomo Glick
 Since : 2022-10
"""

from typing import Callable, Any

def extract_path_from_dict_of_parents(parnts: dict, start, end):
    """
    The function receives a start node, an end node, a dictionary
    that indicates for each node where we got to.
    The function returns an ordered list of the track from beginning to end

    test1
    >>> extract_path_from_dict_of_parents(parnts={1:3, 3:5, 5:7, 6:1}, start=7, end=6)
    [7, 5, 3, 1, 6]

    test2
    >>> extract_path_from_dict_of_parents(parnts={1:2, 2:4, 5:1, 32:7, 4:32, 10:12}, start=7, end=5)
    [7, 32, 4, 2, 1, 5]

    test3
    >>> extract_path_from_dict_of_parents(parnts={1:2, 2:4, 5:1, 32:7, 4:32, 10:12}, start=7, end=12)
    not exists path
    """
    
    if end not in parnts:
        return "not exists path"
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = parnts[current]
    path.insert(0, start)
    return path


def breadth_first_search(start: Any, end: Any, neighbor_function: Callable):
    """
    This is a function that receives a start node,
    an end node and a function that returns the node's neighbors
    and returns a track from the beginning to the end

    TESETS

    test1
    >>> breadth_first_search(start=(1, 3), end=(2, 7), neighbor_function=four_neighbor_function1)
    ['(1, 3)', '(2, 3)', '(2, 4)', '(2, 5)', '(2, 6)', '(2, 7)']

    test2
    >>> breadth_first_search(start={"x": 1, "y": 7}, end={"x": 2, "y": 9}, neighbor_function=four_neighbor_function2)
    ["{'x': 1, 'y': 7}", "{'x': 2, 'y': 7}", "{'x': 2, 'y': 8}", "{'x': 2, 'y': 9}"]

    test3
    >>> G = Graph()
    >>> G.addNode(1)
    >>> G.addNode(2)
    >>> G.addNode(3)
    >>> G.addNode(4)
    >>> G.addNode(5)
    >>> G.addconnection(1,4)
    >>> G.addconnection(4,5)
    >>> G.addconnection(5,2)
    >>> G.addconnection(2,3)
    >>> G.addconnection(5,3)
    >>> breadth_first_search(start=1, end=3, neighbor_function=G.getNeibyId)
    ['1', '4', '5', '3']
    """

    if start == end:
        return start
    parnts = {}
    queue = []
    queue.append(start)
    while len(queue) > 0:
        current = queue.pop(0)
        neighbors = neighbor_function(current)
        for neighbor in neighbors:
            if str(neighbor) not in parnts:
                parnts[str(neighbor)] = str(current)
                queue.append(neighbor)
            if neighbor == end:
                path = extract_path_from_dict_of_parents(parnts=parnts, start=str(start), end=str(end))
                return path
    return "no exists path"
    



#  ################################  FORֹ TESTS ########################################


def four_neighbor_function1(node:Any)->list:
    (x,y) = node
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def four_neighbor_function2(node:Any)->list:
    return [
        {"x": node["x"]+1, "y": node["y"]},
        {"x": node["x"]-1, "y": node["y"]},
        {"x": node["x"], "y": node["y"]+1},
        {"x": node["x"], "y": node["y"]-1},
        ]


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, id):
        n = Node(id)
        self.nodes[id] = n

    def getNeibyId(self, id):
        return self.nodes[id].getNei()

    def addconnection(self, id1, id2):
        self.nodes[id1].addNei(id2)
        self.nodes[id2].addNei(id1)

class Node:
    def __init__(self, id):
        self.id = id
        self.nei = []    


    def addNei(self, id):
        self.nei.append(id)

    def getNei(self):
        return self.nei


def main():
    import doctest
    print(doctest.testmod())

if __name__ == "__main__":
    main()