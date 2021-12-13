from pathlib import Path
from collections import defaultdict
path = Path.cwd() / 'input' / 'day13.txt'
dic = defaultdict(list)
with open(path) as f:
    arr = []
    cmd = []
    max_x, max_y = 0, 0
    for line in f.readlines():
        if line[0] == 'f': cmd.append(line.split()[2])
        elif line.strip() == '' : continue
        else:
            a, b = map(int, line.strip().split(','))
            arr.append([a,b])
            max_x = max(max_x, a)
            max_y = max(max_y, b)

import numpy as np
li = np.zeros(shape = (max_y+1, max_x+1), dtype = 'int8')
for x, y in arr:
    li[y][x] = 1

# Part 1
for idx, c in enumerate(cmd):
    d, t = c.split('=')
    t = int(t)
    if d == 'x':
        for i in range(min(t, max_x - t)):
            li[:,t-i-1] += li[:, t+i+1]
        li = li[:, :t]
        max_x = t - 1
    else:
        for i in range(min(t, max_y - t)):
            li[t-i-1, : ] += li[t+i+1, : ]
        li = li[:t, : ]
        max_y = t - 1
    if idx == 0 :
        print(np.sum(np.where(li > 0 , 1, 0)))
        print('-'*30)


# Part 2
for row in np.where(li > 0 , '0', ' '):
    print(''.join(row))