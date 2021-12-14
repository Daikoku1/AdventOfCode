from pathlib import Path
from collections import defaultdict
path = Path.cwd() / 'input' / 'day14.txt'
change_dic = {}
with open(path) as f:
    string = f.readline().strip()
    f.readline()
    for line in f.readlines():
        a, b = line.split('->')
        a, b = a.strip(), b.strip()
        change_dic[a] = [a[0]+b, b+a[1]]

# # Test
# string = 'NNCB'
# change_dic = {}
# lines = ['CH -> B','HH -> N','CB -> H','NH -> C','HB -> C','HC -> B','HN -> C','NN -> C','BH -> H','NC -> B','NB -> B','BN -> B','BB -> N','BC -> B','CC -> N','CN -> C']
# for line in lines:
#     a, b = line.split('->')
#     a, b = a.strip(), b.strip()
#     change_dic[a] = [a[0]+b, b + a[1]]

count_dic = defaultdict(int)
for i in range(len(string) - 1):
    count_dic[string[i:i+2]] += 1

def subtract(count_dic):
    answer = defaultdict(int)
    for k, v in count_dic.items():
        answer[k[0]] += v
        answer[k[1]] += v
    answer[string[0]] += 1
    answer[string[-1]] += 1
    values = sorted(answer.values())
    return (values[-1] - values[0]) // 2

for i in range(1, 41):
    new_dic = defaultdict(int)
    for k, v in count_dic.items():
        for n in change_dic[k]: 
            new_dic[n] += v
    count_dic = new_dic
    # Part 1 answer
    if i == 10 :
        print(subtract(count_dic))
        print('-'*30)

# Part 2 answer
print(subtract(count_dic))