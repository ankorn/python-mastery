from structure import Structure
import inspect

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    
    def __init__(self, name, shares, price):
        self._init()
        
    @classmethod
    def set_fields(cls):
        syg = inspect.signature(cls.__init__)
        cls._fields = tuple(syg.parameters)[1:] # skip self

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
