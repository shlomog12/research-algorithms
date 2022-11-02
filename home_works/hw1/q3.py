"""
 Author: Shlomo Glick
 Since : 2022-10
"""

def print_sorted(struct):
    """
    The function receives a data structure containing various types and additional structures
    The function should print the structures sorted at all depth levels

    >>> print_sorted(struct=get_struct1())
    [(['222', {'a': "{'4', '5', '6'}", 'b': ['Aaa', 'ggg', 't'], 'c': '3'}], 'ff'), '111', 'bbba', {'aa': '2', 'b': '0', 'c': '1', 'xx4': [('2', '5', 's', 'z', {'55': '10', '66': '3', '77': '9'}), '1', '2', '55']}]
    >>> print_sorted(struct=get_struct2())
    ['111', [('1', '3', '4'), 'd', {}], 'ta', {'aa': '2', 'b': '0', 'c': '1', 'xx4': [('2', '5', 's', 'z', {'55': '10', '66': '3', '77': '9'}), '1', '2', '55']}, {0: '2'}, {}]
    """
    print(sorted_struct(struct=struct))

def sorted_struct(struct):
    swith = {dict: sort_dict, set: sort_set, list: sort_list, tuple: sort_tuple}
    sort_func = swith.get(type(struct), str)
    return sort_func(struct)

def sort_dict(struct):
    sorted_keys = sorted(struct, key=lambda x: str(x))
    ans = {}
    for k in sorted_keys:
        ans[k] = sorted_struct(struct[k])
    return ans

def sort_list(struct):
    list_objects = []
    for v in struct:
        list_objects.append(sorted_struct(v))
    return sorted(list_objects, key=lambda x: str(x))

def sort_set(struct):
    ans = str(sort_list(struct))
    return '{' + ans[1:-1] + '}'

def sort_tuple(struct):
    return tuple(sort_list(struct))


def get_struct1():
    return [
    ('ff', 
        [
            '222',
            {
                "c": 3,
                "a": {4, 5, 6},
                "b": ["Aaa", "ggg", "t"]
            }
        ]
    ),
    "bbba",
    "111",
    {
        "aa": 2,
        "c": 1,
        "b": 0,
        "xx4": [
                1,
                2,
                "55",
                (
                    's',
                    5,
                    {
                        "77": 9,
                        "55":10,
                        "66": 3
                    }, 
                    '2',
                    "z"
                )
            ]
        }
    ]

def get_struct2():
    return[
        {},
        ["d",(1,4,3),{}],
        "ta",
        "111",
        {0: 2},
        {
            "aa": 2,
            "c": 1,
            "b": 0,
            "xx4": [
                    1,
                    2,
                    "55",
                    (
                        's',
                        5,
                        {
                            "77": 9,
                            "55":10,
                            "66": 3
                        }, 
                        '2',
                        "z"
                    )
                ]
            }
        ]

def main():
    import doctest
    print(doctest.testmod())

if __name__ == "__main__":
    main()