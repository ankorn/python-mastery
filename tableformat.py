from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

def print_table(records, fields, formatter: TableFormatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('expected a TableFormatter')
    
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
        
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
        
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
        
from typing import Literal
def create_formatter(type: Literal['text', 'csv', 'html'], upper_headers=False, column_formats=None):
    match type:
        case 'text':
            Formatter = TextTableFormatter
        case 'csv':
            Formatter = CSVTableFormatter
        case 'html':
            Formatter = HTMLTableFormatter
        case _:
            raise RuntimeError(f'no such formatter type: {type}')

    if upper_headers:
        class UpperHeadersFormatter(UpperHeadersMixin, Formatter):
            pass
        
        return UpperHeadersFormatter()
    
    if column_formats:
        class ColumnFormatter(ColumnFormatMixin, Formatter):
            formats = column_formats
            pass
        
        return ColumnFormatter()
    
    return Formatter()

import sys
class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file
    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout

import stock, reader
portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
# formatter = create_formatter('text', upper_headers=True)
formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
print_table(portfolio, ['name','shares','price'], formatter)