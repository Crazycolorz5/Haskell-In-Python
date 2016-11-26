from RTS import *
from Function import *

# Wrapper for 2-tuples.
# Tuple :: *->*->*
class Tuple(HaskObj):
    def __init__(self, a, b):
        self.fst = a
        self.snd = b

# fst :: Tuple a b -> a
fst = Function(lambda t: t.fst)
# snd :: Tuple a b -> b
snd = Function(lambda t: t.snd)

# curry :: (Tuple a b -> c) -> a -> b -> c
curry = Function(lambda f: Function(lambda a: Function(lambda b: f(Tuple(a, b)))))
# uncurry :: (a -> b -> c) -> Tuple a b -> c)
uncurry = Function(lambda f: Function(lambda t: f(fst(t))(snd(t))))

class Eq(HaskObj):
    # Minimal definition: (== | !=)
    def __eq__(self, other): 
        return not self != other
    def __ne__(self, other):
        return not self == other
    
class Ord(Eq): 
    # Minimal definition: (compare | <=)
    def compare(self, other): 
        return -1 if self <= other and not self == other else 0 if self == other else 1
    def __lt__(self, other): 
        return self.compare(other) == -1
    def __le__(self, other):
        return self.compare(other) <= 0
    def __gt__(self, other): 
        return self.compare(other) > 0
    def __ge__(self, other): 
        return self.comapre(other) >= 0

class Show(HaskObj):
    # Minimal definition: show
    #Original haskell had showsPrec and showList, but neither will play well with python, nor is showsPrec that useful at the end level.
    def __str__(self):
        return self.show()
    def show(self):
        raise NotImplementedError()

class Read(HaskObj):
    # Minimal definition: read
    def read(self):
        raise NotImplementedError()

class Enum(HaskObj):
    # Minimal definition: toEnum, fromEnum
    #toEnum :: Int -> a
    @classmethod
    def toEnum(cls, val):
        raise NotImplementedError()
    #fromEnum :: a -> Int
    def fromEnum(self):
        raise NotImplementedError()
    
    def succ(self):
        return self.toEnum(self.fromEnum() + 1)
    def pred(self):
        return self.toEnum(self.fromEnum() - 1)
    
class Num(HaskObj):
    # Minimal definition: __add__, __mul__, __abs__, signum, fromInteger, __neg__
    def signum(self):
        raise NotImplementedError()
    @classmethod
    def fromInteger(cls, anInt):
        raise NotImplementedError()

class Real(Num, Ord):
    # Minimal definition: toRational
    def toRational(self):
        raise NotImplementedError()


class Integral(Real, Enum):
    #Minimal definition: quotRem, toInteger
    
    #quotRem :: a -> a -> Tuple a a
    def quotRem(self, divisor):
        raise NotImplementedError()
    #toInteger :: a -> Integer
    def toInteger(self):
        raise NotImplementedError()

    def quot(self, other):
        return fst(self.quotRem(other))
    def rem(self, other):
        return snd(self.quotRem(other))
    def div(self, other):
        quotRem = self.quot(other)
        quot = fst(quotRem)
        rem = fst(quotRem)
        return quot if self < other or rem == boxInt(rem, 0) else quot - boxInt(quot, 1)

#Eq implied by Ord
#Num and Ord implied by Real
#Read and Enum implied by Integral
class Integer(Show, Integral): #, Integral, Data, Read, Real, Ix, Bits, PrintfArg
    def __init__(self, val):
        self.val = int(val)
    def __eq__(self, other):
        return self.val == other.val
    def compare(self, other):
        return self.val - other.val
    def show(self):
        return str(self.val)
    
    def __add__(self, other):
        return Integer(self.val + other.val)
    def __sub__(self, other):
        return Integer(self.val - other.val)
    def __mul__(self, other):
        return Integer(self.val * other.val)
    def __abs__(self, other):
        return self if self >= 0 else -self
    def __neg__(self):
        return Integer(-self.val)
    def signum(self):
        return 0 if self.val == 0 else 1 if self.val > 0 else -1
    def fromInteger(cls, anInt):
        return Integer(anInt)
    def toEnum(self):
        return self.val
    def fromEnum(cls, val):
        return Integer(val)
    def toRational(self):
        return Rational(self.val)

from fractions import Fraction
#TODO: Someday rewrite with Integers
class Rational(Fraction, Show):
    def __init__(self, val):
        try:
            super(Rational, self).__init__(val)
        except TypeError: #I only care about initializing Fraction.
            pass
    def show(self):
        return self.numerator.__str__() + " % " + self.denominator.__str__()
    def __str__(self):
        return self.show()

def boxInt(sample, raw):
    return raw if type(sample) is int else sample.fromInteger(raw)

@makeFunction
def factorial(n):
    return boxInt(n, 1) if n<=boxInt(n, 1) else n*factorial(n-boxInt(n, 1))

class List(Eq):
    def __init__(self, hd, tl):
        self.hd = hd
        self.tl = tl
    @classmethod
    def singleton(cls, x):
        self.hd = x
        self.tl = emptyList
    def cons(self, x):
        return List(x, self)
    def null(self):
        return self == emptyList
    def map(self, f):
        return emptyList if self.null() else List(f(self.hd), self.tl.map(f))
    def foldl(self, f, i):
        return i if self.null() else self.tl.foldl(f, f(i)(self.hd))
    def __eq__(self, other):
        return False if self is emptyList and not other is emptyList or not self is emptyList and other is emptyList else (self is other) or (self.hd == other.hd and self.tl == other.tl)
    
emptyList = List(None, None)
