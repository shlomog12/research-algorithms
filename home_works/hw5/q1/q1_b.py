
import heapq

history = {}
next_iter = {}
def save_history_of_generator(func):
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
def subset_generator(myList):
    myList = sorted(myList)
    yield []
    queue = []
    n = len(myList)
    for i in range(n):
        current = myList[i]
        list_ad_i = myList[i+1:n]
        it = subset_generator(list_ad_i)
        try:
            first_sub = [current] + next(it)
        except StopIteration:
            continue
        sumFirst = sum(first_sub)
        heapq.heappush(queue, (sumFirst, i, first_sub, it, list_ad_i))
    
    while len(queue) > 0:
        (sumFirst, i, first_sub ,current_iter, list_ad_i) =  heapq.heappop(queue)
        yield first_sub
        try:
            current = myList[i]
            next_sub = [current]+next(current_iter)
        except StopIteration:
            continue
        sumNext = sum(next_sub)
        heapq.heappush(queue, (sumNext, i, next_sub, current_iter, list_ad_i))
 
def bounded_subsets(myList, maximum):
    for x in subset_generator(myList):
        if sum(x) > maximum:
            return
        yield x




l = [1,10,40,50,70,75]
# l = [1,10,40]

for x in bounded_subsets(l,103):
    print(x)

for x in bounded_subsets(range(50,150),103):
    print(x)


# for k,v in history.items():
#     print(f'*******************************************  l = {k}')
#     print(f'v = {v}')
# for x in bounded_subsets(range(50,1500),1931):
#     print(x)














# dd = subset_generator(l,103)
# xxx = [1,2,3]
# ccc = dd+xxx
# for i in ccc:
#     print(i)