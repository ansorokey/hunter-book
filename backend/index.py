
from data import largeMonsters

res = []
for m in largeMonsters:
    mon = {
        'name': m[0],
        'species': m[1],
        'size': m[2]
    }
    res.append(mon)

# Open the file - a flag to append (write to the end of the file)
f = open('./data.py', 'a')
f.write('largeMonsters = {0}'.format(res))
