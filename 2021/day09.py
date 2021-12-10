import os
path = os.path.join(os.getcwd(), 'input', 'day09.txt')
with open(path) as f:
    location = []
    for line in f.readlines():
        temp = []
        for i in line.strip():
            temp.append(int(i))
        location.append(temp)

# # test
# location = [
#     [2,1,9,9,9,4,3,2,1,0],
#     [3,9,8,7,8,9,4,9,2,1],
#     [9,8,5,6,7,8,9,8,9,2],
#     [8,7,6,7,8,9,6,7,8,9],
#     [9,8,9,9,9,6,5,6,7,8]]

# Part 1
answer_p1 = 0
mx, my = len(location) - 1, len(location[0]) - 1
def check_low(x, y):
    t = location[x][y]
    if x > 0 and t >= location[x-1][y] : return 
    if y > 0 and t >= location[x][y-1] : return 
    if x < mx and t >= location[x+1][y] : return 
    if y < my and t >= location[x][y+1] : return 
    return [x,y]

low_point = []
answer_p1 = 0
for i in range(mx+1):
    for j in range(my+1):
        p = check_low(i,j)
        if p != None: 
            low_point.append(p)
            answer_p1 += (location[p[0]][p[1]] + 1)
print(answer_p1)
print('-'*30)


# Part 2
answer_p2 = []
for i, j in low_point:
    visited = set()
    to_do = [[i,j]]
    area = 0
    while to_do:
        x, y = to_do.pop()
        if (x,y) in visited: continue
        visited.add((x,y))
        area += 1
        for nx, ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
            if 0 <= nx <= mx and 0 <= ny <= my and location[nx][ny] != 9:
                to_do.append([nx,ny])
    answer_p2.append(area)
answer_p2.sort()
print(answer_p2[-1] * answer_p2[-2] * answer_p2[-3])