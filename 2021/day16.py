import heapq
from collections import defaultdict, Counter, deque
from pathlib import Path
path = Path.cwd() / 'input' / 'day16.txt'
with open(path) as f:
    arr = f.readline().strip()

binary = bin(int(arr, 16))[2:]
if len(binary) < 4*len(arr):
    binary = '0'*(4*len(arr) - len(binary)) + binary

p1 = 0
def parse(bits, i, indent): # bit, index, packet
    global p1
    version = int(bits[i+0:i+3], 2)
    p1 += version
    type = int(bits[i+3:i+6], 2)

    if type == 4: # lit
        i += 6
        v = 0
        while True:
            v = v*16 + int(bits[i+1:i+5], 2)
            i += 5
            if bits[i-5] == '0':
                return v,i

    else:
        len_id = int(bits[i+6], 2)
        vs = []
        if len_id == 0:
            len_bits = int(bits[i+7:i+7+15], 2)
            #print(f'len_bits={len_bits} {bits[i+7:i+7+15]}')
            start_i = i+7+15
            i = start_i
            while True:
                v, next_i = parse(bits, i, indent+1)
                #print(f'v={v} next_i={next_i}')
                vs.append(v)
                i = next_i
                if next_i - start_i == len_bits:
                    break
        else:
            n_packets = int(bits[i+7:i+7+11], 2)
            #print(f'n_packets={n_packets}')
            i += 7+11
            for t in range(n_packets):
                v, next_i = parse(bits, i, indent+1)
                #print(f'v={v} next_i={next_i}')
                vs.append(v)
                i = next_i
        if type == 0:
            return sum(vs), i
        elif type == 1:
            ans = 1
            for v in vs:
                ans *= v
            return ans, i
        elif type == 2:
            return min(vs), i
        elif type == 3:
            return max(vs), i
        elif type == 5:
            return (1 if vs[0] > vs[1] else 0), i
        elif type == 6:
            return (1 if vs[0] < vs[1] else 0), i
        elif type == 7:
            return (1 if vs[0] == vs[1] else 0), i

value, next_i  = parse(binary, 0, 0)
print(p1)
print(value)