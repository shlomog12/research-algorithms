"""
 Author: Shlomo Glick
 Since : 2022-10
"""

from __future__ import annotations
from typing import Callable

def safe_call(f: Callable, **kwargs):
    """
    This function receives as input another function and
    arguments with names, and calls the function with the arguments,
    but only they correspond exactly to the types defined in the annotation
    of the function


    def sum4(x: int, y:int ,z, w:float, l: list):
        return x+y+z+w
    
    A good example
    >>> safe_call(sum4, x=1, y=2, z=3.6, w=6.0, l=[])
    12.6

    Error: w should be type float but is type int
    >>> safe_call(sum4, x=1, y=2, z=3.6, w=6, l=[])
    Traceback (most recent call last):
        ...
    ValueError: Arguments do not fit annotations

    Error: w should be type list but is type int
    >>> safe_call(sum4, x=1, y=2, z=3.6, w=6.0, l=3)
    Traceback (most recent call last):
        ...
    ValueError: Arguments do not fit annotations

    A good example
    >>> safe_call(get_first_argumet, l=[1, 2, 4])
    1

    Error: l should be type list but is type dict
    >>> safe_call(get_first_argumet, l={'x': 3})
    Traceback (most recent call last):
        ...
    ValueError: Arguments do not fit annotations



    A good example with out arguments
    >>> safe_call(get1)
    1
    
    """
    with_annotations = {k: v  for k,v in kwargs.items() if k in f.__annotations__.keys()}
    if all([f.__annotations__[k] == type(v).__name__ for k, v in with_annotations.items()]):
        return f(**kwargs)
    else:
        raise ValueError("Arguments do not fit annotations")




def main():
    import doctest
    print(doctest.testmod())

if __name__ == "__main__":
    main()

############################ function for doctest

def sum4(x: int, y:int ,z, w:float, l: list):
    print(x+y+z+w)

def get_first_argumet(l: list): 
    if len(l) > 0:
        return l[0]
    else:
        return 0

def get1():
    return 1