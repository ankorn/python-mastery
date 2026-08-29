def portfolio_cost (fname):
    sum = 0
    
    with open(fname, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split()
            amount = line[1]
            price = line[2]
            
            try:
                sum += (float(amount) * float(price))
            except ValueError as e:
                print(f'Couldn\'t parse: {line}: {e}')
            
    return sum

if __name__ == '__mane__':
    print(portfolio_cost('Data/portfolio3.dat'))