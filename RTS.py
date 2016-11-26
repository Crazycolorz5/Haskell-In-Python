#class Thunk:
#    def __init__(self, res, isTerminal = False):
#        self.__term__ = isTerminal
#        self.__res__ = res
#    def evaluate(self):
#        while not self.__term__:
#            tempRes = self.__res__()
#            self.__term__ = tempRes.__term__
#            self.__res__ = tempRes.__res__
#        return self.__res__


# Conventions:
#   - Wrap everything that doesn't get evaluated in WHNF in a thunk.
#   - No outside-of-class functions take or return Thunks (maybe?)
#   - Functions in classes may return Thunks. (eg tail list)


# Base object class
class HaskObj():
    def __init__(): pass
    #def __new__(cls, *args): 
    #    super(cls).__new__()
    #def __del__(cls, *args):
    #    super(cls).__del__()
    # <
    def __lt__(self, other): 
        raise NotImplementedError()
    # <=
    def __le__(self, other): 
        raise NotImplementedError()
    # ==
    def __eq__(self, other): 
        raise NotImplementedError()
    # !=
    def __ne__(self, other): 
        raise NotImplementedError()
    # >
    def __gt__(self, other): 
        raise NotImplementedError()
    # >=
    def __ge__(self, other): 
        raise NotImplementedError()
    # unary +
    def __pos__(self): 
        raise NotImplementedError()
    # unary -
    def __neg__(self): 
        raise NotImplementedError()
    # ~
    def __invert__(self): 
        raise NotImplementedError()
    # abs()
    def __abs__(self): 
        raise NotImplementedError()
    # round()
    def __round__(self): 
        raise NotImplementedError()
    # floor()
    def __floor__(self): 
        raise NotImplementedError()
    # ceil()
    def __ceil__(self): 
        raise NotImplementedError()
    # trunc()
    def __trunc__(self): 
        raise NotImplementedError()
    # (+)
    def __add__(self, other): 
        raise NotImplementedError()
    # (-)
    def __sub__(self, other): 
        raise NotImplementedError()
    # (*)
    def __mul__(self, other): 
        raise NotImplementedError()
    # (//)
    def __div__(self, other): 
        raise NotImplementedError()
    # (/)
    def __truediv__(self, other): 
        raise NotImplementedError()
    # (%)
    def __mod__(self, other): 
        raise NotImplementedError()
    # divmod()
    def __divmod__(self, other): 
        raise NotImplementedError()
    # (**)
    def __pow__(self, other): 
        raise NotImplementedError()
    # (<<)
    def __lshift__(self, other): 
        raise NotImplementedError()
    # (>>)
    def __rshift__(self, other): 
        raise NotImplementedError()
    # (&)
    def __and__(self, other): 
        raise NotImplementedError()
    # (|)
    def __or__(self, other): 
        raise NotImplementedError()
    # (^)
    def __xor__(self, other): 
        raise NotImplementedError()
    # flip (+)
    def __radd__(self, other): 
        return other + self
    # flip (-)
    def __rsub__(self, other): 
        return other - self
    # flip (*)
    def __rmul__(self, other): 
        return other * self
    # flip (//)
    def __rdiv__(self, other): 
        raise NotImplementedError()
    # flip (/)
    def __rtruediv__(self, other): 
        return other / self
    # flip (%)
    def __rmod__(self, other): 
        return other % self
    # divmod()
    def __rtruediv__(self, other): 
        raise NotImplementedError()
    # flip (**)
    def __rpow__(self, other): 
        raise NotImplementedError()
    # flip (<<)
    def __rlshift__(self, other): 
        raise NotImplementedError()
    # flip (>>)
    def __rrshift__(self, other): 
        raise NotImplementedError()
    # flip (&)
    def __rand__(self, other): 
        raise NotImplementedError()
    # flip (|)
    def __ror__(self, other): 
        raise NotImplementedError()
    # flip (^)
    def __rxor__(self, other): 
        raise NotImplementedError()
    
    def __int__(self): 
        raise NotImplementedError()
    def __long__(self): 
        raise NotImplementedError()
    def __float__(self): 
        raise NotImplementedError()
    
    #show
    def __str__(self): 
        raise NotImplementedError()
    
    #($)
    def __call__(self, *args): 
        raise NotImplementedError()

