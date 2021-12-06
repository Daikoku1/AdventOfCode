import os
path = os.path.join(os.getcwd(), 'input', 'day05.txt')
with open(path) as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

# part1
ans = 0
dic = {}
for l in lines:
    p1, p2 = l.split('->')
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    
    if x1 == x2:
        for i in range(min(y1,y2), max(y1,y2)+1):
            if (x1, i) in dic:
                if dic[(x1,i)] == 1 : ans += 1
                dic[(x1, i)] += 1
            else: dic[(x1, i)] = 1
    elif y1 == y2:
        for i in range(min(x1,x2), max(x1,x2)+1):
            if (i, y1) in dic:
                if dic[(i, y1)] == 1 : ans += 1
                dic[(i, y1)] += 1
            else: dic[(i, y1)] = 1
print(ans)
print('-'*30)


# part2
for l in lines:
    p1, p2 = l.split('->')
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    
    if abs(x1- x2) == abs(y1-y2):
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        for i, j in zip(range(x1, x2+dx, dx), range(y1, y2+dy, dy)):
            if (i, j) in dic:
                if dic[(i, j)] == 1 : ans += 1
                dic[(i, j)] += 1
            else: dic[(i, j)] = 1
print(ans)