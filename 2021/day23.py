from pathlib import Path
import numpy as np
import re, copy
import sys
sys.setrecursionlimit(10**6)
path = Path.cwd() / 'input' / 'day23.txt'
data = open(path).read().strip().split('\n')

roads = {
    0 : [4,5],
    4 : [0,5],
    5 : [0,1,4,6],
    1 : [5,6],
    6 : [1,2,5,7],
    2 : [6,7],
    7 : [2,3,6,8],
    3 : [7,8],
    8 : [3,7]
}

amphipods = [[] for _ in range(9)]
for idx, species in enumerate(zip(re.findall('\w', data[3]), re.findall('\w', data[2]))):
    amphipods[idx] = list(species)

answer = float('inf')
def solution(amphipods, energy):
    global answer
    if energy > answer : return # to find minimum energy. and this case can't be minimum.

    if amphipods == [['A','A'], ['B','B'], ['C','C'], ['D','D'], [], [], [], [], []]:
        print(answer)
        answer = min(answer, energy)
        return

    to_change = [(i,v) for i, v in enumerate(amphipods) if v != []]
    for k, v in to_change:
        if k not in [5,6,7] and len(v) == 1 : move = 1
        else : move = 0

        move_target = v[-1]
        for x in roads[k]:
            if x in [0,1,2,3] and len(amphipods[x]) == 0: move += 3
            else: move += 2
            new_amphipods = copy.deepcopy(amphipods)
            new_amphipods[x].append(new_amphipods[k].pop())
            solution(new_amphipods, energy + move*10**(abs(ord('A') - ord(move_target))))

print("Answer p1 : ", solution(amphipods, 0))