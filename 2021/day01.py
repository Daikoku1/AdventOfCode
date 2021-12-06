import os
path = os.path.join(os.getcwd(), 'input', 'day01.txt')
with open(path) as f:
    lines = list(map(int, f.readlines()))

# part1
print(sum([i < j for i, j in zip(lines[:-1], lines[1:])]))
print('-'*30)

# part2
three_sums = [sum(lines[i:i+3]) for i in range(len(lines) - 2)]
print(sum([i < j for i, j in zip(three_sums[:-1], three_sums[1:])]))