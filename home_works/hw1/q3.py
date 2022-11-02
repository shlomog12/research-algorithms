import re
import time
from traceback import print_tb

def print_sorted(struct):
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




struct=[
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
print_sorted(struct=struct)
struct=[
    "bbba",
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
print_sorted(struct=struct)

# print_sorted(struct=struct)
# z65 = ['1', '2', '55']
# tt65 =('2', '5', 's', 'z', "{'55': '10', '66': '3', '77': '9'}")
# z65.append(tt65)
# print(z65)
# z65 =[]
# tt1 = 'bbba'
# tt2 = 111
# tt3 = 1
# tt4 = 2
# tt5 = 55
# tt6 = ('2', '5', 's', 'z', "{'55': '10', '66': '3', '77': '9'}")
# z65.append(tt1)
# z65.append(tt2)
# z65.append(tt3)
# z65.append(tt4)
# z65.append(tt5)
# z65.append(tt6)
# print(z65)
# s = 'a'
# if hasattr(s, '__iter__'):
#     print('sy')
# else:
#     print('sn')
# print_sorted(struct={"zz": 4 ,"aa": 2, "c": 1})

# print_sorted(struct=["bbba", "111"])  #, {"aa": 2, "c": 1}])


# def foo(str2):
#     if len(str(str2)) < 2:
#         return str2 
#     time.sleep(0.2)
#     try:
#         str2.sort()
#         print(f'str2 = {str2}, try')
#         return str(str2)
#     except:
#         print(f'str2 = {str2}, exp')
#         ans = ''
#         for d in str2:
#             x = foo(d)
#             ans +=x
#         return ans









# xx = (1,4,6,3,7)
# print(sorted(xx))
