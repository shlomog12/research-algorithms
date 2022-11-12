


# myDict = {}
def lastcall(func):
    def wrapper(arg):
        if arg in lastcall.myDict.keys():
            return f'I already told you that the answer is {lastcall.myDict[arg]}'
        else:
            lastcall.myDict[arg] = func(arg)
            return lastcall.myDict[arg]
    return wrapper
lastcall.myDict = {}


@lastcall
def printX(a):
    print(f'xxx: {a}')

@lastcall
def mult2(a):
    return a**2


print(mult2(4))
print(mult2(4))
print(mult2(8))
print(mult2(4))
print(mult2(2))
print(mult2(16))
print(mult2(2))