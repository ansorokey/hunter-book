
from data import largeMonsters, smallMonsters

res = []
for m in smallMonsters:
    mon = {
        'name': m[0],
        'size': m[1]
    }
    res.append(mon)

# Open the file - a flag to append (write to the end of the file)
f = open('./data.py', 'a')
f.write('smallMonsters = {0}'.format(res))
