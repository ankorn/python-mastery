import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares
        
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(record)
    return portfolio
        
def print_portfolio(portfolio):
    headings = vars(portfolio[0]).keys()
    
    formatted_s = ['%10s'] * len(headings)
    formatted_s = ' '.join(formatted_s)
        
    print(formatted_s % tuple(headings))
    
    print(formatted_s % tuple(['----------'] * len(headings)))
    
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))