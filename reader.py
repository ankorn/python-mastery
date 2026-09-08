
import csv
from collections.abc import Iterable, Callable
from abc import ABC, abstractmethod

type Lines = Iterable[tuple[str, int, float]]
type Types = list[Callable[[str], str | int | float]]
type Record = dict[str, str | int | float]
type Records = list[Record]
class ClassWithFromRow(ABC):
    @abstractmethod
    def from_row(self, row: list[str]) -> Record:
        ...
        
def convert_csv(lines, convert: Callable[[list[str], list[str, int, float]]], *, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
        
    return list(map(lambda row: convert(headers, row), rows))

def csv_as_dicts(lines: Lines, types: Types, *, headers=None) -> Records:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def make_typed_dict(headers, row):
        return { name: func(value) for name, value, func in zip(headers, row, types) }
    
    records = convert_csv(lines, make_typed_dict)
    return records

def csv_as_instances(lines: Lines, cls: ClassWithFromRow, *, headers=None) -> Records:
    '''
    Convert lines of CSV data into a list of instances
    '''
    def make_instance(_, row):
        return cls.from_row(row)
    
    records = convert_csv(lines, make_instance)
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
    
    
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
up, down = counter(0)
r = up()
r = up()
r = up()
r = up()
r = up()


print(r)
