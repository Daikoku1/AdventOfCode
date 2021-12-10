import os
path = os.path.join(os.getcwd(), 'input', 'day10.txt')
with open(path) as f:
    lines = []
    for l in f.readlines():
        lines.append(list(l.strip()))

# # test
# lines = ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '{([(<{}[<>[]}>{[]{[(<()>', '(((({<>}<{<{<>}{[]{[]{}', '[[<[([]))<([[{}[[()]]]', 
#          '[{[{({}]{}}([{[{{{}}([]', '{<[[]]>}<{[{[{[]{()[[[]', '[<(<(<(<{}))><([]([]()', '<{([([[(<>()){}]>(<<{{', '<{([{{}}[<[[[<>{}]]]>[]]']
# lines = [list(l) for l in lines]

# Part 1
def sol_p1(string):
    stack = []
    for c in string:
        if c == ')':
            if stack[-1] == '(': stack.pop()
            else: return 3
        elif c == ']':
            if stack[-1] == '[': stack.pop()
            else: return 57
        elif c == '}':
            if stack[-1] == '{': stack.pop()
            else: return 1197
        elif c == '>':
            if stack[-1] == '<': stack.pop()
            else: return 25137
        else: stack.append(c)
    return stack if stack else 0

answer_p1 = 0
for line in lines:
    num = sol_p1(line)
    if type(num) != list:
        answer_p1 += num
print(answer_p1)
print('-'*30)


# Part 2
def sol_p2(li):
    answer = 0
    while li:
        c = li.pop()
        answer *= 5
        if c == '(': answer += 1
        elif c == '[': answer += 2
        elif c == '{': answer += 3
        elif c == '<': answer += 4
    return answer

answer_p2 = []
for line in lines:
    num = sol_p1(line)
    if type(num) == list:
        answer_p2.append(sol_p2(num))

answer_p2.sort()
print(answer_p2[len(answer_p2)//2])