from RTS import *

class Category(HaskObj):
    # Minimal definition: id, compose
    id = NotImplementedError()
    def compose(self, other):
        raise NotImplementedError()
    
    def composeLtR(self, other):
        return other.compose(self)
    composeRtL = compose
