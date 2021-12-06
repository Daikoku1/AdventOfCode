import os
with open('2021/input/day01.txt') as f:
    lines = list(map(int, f.readlines()))

# part1
print(sum([i < j for i, j in zip(lines[:-1], lines[1:])]))


# part2
three_sums = [sum(lines[i:i+3]) for i in range(len(lines) - 2)]
print(sum([i < j for i, j in zip(three_sums[:-1], three_sums[1:])]))