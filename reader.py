
import csv
from collections.abc import Iterable, Callable
from abc import ABC, abstractmethod
import logging

type Lines = Iterable[tuple[str, int, float]]
type Types = list[Callable[[str], str | int | float]]
type Record = dict[str, str | int | float]
type Records = list[Record]
class ClassWithFromRow(ABC):
    @abstractmethod
    def from_row(self, row: list[str]) -> Record:
        ...
        
log = logging.getLogger(__name__)
        
def convert_csv(lines, convert: Callable[[list[str], list[str, int, float]]], types: Types, *, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    
    records = []
    for i, row in enumerate(rows):
        error = False
        message = None
        for t, v in zip(types, row):
            try:
                t(v)
            except ValueError as e:
                message = e
                error = True
                
        if error:
            log.warning(f'Row {i + 1}: Bad row: {row}')
            
            if message:
                log.debug(f'Row {i + 1}: Reason: {message}')
        else:
            records.append(convert(headers, row))
        
    return records

def csv_as_dicts(lines: Lines, types: Types, *, headers=None) -> Records:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def make_typed_dict(headers, row):
        return { name: func(value) for name, value, func in zip(headers, row, types) }
    
    records = convert_csv(lines, make_typed_dict, types)
    return records

def csv_as_instances(lines: Lines, cls: ClassWithFromRow, types: Types, *, headers=None) -> Records:
    '''
    Convert lines of CSV data into a list of instances
    '''
    def make_instance(_, row):
        return cls.from_row(row)
    
    records = convert_csv(lines, make_instance, types)
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
