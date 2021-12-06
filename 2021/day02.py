import os
path = os.path.join(os.getcwd(), 'input', 'day02.txt')
with open(path) as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

# Part1
x, y = 0, 0
for l in lines:
    c, n = l.split()
    n = int(n)
    if c == 'up' : y -= n
    elif c == 'down' : y += n
    else: x += n
print(x*y)
print('-'*30)

# Part1
x, y, aim = 0, 0, 0
for l in lines:
    c, n = l.split()
    n = int(n)
    if c == 'up' : aim -= n
    elif c == 'down' : aim += n
    else:
        x += n
        y += aim * n
print(x*y)