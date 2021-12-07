import os
from collections import Counter, deque
# path = os.path.join(os.getcwd(), 'input', 'day07.txt')
# with open(path) as f:
#     arr = list(map(int, f.readline().split(',')))

# test
arr = list(map(int, '16,1,2,0,4,2,7,1,2,14'.split(',')))

# Part 1
l, r = [], sorted(arr, reverse = True)
l_sum, r_sum = 0, sum(r)
answer = r_sum - r[-1] * len(r)
t = r[-1]
while True:
    t += 1
    while r and r[-1] < t:
        num = r.pop()
        l.append(num)
        l_sum += num
        r_sum -= num
    temp = r_sum - t * len(r) + t * len(l) - l_sum
    if temp < answer : answer = temp
    else: break
print(answer)
print('-'*30)


# Part2
l, r = [], deque()
l_sum, r_sum = 0, 0
l_total, r_total = 0, 0
cnt = len(arr)
prev_point = 0
for i in arr:
    if i < 0 :
        for j in r
print(sorted(Counter(arr).items()))
for i, v in sorted(Counter(arr).items()):
    print('-'*30)
    for j in range(prev_point, i+1):
        r.append([j, cnt])
        r_sum += cnt * j
        r_total += cnt
    print(r)
    prev_point = i
    cnt -= v

r.popleft()
answer = r_sum - r[0][0] * r_total
t = r[0][0]
while True:
    t += 1
    while r and r[0][0] < t:
        num, cnt = r.popleft()
        l.append([num,cnt])
        l_sum += num * cnt
        r_sum -= num * cnt
        l_total += cnt
        r_total -= cnt
    temp = r_sum - t * r_total + t * l_total - l_sum
    print('-' * 30)
    # print(r_sum, l_sum)
    # print(r_total, l_total)
    print(t, temp)
    if temp < answer : answer = temp
    else: break
print(answer)