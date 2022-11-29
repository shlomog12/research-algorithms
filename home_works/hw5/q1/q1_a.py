
def subset_generator(myList,maximum):
    if maximum < 0:
        return []
    myList = sorted(myList)
    yield []
    for i in range(len(myList)):
        current = myList[i]
        list_ad_i = myList[i+1:len(myList)-1]
        sum_2 = maximum - current
        for sub in subset_generator(list_ad_i, sum_2):
            sum_temp = current+sum(sub)
            if sum_temp <= maximum:
                yield [current]+sub

l = [1,10,40,50,70,75]
# for x in subset_generator(l,103):
    # print(x)
for x in subset_generator(range(50,150),103):
    print(x)
