from collections import Counter
import readrides

rows = readrides.read_rides_as_dicts('Data/ctabus.csv')

rides2001 = { row['route']: 0 for row in rows }
rides2011 = { row['route']: 0 for row in rows }


for row in rows:
    if row['date'].endswith('2001'):
        rides2001[row['route']] += row['rides']
    if row['date'].endswith('2011'):
        rides2011[row['route']] += row['rides']
            
c = Counter()

for key in rides2001:
    c[key] = rides2011[key] - rides2001[key]
    
print(c.most_common(5))