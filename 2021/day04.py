import copy, os
path = os.path.join(os.getcwd(), 'input', 'day04.txt')
with open(path) as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

cmd = list(map(int, lines[0].split(',')))
arrs = []
for i in range(1, len(lines), 6):
    temp = []
    for j in range(1, 6):
        for k in map(int, lines[i+j].split()):
            temp.append(k)
    arrs.append(temp)

def check(arrs, idx, t):
    for i, v in enumerate(arrs[idx]):
        if v == t : 
            arrs[idx][i] = -1
            if sum([arrs[idx][j] for j in range(i%5, 25, 5)]) == -5 : return True 
            if sum([arrs[idx][j] for j in range(i//5 * 5, i//5 * 5 + 5)]) == -5 : return True 
            return False

# Part1
end = False
t_idx = 0
arr_p1 = copy.deepcopy(arrs)
while not end:
    for idx in range(len(arr_p1)):
        if check(arr_p1, idx, cmd[t_idx]): 
            end = True
            print((sum(arr_p1[idx]) + arr_p1[idx].count(-1)) * cmd[t_idx])
            break
    t_idx += 1

print('-'*30)


# Part2
max_idx = 0
answer = 0
arr_p2 = copy.deepcopy(arrs)
for idx in range(len(arr_p2)):
    for jdx, c in enumerate(cmd):
        if check(arr_p2, idx, c):
            if jdx > max_idx :
                max_idx = jdx
                answer = (sum(arr_p2[idx]) + arr_p2[idx].count(-1)) * c
            break
print(answer)