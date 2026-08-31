import csv
import tracemalloc

def read_csv_as_dicts(path, convs):
    tracemalloc.start()
    
    result = []
    f = open(path)
    rows = csv.reader(f)
    headers = next(rows)
    
    for row in rows:
        row_dict = { name: conv(value) for name, conv, value in zip(headers, convs, row) }
        result.append(row_dict)
        
    current, peak = tracemalloc.get_traced_memory()
    print('current', current / (1024**2))
    print('peak', peak / (1024**2))
    
    return result

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
    