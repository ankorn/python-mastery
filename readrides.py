import csv
import tracemalloc
import collections

class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []
        
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            r = []
            for route, date, daytype, rides in zip(self.routes[index], self.dates[index], self.daytypes[index], self.numrides[index]):
                r.append({
                    'route': route,
                    'date': date,
                    'daytype': daytype,
                    'rides': rides
                })

            return r
        
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

# class Row:
#     def __init__(self, route, date, daytype, rides):
#         self.route = route
#         self.date = date
#         self.daytype = daytype
#         self.rides = rides

# from collections import namedtuple
# Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            
            # record = {
            #     'route': route,
            #     'date': date,
            #     'daytype': daytype,
            #     'rides': rides,
            # }
            
            # record = Row(route, date, daytype, rides)
            
            records.append(record)
            
    return records

def read_rides_as_dicts(filename):
    tracemalloc.start()
    # records = []
    records = RideData() # 300+ to 90 MB
    
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
            
    current, peak = tracemalloc.get_traced_memory()
    print('current', current / (1024**2))
    print('peak', peak / (1024**2))
            
    return records

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())