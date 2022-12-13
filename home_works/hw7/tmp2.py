import networkx as nx
import networkx.algorithms.approximation as nx_app
import heapq


history = {}
next_iter = {}
def save_history_of_generator(func):
    """
    This is a decorator of a generator so it keeps the history of the runs
    """
    def wrapper(*args, **kwargs):
        key = str(args)
        i = 0
        while True:
            if key in history and len(history[key]) > i:
                yield history[key][i]
            else:
                it = next_iter.get(key, func(*args))
                try:
                    next_one = next(it)
                except StopIteration:
                    return
                history.setdefault(key,[]).append(next_one)
                next_iter[key] = it
                yield next_one
            i+=1
    return wrapper

@save_history_of_generator
def subset_generator_sorted(myList,sum_func=sum):
    """
    This creates all the subsets of the list and returns them sorted from lowest to highest total
    """
    myList = sorted(myList)
    yield []
    queue = []
    n = len(myList)
    for i in range(n):
        current = myList[i]
        sub_list = myList[i+1:n]
        it = subset_generator_sorted(sub_list)
        try:
            first_sub = [current] + next(it)
        except StopIteration:
            continue
        sumFirst = sum_func(first_sub)
        heapq.heappush(queue, (sumFirst, i, first_sub, it))
    
    while len(queue) > 0:
        (sumFirst, i, first_sub ,current_iter) =  heapq.heappop(queue)
        yield first_sub
        try:
            current = myList[i]
            next_sub = [current]+next(current_iter)
        except StopIteration:
            continue
        sumNext = sum_func(next_sub)
        heapq.heappush(queue, (sumNext, i, next_sub, current_iter))
 
def bounded_subsets(myList, maximum, sum_func=sum):
    """
    This creates all subsets of the list whose sum < max returns them sorted from lowest to highest sum
    >>> print_by_iterator(bounded_subsets([1,10,40,50,70,75],3))
    [],[1],
    >>> print_by_iterator(bounded_subsets([1,10,40,50,70,75],55))
    [],[1],[10],[1, 10],[40],[1, 40],[10, 40],[50],[1, 10, 40],[1, 50],
    >>> print_by_iterator(bounded_subsets(range(4),12))
    [],[0],[0, 1],[1],[0, 2],[2],[0, 1, 2],[0, 3],[1, 2],[3],[0, 1, 3],[1, 3],[0, 2, 3],[2, 3],[0, 1, 2, 3],[1, 2, 3],
    >>> print_by_iterator(bounded_subsets(range(50,150),103))
    [],[50],[51],[52],[53],[54],[55],[56],[57],[58],[59],[60],[61],[62],[63],[64],[65],[66],[67],[68],[69],[70],[71],[72],[73],[74],[75],[76],[77],[78],[79],[80],[81],[82],[83],[84],[85],[86],[87],[88],[89],[90],[91],[92],[93],[94],[95],[96],[97],[98],[99],[100],[50, 51],[101],[50, 52],[102],[50, 53],[51, 52],[103],
    """
    for x in subset_generator_sorted(myList,sum_func):
        if sum_func(x) > maximum:
            return
        yield x

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

def sum_weights_of_set(G,nodes):
    """
    
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
    for s in bounded_subsets(G.nodes, sum_w(cover_nx), sum_func=sum_w):
        if is_cover(G,set(s)):
            ans = float(sum_w(s))/float(sum_w(cover_nx))
            if ans < 1:
                print(ans)
                print(s)
                print(G.edges())
            return ans
            # return float(sum_w(s))/float(sum_w(cover_nx))
    print(G.edges())
    print(f'is cover = {is_cover(cover_nx)}')
    return False

G = nx.gnp_random_graph(10,0.3)

cover_nx = nx_app.min_weighted_vertex_cover(G,weight="weight")
# sum_cover_nx = sum_weights_of_set(G, cover_nx)

print(cover_nx)
print('#######################################################################')
x = approximation_vertex_coverage(G, cover_nx)
print(x)

# nodes = list(G.nodes)



# cover = nx_app.min_weighted_vertex_cover(G,weight="weight")