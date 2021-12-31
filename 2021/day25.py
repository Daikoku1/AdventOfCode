from pathlib import Path
import copy
path = Path.cwd() / 'input' / 'day25.txt'
data = open(path).read().strip()

# Test data
# data ='''
# v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>'''.strip()

data = [list(d) for d in data.split('\n')]

# Part 1
answer_p1 = 0
end = False
while not end :
    answer_p1 += 1
    end = True
    for x1 in range(len(data)):
        moveable = []
        for y1 in range(len(data[0])-1):
            if data[x1][y1] == '>' and data[x1][y1+1] == '.':
                moveable.append(y1)
        if data[x1][len(data[0])-1] == '>' and data[x1][0] == '.':
            data[x1][0] , data[x1][len(data[0])-1] = '>', '.'
            end = False
        if moveable : end = False
        for my in moveable:
            data[x1][my] , data[x1][my+1] = '.', '>'
    
    for y2 in range(len(data[0])):
        moveable = []
        for x2 in range(len(data)-1):
            if data[x2][y2] == 'v' and data[x2+1][y2] == '.':
                moveable.append(x2)
        if data[len(data)-1][y2] == 'v' and data[0][y2] == '.':
            data[0][y2] , data[len(data)-1][y2] = 'v', '.'
            end = False
        if moveable : end = False
        for mx in moveable:
            data[mx][y2] , data[mx+1][y2] = '.', 'v'
print(answer_p1)