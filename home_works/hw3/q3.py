"""
 Author: Shlomo Glick
 Since : 2022-11
"""

class List(list):
    """
    This is the same construct as Python list (list)
    but allows access to items in multidimensional array syntax.

    TESTS:

    >>> mylist = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]],])
    >>> print(mylist[0,1,3])
    66
    >>> mylist[0,1,3] = 77
    >>> print(mylist)
    [[[1, 2, 3, 33], [4, 5, 6, 77]], [[1, 2, 3, 33], [4, 5, 6, 77]], [[13, 14, 15, 155], [16, 17, 18, 188]]]
    >>> mylist2 = List([[[1,2,3,33],[4,5,6,[4,3,1,[44,21]]]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]],])
    >>> print(mylist2[0,1,3,3,1])
    21
    """
 
    def __getitem__(self, *args):
        """
        allows to get an object from a list in a multi-dimensional syntax
        """
        if isinstance(args[0],int):
            return super().__getitem__(args[0])
        indexes = args[0]
        current_index = indexes[0]
        ans = super().__getitem__(current_index)
        for i in range(1,len(indexes)):
            current_index = indexes[i]
            ans = ans[current_index]
        return ans

    def __setitem__(self, *args):
        """
        allows to set an object from a list in a multi-dimensional syntax
        """
        length = len(args)
        value = args[length-1]
        indexes = args[0]
        current_index = indexes[0]
        current_val = super().__getitem__(current_index)
        queue = []
        queue.append(current_val)
        for i in range(1,len(indexes)-1):
            current_index = indexes[i]
            current_val = current_val[current_index]
            queue.append(current_val)
        
        current_val = value
        for i in reversed(range(1,len(indexes))):
            index = indexes[i]
            current = queue.pop()
            current[index] = current_val
            current_val = current
        super().__setitem__(index, current_val)


def main():
    import doctest
    print(doctest.testmod())
    # examples:
    mylist3 = List([[[[[[1]]]]]])
    print(mylist3[0,0,0,0,0,0])
    mylist4 = List([[[1,2,3,33],[4,5,6,66]],
        [[7,8,9,99],[10,11,12,122],['BAD3','BAD2','BAD1','THIS_GOOD']],[[13,14,15,155],[16,17,18,188]]]
    )
    print(mylist4[1,2,3])

if __name__ == "__main__":
    main()