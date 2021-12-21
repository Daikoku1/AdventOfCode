from pathlib import Path
from itertools import product
from collections import Counter, defaultdict
path = Path.cwd() / 'input' / 'day21.txt'
data = open(path).read().strip().split('\n')
print(data)
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
quantum_die = Counter(list(map(sum, product([1,2,3], repeat = 3)))).items()
def solution_p2(p1, p2):
    scores = [10,1,2,3,4,5,6,7,8,9]
    p1_wins, p2_wins = 0, 0
    universe_points = defaultdict(int)
    universe_points[(p1, p2, 0, 0)] = 1 # p1, p2, point_p1, point_p2
    while True:
        new_universe = defaultdict(int)
        for (x1, x2, point_p1, point_p2), num in universe_points.items():
            for v1, c1 in quantum_die: # make universe
                nx1 = (x1 + v1) % 10 
                n_point_p1 = scores[nx1] + point_p1
                if n_point_p1 >= 21 :
                    p1_wins += c1 * num
                else:
                    for v2, c2 in quantum_die: # make universe
                        nx2 = (x2 + v2) % 10
                        n_point_p2 = scores[nx2] + point_p2
                        if n_point_p2 >= 21 : 
                            p2_wins += c1 * c2 * num
                        else: 
                            new_universe[(nx1, nx2, n_point_p1, n_point_p2)] += c1 * c2 * num

        if not new_universe : break
        universe_points = new_universe.copy()
    return max(p1_wins, p2_wins)
    
print(solution_p2(p1, p2))