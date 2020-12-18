from __future__ import print_function

inp = """.#.
..#
###"""

inp = """...#...#
#######.
....###.
.#..#...
#.#.....
.##.....
#.####..
#....##."""

from collections import defaultdict

cubes = defaultdict(lambda : '.')

lines = inp.split('\n')
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        cubes[(i - 1, j - 1, 0, 0)] = c

xmin = min(cubes.keys(), key = lambda k: k[0])[0]
xmax = max(cubes.keys(), key = lambda k: k[0])[0]
ymin = min(cubes.keys(), key = lambda k: k[1])[1]
ymax = max(cubes.keys(), key = lambda k: k[1])[1]
zmin = min(cubes.keys(), key = lambda k: k[2])[2]
zmax = max(cubes.keys(), key = lambda k: k[2])[2]
umin = min(cubes.keys(), key = lambda k: k[3])[3]
umax = max(cubes.keys(), key = lambda k: k[3])[3]

for i in range(xmin, xmax+1):
    for j in range(ymin, ymax+1):
        print(cubes[(i, j, 0, 0)], end = '')
    print()

def count(cc, x, y, z, u):
    cnt = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    if cc[(x + i,y + j,z + k,u + l)] == '#':
                        cnt += 1
    return cnt

for i in range(6):
    print(i)
    ncubes = defaultdict(lambda : '.')
    for k in cubes:
        ncubes[k] = cubes[k]

    xmin = min(cubes.keys(), key = lambda k: k[0])[0]
    xmax = max(cubes.keys(), key = lambda k: k[0])[0]
    ymin = min(cubes.keys(), key = lambda k: k[1])[1]
    ymax = max(cubes.keys(), key = lambda k: k[1])[1]
    zmin = min(cubes.keys(), key = lambda k: k[2])[2]
    zmax = max(cubes.keys(), key = lambda k: k[2])[2]
    umin = min(cubes.keys(), key = lambda k: k[3])[3]
    umax = max(cubes.keys(), key = lambda k: k[3])[3]
    # print(xmin, xmax, ymin, ymax, zmin, zmax)
    for z in range(zmin - 1, zmax + 2):
        for u in range(umin - 1, umax + 2): 
            for x in range(xmin - 1, xmax + 2):
                for y in range(ymin - 1, ymax + 2): 
                    cnt = count(cubes, x, y, z, u)
                    k = (x, y, z, u)
                    if cubes[k] == '#':
                        if cnt == 2 or cnt == 3:
                            pass
                        else:
                            ncubes[k] = '.'
                    if cubes[k] == '.':
                        if cnt == 3:
                            ncubes[k] = '#'
    cubes = ncubes

    # xmin = min(cubes.keys(), key = lambda k: k[0])[0]
    # xmax = max(cubes.keys(), key = lambda k: k[0])[0]
    # ymin = min(cubes.keys(), key = lambda k: k[1])[1]
    # ymax = max(cubes.keys(), key = lambda k: k[1])[1]
    # zmin = min(cubes.keys(), key = lambda k: k[2])[2]
    # zmax = max(cubes.keys(), key = lambda k: k[2])[2]
    # umin = min(cubes.keys(), key = lambda k: k[3])[3]
    # umax = max(cubes.keys(), key = lambda k: k[3])[3]
    # print(xmin, xmax, ymin, ymax, zmin, zmax)
    # for z in range(zmin, zmax + 1):
    #     print("z = %d" % z )
    #     for x in range(xmin, xmax + 1):
    #         for y in range(ymin, ymax + 1): 
    #             print(cubes[(x,y,z)], end='')
    #         print()
    #     print()

cnt = 0
for k in cubes:
    if cubes[k] == '#':
        cnt += 1
print(cnt)