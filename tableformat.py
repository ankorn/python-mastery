class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

def print_table(records, fields, formatter: TableFormatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
        
class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join([str(d) for d in rowdata]))
        
class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        inner = ' '.join([f'<th>{h}</th>' for h in headers])
        print(f'<tr> {inner} </tr>')
        
    def row(self, rowdata):
        inner = ' '.join([f'<td>{h}</td>' for h in rowdata])
        print(f'<tr> {inner} </tr>')
        
from typing import Literal
def create_formatter(type: Literal['text', 'csv', 'html']):
    match type:
        case 'text':
            return TextTableFormatter()
        case 'csv':
            return CSVTableFormatter()
        case 'html':
            return HTMLTableFormatter()
        
    raise RuntimeError(f'no such formatter type: {type}')
        

# import stock, reader
# portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
# formatter = create_formatter('html')
# print_table(portfolio, ['name','shares','price'], formatter)