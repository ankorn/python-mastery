class Stock:
    _types = (str, int, float)
    __slots__ = '_shares', '_price', 'name'
    
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self._price = price
        
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))
        
    @classmethod
    def from_row(cls, row: list[str]):
        values = [func(value) for value, func in zip(row, cls._types)]
        
        return cls(*values)
        
    @property
    def cost(self):
        return self._shares * self._price
    
    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, v):
        if not isinstance(v, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}')
        
        if v < 0:
            raise ValueError('shares must be >= 0')
        
        self._shares = v
        
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, v):
        if not isinstance(v, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}')
        
        if v < 0:
            raise ValueError('price must be >= 0')
        
        self._price = v
    
    def sell(self, nshares):
        self._shares -= nshares
        
def print_portfolio(portfolio):
    headings = vars(portfolio[0]).keys()
    
    formatted_s = ['%10s'] * len(headings)
    formatted_s = ' '.join(formatted_s)
        
    print(formatted_s % tuple(headings))
    
    print(formatted_s % tuple(['----------'] * len(headings)))
    
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
        
from decimal import Decimal
class DStock(Stock):
    _types = (str, int, Decimal)
    
class SimpleStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
