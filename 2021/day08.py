import os
from collections import Counter, deque
path = os.path.join(os.getcwd(), 'input', 'day08.txt')
with open(path) as f:
    lines = []
    for line in f.readlines():
        temp = []
        for l in line.split("|"):
            # print(l)
            temp.append(l.strip())
        lines.append(temp)
        print(lines[-1])


# Part 1
answer_p1 = 0
for input, output in lines:
    for x in output.split():
        if len(x) in [2,3,4,7]: answer_p1 += 1
print(answer_p1)
print('-'*30)

# Part 2
def change_to_arr(x):
    num = [0] * 7
    for i in x:
        num[ord(i) - ord('a')] = 1
    return num
def union(x, y):
    temp = []
    for a, b in zip(x,y):
        if a == 1 or b == 1: temp.append(1)
        else: temp.append(0)
    return temp
def minus(x, y):
    temp = []
    for a, b in zip(x,y):
        if a == b: temp.append(0)
        else: temp.append(1)
    return temp

def solution(input, output):
    A, C, F, CF, ACF, BCDF, ABCDEFG = '', '', '', '', '', '', ''
    input = input.split()
    output = output.split()
    five, six = [], []
    for x in input:  
        if len(x) == 2 : CF = change_to_arr(x)
        elif len(x) == 3 : ACF = change_to_arr(x)
        elif len(x) == 4 : BCDF = change_to_arr(x)
        elif len(x) == 5 : five.append(change_to_arr(x))
        elif len(x) == 6 : six.append(change_to_arr(x))
        elif len(x) == 7 : ABCDEFG = change_to_arr(x)
    A = minus(CF, ACF)
    BD = minus(BCDF, CF)
    for i in six:
        # CF + C = CF // CF + E = CEF // CF + D = CDF
        if sum(union(minus(ABCDEFG, i), CF)) == 2 : C = minus(ABCDEFG, i)
    F = minus(CF, C)

    answer = ''
    for x in output:
        if len(x) == 6:
            x = minus(ABCDEFG, change_to_arr(x))
            if x == C : answer += '6'   # ABCDEFG - 6(ABDEFG) : C
            elif sum(union(x, BD)) == 2 : answer += '0'   # ABCDEFG - 0(ABCEFG) : D
            else: answer += '9'   # ABCDEFG - 9(ABCDFG) : E
        elif len(x) == 5:
            x = change_to_arr(x)
            if sum(union(F, x)) == 5:   # 5(ABDFG) + F : ABDFG // # 3(ACDFG) + F : ACDFG
                if sum(union(C, x)) == 5 : answer += '3'   # 3(ACDFG) + C : ACDFG  
                else : answer += '5'   # 5(ABDFG) + C : ABCDFG
            else: answer += '2'   # 2(ACDEG) + F : ACDEFG
        elif len(x) == 2 : answer += '1'
        elif len(x) == 3 : answer += '7'
        elif len(x) == 4 : answer += '4'
        else: answer += '8'
    return int(answer)

answer_p2 = 0
for i, o in lines:
    num = solution(i, o)
    answer_p2 += num
print(answer_p2)