from pathlib import Path
import numpy as np
path = Path.cwd() / 'input' / 'day11.txt'
arr = np.ones(shape = (10, 10), dtype = np.int8)
with open(path) as f:
    lines = []
    for i, l in enumerate(f.readlines()):
        for j, v in enumerate(map(int, l.strip())):
            arr[i][j] = v

# # test
# lines = ['5483143223','2745854711','5264556173','6141336146','6357385478',
#         '4167524645','2176841721','6882881134','4846848554','5283751526']
# arr = np.ones(shape = (10, 10), dtype = np.int8)
# for i, line in enumerate(lines):
#     for j, v in enumerate(line):
#         arr[i][j] = v


# Part 1
answer_p1, answer_p2 = 0, 0
while True:
    answer_p2 += 1
    arr += 1
    to_do = []
    for i, line in enumerate(arr):
        for j, v in enumerate(line):
            if v > 9 : 
                to_do.append([i,j])
                answer_p1 += 1
    visited = np.where(arr > 9, 1, 0)
    while to_do:
        x, y = to_do.pop()
        for nx, ny in [[x+1,y+1],[x+1,y],[x+1,y-1],[x,y-1],[x,y+1],[x-1,y-1],[x-1,y],[x-1,y+1]]:
            if 0 <= nx < 10 and 0 <= ny < 10:
                arr[nx][ny] += 1
                if arr[nx][ny] > 9 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    to_do.append([nx,ny])
                    answer_p1 += 1

    masking = arr > 9
    if np.all(masking == True):
        print(answer_p2)
        break
    arr[masking] = 0
    if answer_p2 == 100: 
        print(answer_p1)
        print('-'*30)
