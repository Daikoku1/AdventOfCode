from pathlib import Path
path = Path.cwd() / 'input' / 'day17.txt'
with open(path) as f:
    cmd = f.readline().split(':')[1]
    print(cmd)
x1, x2 = map(int, cmd.split(',')[0].split('=')[1].split('..'))
y1, y2 = map(int, cmd.split(',')[1].split('=')[1].split('..'))

y1, y2 = abs(y1), abs(y2)
y1, y2 = min(y1, y2), max(y1, y2)
x1, x2 = min(x1,x2), max(x1,x2)


# Part 1
# the shot when they going up from y == 0 and going down to y == 0 is same   
# It is because V_y is minus 1 by time.
#     - v(0), v(0) - 1 ... v(0) - v(0) | 0 , 1, 2, ... v(0)
# so if V_y > 0 at first
#   - when shot in y == 0 : V_y = V_y(0) + 1
# so if V_y(0) > y2: shot can't reach at target area

# answer = y2 + y2-1 + ... + 1 = (y2)*(y2+1) // 2
answer = (y2)*(y2+1) // 2
print(answer)
print('-'*30)


# Part 2
def count_x_time(x1, x2):
    dic = {i : set() for i in range(x2+1)}
    for x in range(x2+1):
        sum_x = 0
        time = 0
        while time < x:
            sum_x += x - time
            time += 1
            if sum_x > x2 : break
            if sum_x >= x1 : 
                dic[time].add(x)
        if x1 <= sum_x <= x2 :
            for t in range(time+1, x2+1):
                dic[t].add(x)
    return dic

x_time = count_x_time(x1, x2)
answer_p2 = 0
# V_y(0) > 0 
for y in range(1, y2):
    temp = set()
    sum_n = 0
    t = 0
    while True:
        t += 1
        sum_n += y + t
        if sum_n > y2 : break
        if sum_n >= y1 : temp = temp.union(x_time[2*y+1 + t])
    answer_p2 += len(temp)

# V_y(0) < 0
for y in range(y2+1):
    temp = set()
    sum_n = 0
    t = 0
    while True:
        sum_n += y + t
        t += 1
        if sum_n > y2 : break
        if sum_n >= y1 : temp = temp.union(x_time[t])
    answer_p2 += len(temp)

print(answer_p2)
