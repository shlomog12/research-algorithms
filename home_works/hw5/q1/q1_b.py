
"""
 Author: Shlomo Glick
 Since : 2022-11
"""

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
def subset_generator_sorted(myList):
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
        sumFirst = sum(first_sub)
        heapq.heappush(queue, (sumFirst, i, first_sub, it))
    
    while len(queue) > 0:
        (sumFirst, i, first_sub ,current_iter) =  heapq.heappop(queue)
        yield first_sub
        try:
            current = myList[i]
            next_sub = [current]+next(current_iter)
        except StopIteration:
            continue
        sumNext = sum(next_sub)
        heapq.heappush(queue, (sumNext, i, next_sub, current_iter))
 
def bounded_subsets(myList, maximum):
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
    for x in subset_generator_sorted(myList):
        if sum(x) > maximum:
            return
        yield x

def print_by_iterator(it):
    """
    print for tests
    """
    for x in it:
        print(x, end =",")


def main():
    import doctest
    print(doctest.testmod())






    # with open('./tt1_b.txt', 'w') as f:
    #     for s in bounded_subsets(list(range(90,100)) + list(range(920,1000)), 1000):
    #         print(s, file=f)  

    # with open('./tt2_b.txt', 'w') as f:
    #     print("1: bounded_subsets([1,2,3], 4):", file=f)
    #     for s in bounded_subsets([1,2,3], 4):
    #         print(s, file=f) 
    #     print("**************************************************************************",file=f)
    #     print("2: bounded_subsets(range(50,150), 103):", file=f)
    #     for s in bounded_subsets(range(50,150), 103):
    #         print(s, file=f)    
    #     print("**************************************************************************",file=f)
    #     print("3: zip(range(5), bounded_subsets(range(100), 1000000000000))", file=f)
    #     for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
	#         print(s, file=f)
   


if __name__ == "__main__":
    main()
