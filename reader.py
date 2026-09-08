
import csv
from collections.abc import Iterable, Callable

type Lines = Iterable[tuple[str, int, float]]
type Types = list[Callable[[str], str | int | float]]
type Record = dict[str, str | int | float]
type Records = list[Record]
class ClassWithFromRow:
    def from_row(self, row: list[str]) -> Record:
        pass

def csv_as_dicts(lines: Lines, types: Types, *, headers=None) -> Records:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    records: Records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Lines, cls: ClassWithFromRow, *, headers=None) -> Records:
    '''
    Convert lines of CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)

def read_csv_as_instances(filename, cls, *, headers=None):
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)

port = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
print(port)

import stock
port = read_csv_as_instances('Data/portfolio.csv', stock.Stock)
print(port)