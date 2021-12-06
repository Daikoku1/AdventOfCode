from collections import Counter
with open('2021/input/day03.txt') as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

T = len(lines) // 2

# Part1
def solution1(lines, T):
    gamma = ''
    epsilon = ''
    for i in zip(*map(lambda x : x.strip(), lines)):
        if Counter(i)['0'] > T : 
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)

print(solution1(lines, T))
print('----------------')


# Part2
def solution2(lines, T):
    def check(i, li):
        ones, zeros = [], []
        for l in li:
            if l[i] == '1' : ones.append(l)
            else: zeros.append(l)
        return ones, zeros

    ones, zeros = check(0, lines)
    if len(ones) >= len(zeros):
        oxygen = ones.copy()
        co2 = zeros.copy()
    else:
        oxygen = zeros.copy()
        co2 = ones.copy()
    
    idx = 1
    while len(oxygen) != 1:
        ones, zeros = check(idx, oxygen)
        if len(ones) >= len(zeros) : oxygen = ones.copy()
        else: oxygen = zeros.copy()
        idx += 1
    
    idx = 1
    while len(co2) != 1:
        ones, zeros = check(idx, co2)
        if len(ones) >= len(zeros) : co2 = zeros.copy()
        else: co2 = ones.copy()
        idx += 1

    return int(oxygen[0], 2) * int(co2[0], 2)

print(solution2(lines, T))