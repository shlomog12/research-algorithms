import mystruct

def DFS(get_neigbors ,v):
    s = mystruct.Stack()
    return serch_in_graph(get_neigbors=get_neigbors ,v=v,s=s)

def BFS(get_neigbors ,v):
    s = mystruct.Queue()
    return serch_in_graph(get_neigbors=get_neigbors ,v=v,s=s)

def serch_in_graph(get_neigbors, v, s: mystruct.Struct):
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


