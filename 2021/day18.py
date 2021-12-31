from pathlib import Path
import copy
path = Path.cwd() / 'input' / 'day18.txt'
data = open(path).read().strip().split('\n')

# # TEST (4140 / 3993)
# data = '''
# [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.strip().split('\n')
def setting_data(da):
    level = -1
    res = []
    for x in da:
        if x == '[' : level += 1
        elif x == ']' : level -= 1
        elif x.isdigit(): res.append((int(x), level))
    return res

def explode(A):
    for i, v in enumerate(A):
        if v[1] >= 4:
            if i > 0 : A[i-1] = (A[i-1][0] + v[0] , A[i-1][1])
            if i + 2 < len(A) : A[i+2] = (A[i+2][0] + A[i+1][0], A[i+2][1])
            A[i] = (0, v[1]-1)
            A[i+1] = None
            
            return list(filter(lambda x: x != None, A)), False
    return A, True

def split(A):
    for i, v in enumerate(A):
        if v[0] > 9 :
            q, r = divmod(v[0], 2)
            return A[:i] + [(q, v[1]+1), (q + r, v[1]+1)] + A[i+1:], False
    return A, True

def addition(A, B):
    C = []
    for a1, a2 in A:
        C.append((a1,a2+1))
    for b1, b2 in B:
        C.append((b1,b2+1))
        
    while True:
        C, end_explode = explode(C)
        if not end_explode : continue
        C, end_split = split(C)
        if not end_split : continue
        break
    return C

def cal_magnitude(A):
    def cal(level, A):
        for i, v in enumerate(A):
            if v[1] == level:
                A[i] = (3*v[0] + 2 * A[i+1][0], level-1)
                A[i+1] = None
                return list(filter(lambda x: x != None, A)), False
        return A, True
    level = 3
    while level > -1 : 
        A, end = cal(level, A)
        if end : level -= 1
    return A[0][0]   

A = setting_data(data[0])
for B in data[1:]:
    B = setting_data(B)
    A = addition(A, B)

print('Answer P1 : ', cal_magnitude(A))
print('-'*30)

answer_p2 = 0
for i, v1 in enumerate(data):
    v1 = setting_data(v1)
    for j, v2 in enumerate(data):
        if i == j : continue
        v2 = setting_data(v2)
        temp = cal_magnitude(addition(v1,v2))        
        answer_p2 = max(temp, answer_p2)

print('Answer P2 :', answer_p2)