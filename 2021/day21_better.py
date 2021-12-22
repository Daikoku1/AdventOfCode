from pathlib import Path
from itertools import product
from collections import Counter, defaultdict
path = Path.cwd() / 'input' / 'day21.txt'
data = open(path).read().strip().split('\n')
p1, p2 = int(data[0].split(':')[1]), int(data[1].split(':')[1])

# # test
# p1, p2 = 4, 8


# Part 1
def solution_p1(p1, p2):
    die_rolled = 0
    # if position == i : point += i
    # but in python index starts at 0
    # so In code we maek position == 10 -> 0 and use scores list to add point
    scores = [10,1,2,3,4,5,6,7,8,9]
    point_p1, point_p2 = 0, 0
    x = 1
    while True:
        # x + (x+1) + (x+2) == 3*(x+1)
        p1 = (3 * (x+1) + p1) % 10
        point_p1 += scores[p1]
        if point_p1 >= 1000 : return point_p2 * (die_rolled * 100 + x+2)
        x += 3

        p2 = (3 * (x+1) + p2) % 10
        point_p2 += scores[p2]
        if point_p2 >= 1000 : return point_p1 * (die_rolled * 100 + x+2)
        x += 3

        if x > 100 :
            x -= 100
            die_rolled += 1

print(solution_p1(p1, p2))
print('-'* 30)


# Part 2
scores = [10,1,2,3,4,5,6,7,8,9]
dic = {}
def solution_p2(p1, p2, point_p1, point_p2):
    if point_p1 >= 21 : return (1,0)
    if point_p2 >= 21 : return (0,1)
    if (p1, p2, point_p1, point_p2) in dic:
        return dic[(p1, p2, point_p1, point_p2)]

    ans = (0, 0)
    for d1 in [1,2,3]:
        for d2 in [1,2,3]:
            for d3 in [1,2,3]:
                np1 = (p1 + d1 + d2 + d3) % 10
                n_point_p1 = point_p1 + scores[np1]

                x1, y1 = solution_p2(p2, np1, point_p2, n_point_p1)
                ans = (ans[0] + y1, ans[1] + x1)    

    dic[(p1, p2, point_p1, point_p2)] = ans
    return ans

print(max(solution_p2(p1, p2, 0, 0)))