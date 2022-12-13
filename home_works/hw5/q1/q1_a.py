"""
This creates all subsets of the list that sum < max
>>> print_by_iterator(bounded_subsets([1,10,40,50,70,75],3))
[],[1],
>>> print_by_iterator(bounded_subsets([1,10,40,50,70,75],55))
[],[1],[1, 10],[1, 10, 40],[1, 40],[1, 50],[10],[10, 40],[40],[50],
>>> print_by_iterator(bounded_subsets(range(4),12))
[],[0],[0, 1],[0, 1, 2],[0, 1, 2, 3],[0, 1, 3],[0, 2],[0, 2, 3],[0, 3],[1],[1, 2],[1, 2, 3],[1, 3],[2],[2, 3],[3],
>>> print_by_iterator(bounded_subsets(range(50,150),103))
[],[50],[50, 51],[50, 52],[50, 53],[51],[51, 52],[52],[53],[54],[55],[56],[57],[58],[59],[60],[61],[62],[63],[64],[65],[66],[67],[68],[69],[70],[71],[72],[73],[74],[75],[76],[77],[78],[79],[80],[81],[82],[83],[84],[85],[86],[87],[88],[89],[90],[91],[92],[93],[94],[95],[96],[97],[98],[99],[100],[101],[102],[103],
"""
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
def bounded_subsets(myList,maximum):
  
    if maximum < 0:
        return []
    myList = sorted(myList)
    yield []
    for i in range(len(myList)):
        current = myList[i]
        sub_list = myList[i+1:len(myList)]
        sum_2 = maximum - current
        for sub in bounded_subsets(sub_list, sum_2):
            sum_temp = current+sum(sub)
            if sum_temp <= maximum:
                yield [current]+sub
                # yield sub

def print_by_iterator(it):
    """
    print for tests
    """
    for x in it:
        print(x, end =",")



def main():
    import doctest
    print(doctest.testmod())
    # with open('./out_a.txt', 'w') as f:
    #     for s in bounded_subsets(list(range(90,100)) + list(range(920,1000)), 1000):
    #         # print(s, file=f)
    #         print(s)
    
    
    # # with open('./out_from_hw5_a.txt', 'w') as f:
        # print("1: bounded_subsets([1,2,3], 4):", file=f)
    #     print("1: bounded_subsets([1,2,3], 4):")
        # for s in bounded_subsets([1,2,3], 4):
        #     # print(s, file=f) 
        #     print(s)
    #     # print("**************************************************************************",file=f)
    #     print("**************************************************************************")
    #     # print("2: bounded_subsets(range(50,150), 103):", file=f)
    #     print("2: bounded_subsets(range(50,150), 103):")
    #     for s in bounded_subsets(range(50,150), 103):
    #         # print(s, file=f) 
    #         print(s)   
    #     # print("**************************************************************************",file=f)
    #     print("**************************************************************************")
    #     # print("3: zip(range(5), bounded_subsets(range(100), 1000000000000))", file=f)
    #     print("3: zip(range(5), bounded_subsets(range(100), 1000000000000))")
        # for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
	    #     # print(s, file=f)   
        #     print(s) 


if __name__ == "__main__":
    main()

# for x in bounded_subsets(range(4),12):
#     print(x)