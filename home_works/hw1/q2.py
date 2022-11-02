from typing import Callable, Any


def extract_path_from_dict_of_parents(parnts: dict, start, end):
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = parnts[current]
    path.insert(0, start)
    return path


def breadth_first_search(start: Any, end: Any, neighbor_function: Callable):
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
    



#  ################################  TESTS ########################################


# def four_neighbor_function(node:Any)->list:
#     (x,y) = node
#     return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

# def four_neighbor_function(node:Any)->list:

#     return [
#         {"x": node["x"]+1, "y": node["y"]},
#         {"x": node["x"]-1, "y": node["y"]},
#         {"x": node["x"], "y": node["y"]+1},
#         {"x": node["x"], "y": node["y"]-1},
#         ]

# start = {"x": 1, "y": 7}
# end = {"x": 2, "y": 9}
# start = (1,7)
# end = (2,9)


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





G = Graph()
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)
G.addNode(5)
G.addconnection(1,4)
G.addconnection(4,5)
G.addconnection(5,2)
G.addconnection(2,3)
G.addconnection(5,3)
t23 = G.getNeibyId(2)
print(t23)

start = 3
end = 1

# xrr = breadth_first_search(start=start, end=end, neighbor_function=four_neighbor_function)
# print(xrr)
xrr = breadth_first_search(start=start, end=end, neighbor_function=G.getNeibyId)
print(xrr)