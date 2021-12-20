from itertools import permutations
from collections import defaultdict
from pathlib import Path
path = Path.cwd() / 'input' / 'day19.txt'
data = open(path).read().strip()

scanners = data.split('\n\n')
B = []
for scan in scanners:
    beacons = []
    for line in scan.split('\n'):
        line = line.strip()
        if line.startswith('--'):
            continue
        x,y,z = [int(v) for v in line.split(',')]
        beacons.append((x,y,z))
    B.append(beacons)

# +- x, +- y , +-z in rotataion : 6 * 2 * 2 * 2 = 48
rotate_direc = {i : p for i,p in enumerate(list(permutations([0, 1, 2])))}
def rotate_point(rotate_direc, point, d):
    new_p = [point[0], point[1], point[2]]
    if d%2 == 1 : new_p[0] *= -1  # x facing direction
    if (d//2) % 2 == 1 : new_p[1] *= -1  # y facing direction
    if (d//4)%2==1 : new_p[2] *= -1  # z facing direction

    direc = rotate_direc[d//8]
    new_p = [new_p[direc[0]], new_p[direc[1]], new_p[direc[2]]]  # rotate
    
    return new_p

N = len(B)
FINAL = set(B[0])
P = [None for _ in range(N)]
P[0] = (0,0,0)

GOOD = set([0])
BAD = set([x for x in range(1,N)])

while BAD:
    found = None
    for b in BAD:
        if found : continue
        g_scan = [tuple([p[0]+P[0][0], p[1]+P[0][1], p[2]+P[0][2]]) for p in FINAL] #B[g]]
        g_set = set(g_scan)

        for b_dir in range(48):
            b_scan = [rotate_point(rotate_direc, p, b_dir) for p in B[b]]
            VOTE = defaultdict(int)
            for b1, b2, b3, in b_scan:
                for g1, g2, g3 in g_scan:
                    # assume B[b][bi] and G[g][gi] are the same beacon
                    # find 12 beacons 
                    # b[0] + dx == g[0] -> dx = g[0] - b[0]
                    dx = g1 - b1
                    dy = g2 - b2
                    dz = g3 - b3
                    VOTE[(dx, dy, dz)] += 1

            for (dx,dy,dz), val in VOTE.items():
                if val >= 12:
                    P[b] = (dx, dy, dz)
                    for p in b_scan:
                        FINAL.add(tuple([p[0] + dx, p[1]+dy, p[2]+dz]))
                    found = b

    if found:
        BAD.remove(found)
        GOOD.add(found)
print(len(FINAL))

answer_p2 = 0
for p1 in P:
    for p2 in P:
        dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])
        if dist > answer_p2:
          answer_p2 = dist
print(answer_p2)