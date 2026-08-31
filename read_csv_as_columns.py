import collections
import tracemalloc
import csv

class DataCollection(collections.abc.Sequence):
    def __init__(self, headers, convs):
        self.convs_map = {}
        self.values = {}
        self.headers = headers

        for h, c in zip(headers, convs):
            self.values[h] = []
            self.convs_map[h] = c
            
        
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.values[self.headers[0]])

    def __getitem__(self, index):
        # if isinstance(index, slice):
        #     r = []
        #     for route, date, daytype, rides in zip(self.routes[index], self.dates[index], self.daytypes[index], self.numrides[index]):
        #         r.append({
        #             'route': route,
        #             'date': date,
        #             'daytype': daytype,
        #             'rides': rides
        #         })

        #     return r
        
        return {
            h: self.values[h][index] for h in self.headers
        }

    def append(self, d):
        for h in self.headers:
            self.values[h].append(d[h])
            
def read_csv_as_columns(path, convs):
    tracemalloc.start()
    
    with open(path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = DataCollection(headers, convs)
        
        for row in rows:
            row_dict = { name: conv(value) for name, conv, value in zip(headers, convs, row) }
            records.append(row_dict)
            
    current, peak = tracemalloc.get_traced_memory()
    print('current', current / (1024**2))
    print('peak', peak / (1024**2))
            
    return records