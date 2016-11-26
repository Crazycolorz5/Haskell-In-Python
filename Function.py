from Control.Arrow import *
# Wrapper for a 1-adic function
# 
class Function(Arrow):
    def __init__(self, val):
        self.val = val
    #id = None#Function(lambda x: x)
    def compose(self, other):
        return Function(lambda x: self(other(x)))
    def __call__(self, arg):
        return self.val(arg)
Function.id = Function(lambda x: x)


import inspect
from functools import reduce
def makeFunction(f):
    numArgs = len(inspect.getargspec(f).args)
    return nestLambdas(numArgs, f)

def nestLambdas(number, f):
    return Function(f) if number == 1 else Function(lambda x: nestLambdas(number - 1, lambda *args: f(*args, x)))

#@makeFunction
#def test(a,b,c):
#    return a+b+c
