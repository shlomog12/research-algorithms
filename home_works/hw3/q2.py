"""
 Author: Shlomo Glick
 Since : 2022-11
"""



def lastcall(func):
    """
    It's a decorator that keeps a history of runs.
    The decorator checks whether the current input
    is the same as any previous input. If not - he runs the function as usual.
    If so - he does not run the function, but writes an appropriate message.
    >>> print(pow2(4))
    16
    >>> print(pow2(8))
    64
    >>> print(pow2(4))
    I already told you that the answer is 16
    >>> print(add1(4))
    5
    >>> print(add1(4))
    I already told you that the answer is 5
    >>> print(pow2(4))
    I already told you that the answer is 16
    >>> print(length([4, 2]))
    2
    >>> print(length([4,1]))
    2
    >>> print(length([4,2]))
    I already told you that the answer is 2
    >>> print(length('test'))
    4
    >>> print(length('test'))
    I already told you that the answer is 4
    """


    def wrapper(arg):
        if func.__name__ not in lastcall.history:
            lastcall.history[func.__name__] = {}
        
        cuurent_history = lastcall.history[func.__name__]
        if str(arg) in cuurent_history.keys():
            if cuurent_history[str(arg)] is None:
                return 'We have already run the function on this argument'
            else:
                return f'I already told you that the answer is {cuurent_history[str(arg)]}'
        else:
            lastcall.history[func.__name__][str(arg)] = func(arg)
            return lastcall.history[func.__name__][str(arg)]
    return wrapper
lastcall.history = {}

################ function for the tests ###################3
@lastcall
def printX(arg):
    print(f'x: {arg}')

@lastcall
def pow2(a):
    return a**2

@lastcall
def add1(a):
    return a+1

@lastcall
def length(a):
    return len(a)


def main():
    import doctest
    print(doctest.testmod())
    # examples:
    print(pow2(1))   # returns 1
    print(pow2(10))   # returns 100
    print(pow2(1))   # returns "I already told you that the answer is 1"
    print(add1(9))   # returns 10
    print(add1(8))   # returns 9
    print(add1(9))   # returns "I already told you that the answer is 10"
    print(length('example'))   # returns 7
    print(length('example'))   # returns "I already told you that the answer is 7"

if __name__ == "__main__":
    main()

