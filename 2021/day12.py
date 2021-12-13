from pathlib import Path
from collections import defaultdict
path = Path.cwd() / 'input' / 'day12.txt'
dic = defaultdict(list)
with open(path) as f:
    for line in f.readlines():
        a, b = line.strip().split('-')
        dic[a].append(b)
        dic[b].append(a)

# # test_set
# lines = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']
# dic = defaultdict(list)
# for line in lines:
#     a, b = line.strip().split('-')
#     dic[a].append(b)
#     dic[b].append(a)

# Part 1
to_do = [['start', set()]] # position , path_for_lower
answer_p1 = 0
while to_do:
    x, p = to_do.pop()
    if x == 'end': answer_p1 += 1
    else:
        for nx in dic[x]:
            if nx == 'start' : continue
            if nx in p : continue
            
            if nx.islower() : to_do.append([nx, p.union({nx})])
            else: to_do.append([nx, p])
print(answer_p1)
print('-'*30)


# Part 2
to_do = [['start', True, set()]] # position , have_time, path_for_lower
answer_p2 = 0
while to_do:
    x, t, p = to_do.pop()
    if x == 'end': answer_p2 += 1
    else:
        for nx in dic[x]:
            if nx == 'start' : continue

            if nx in p : 
                if t : to_do.append([nx, False, p])
                else : continue
            elif nx.islower() : to_do.append([nx, t, p.union({nx})])
            else: to_do.append([nx, t, p])
print(answer_p2)