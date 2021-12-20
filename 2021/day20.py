from pathlib import Path
from collections import Counter
path = Path.cwd() / 'input' / 'day20.txt'
data = open(path).read().strip()
algorithm, image = data.split('\n\n')
image = image.split('\n')

## Test
# algorithm = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'
# image = '''
# #..#.
# #....
# ##..#
# ..#..
# ..###
# '''
# image = image.strip().split('\n')

def make_padding_image(image, cnt):
    P = cnt + 3
    padding_image = [['0'] * (len(image[0]) + 2*P) for _ in range(P)]
    for line in image:
        temp = ['0'] * P
        for j in line:
            if j == '#' : temp.append('1')
            else: temp.append('0')
        temp.extend(['0'] * P)
        padding_image.append(temp)
    padding_image.extend([['0'] * (len(image[0]) + 2*P) for _ in range(P)])
    return padding_image

    
def image_enhancement(image):
    new = [['0'] * len(image) for _ in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            if i * j == 0 or i == len(image) -1 or j == len(image[0]):
                if image[0][0] == '1': t = algorithm[511]  # 111111111(2) = 511
                else: t = algorithm[0]
            else:
                s = image[i-1][j-1:j+2]
                s += image[i][j-1:j+2]
                s += image[i+1][j-1:j+2]
                t = algorithm[int(''.join(s), 2)]
            if t == '#' : new[i][j] = '1'
            else: new[i][j] = '0'
    return new

# Part 1
image_p1 = make_padding_image(image, 2)
for _ in range(2):
    image_p1 = image_enhancement(image_p1)
print(Counter(sum(image_p1, []))['1'])
print('-'*30)

# Part 2
image_p2 = make_padding_image(image, 50)
for _ in range(50):
    image_p2 = image_enhancement(image_p2)
print(Counter(sum(image_p2, []))['1'])
