class List(list):
 
    def __getitem__(self, *args):
        if isinstance(args[0],int):
            return super().__getitem__(args[0])
        indexes = args[0]
        ans = super().__getitem__(indexes[0])
        for i in range(1,len(indexes)):
            index = indexes[i]
            if not isinstance(index,int):
                raise TypeError
            ans = ans[index]
        return ans

mylist = List([
    [[1,2,3,33],[4,5,6,[4,3,1,[44,33]]]],
    [[7,8,9,99],[10,11,12,122]],
    [[13,14,15,155],[16,17,18,188]],
    ]
)
print(mylist[0,1,3,3,1])


mylist2 = List([
    [[1,2,3,33],[4,5,6,66]],
    [[7,8,9,99],[10,11,12,122]],
    [[13,14,15,155],[16,17,18,188]],
    ]
)