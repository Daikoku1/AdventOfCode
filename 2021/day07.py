import os
from collections import Counter, deque
path = os.path.join(os.getcwd(), 'input', 'day07.txt')
with open(path) as f:
    arr = list(map(int, f.readline().split(',')))

# test
# arr = list(map(int, '16,1,2,0,4,2,7,1,2,14'.split(',')))

# Part 1
arr.sort()
# 현재 위치, 필요한 연료량을 각각 t, f 라 할 때,
# t+1 에서 필요한 연료량 == f 
#                           + t+1보다 위치값이 큰 crab 수 * (-1)
#                           + t+1보다 위치값이 작은 crab 수 * (1)
# So... number of |x > t| == number of |x < t| 일 때, t가 최소 연료
# So... 중앙값 사용(use median) 
T = arr[len(arr)//2]
print(sum([abs(x - T) for x in arr]))
print('-'*30)

# Part 2
min_fuel = 1e9
for t in range(arr[0], arr[-1]):
    fuel = 0
    for x in arr:
        d = abs(x-t)
        fuel += d * (d+1) // 2
    if fuel < min_fuel:
        min_fuel = fuel
print(min_fuel)