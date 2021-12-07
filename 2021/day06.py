import os
from collections import deque
path = os.path.join(os.getcwd(), 'input', 'day06.txt')
with open(path) as f:
    line = list(map(int, f.readline().split(',')))

lanternfish = deque([0] * 9)
for x in line:
    lanternfish[x] += 1

def count_lanternfish(fish, day):
    while day:
        fish.append(fish.popleft())
        fish[6] += fish[-1]
        day -= 1
    return sum(fish)

# Part 1
fish_p1 = lanternfish.copy()
print(count_lanternfish(fish_p1, 80))
print('-'*30)

# Part 2
fish_p2 = lanternfish.copy()
print(count_lanternfish(fish_p2, 256))