import csv

class Stock:
    types = (str, int, float)
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    @classmethod
    def from_row(cls, row: list[str]):
        values = [func(value) for value, func in zip(row, cls.types)]
        
        return cls(*values)
        
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares
        
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
    types = (str, int, Decimal)