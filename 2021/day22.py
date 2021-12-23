from pathlib import Path
import numpy as np
path = Path.cwd() / 'input' / 'day22.txt'

def get_orders(path):
    res = []
    for d in open(path).read().strip().split('\n'):
        cmd, points = d.split(' ')
        cmd = cmd.strip()
        points = points.split(',')
        x1, x2 = map(int, points[0].split('=')[1].split('..'))
        y1, y2 = map(int, points[1].split('=')[1].split('..'))
        z1, z2 = map(int, points[2].split('=')[1].split('..'))
        res.append(((cmd == 'on'), x1, x2, y1, y2, z1, z2))
    return res

orders = get_orders(path)
cubes = np.zeros((101, 101, 101), dtype = 'int8') # limit == -50 ~ 50
# to change range (-50 ~ 50) -> (0, 101)
def change_axis(num, min_n, max_n): 
    return max(min(num, max_n), min_n)

for on, x1, x2, y1, y2, z1, z2 in orders:
    x1, y1, z1 = map(lambda x : change_axis(x+50, 0, 101), (x1,y1,z1))
    x2, y2, z2 = map(lambda x : change_axis(x+51, 0, 101), (x2,y2,z2))
    cubes[x1:x2, y1:y2, z1:z2] = 1 if on else 0

print("Answer 1:", np.sum(cubes))
print('-'*30)

# test_answer2 == 2_758_514_936_282_235
# if make np.array memory will be lack.

# I'll make set of cubes("Cubes") which takes 6 end point (min_x, max_x, min_y, max_y, min_z, max_z)
# if 2 cube is overlabed / overlabed cubes stored other set("Overlapped")
# So. we can calculate area of cubes by
# area of "Cubes" - area of "Overlapped"

class Cube:
    def __init__(self, x1,x2,y1,y2,z1,z2):
        self.size = ((x1,x2), (y1,y2), (z1,z2))
        self.overlapped = []

    def find_overlap(self, x1,x2,y1,y2,z1,z2):
        s0, s1 = self.size[0]
        nx1, nx2 = max(x1, s0), min(x2, s1)
        ox1, ox2 = (nx1, nx2) if nx1 < nx2 else (0, 0)

        s0, s1 = self.size[1]
        ny1, ny2 = max(y1, s0), min(y2, s1)
        oy1, oy2 = (ny1, ny2) if ny1 < ny2 else (0, 0)
        
        s0, s1 = self.size[2]
        nz1, nz2 = max(z1, s0), min(z2, s1)
        oz1, oz2 = (nz1, nz2) if nz1 < nz2 else (0, 0)

        return ox1, ox2, oy1, oy2, oz1, oz2

    def subtract(self, x1,x2,y1,y2,z1,z2):
        x1, x2, y1, y2, z1, z2 = self.find_overlap(x1, x2, y1, y2, z1, z2)
        if x1 == x2 or y1 == y2 or z1 == z2 : return

        cube = Cube(x1,x2,y1,y2,z1,z2)
        for inner in self.overlapped:
            inner.subtract(x1,x2,y1,y2,z1,z2)
        self.overlapped.append(cube)

    def cal_volume(self): 
        area = 1
        for (l, r) in self.size:
            area *= (r-l)
        return area - sum([cube.cal_volume() for cube in self.overlapped])

def solve(orders):
    cubes = []
    for (on, x1, x2, y1, y2, z1, z2) in orders:
        x2, y2, z2 = x2 + 1, y2 + 1, z2 + 1

        for another in cubes:
            another.subtract(x1, x2, y1, y2, z1, z2)  # remove cube from all other cubes

        if on:  # on --> read the cube volume
            cubes.append(Cube(x1, x2, y1, y2, z1, z2))

    return sum(cube.cal_volume() for cube in cubes)

print("Answer 2:", solve(orders))