#
# Advent of Code 2020 - Day 20 Part 1
# 20 Dec 2020 Brian Green
#
# Problem:
#
#
import os
import re


class Aoc20:
    def __init__(self):
        test_data = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""

        file_name = "data" + os.sep + "brian_aoc20.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        self.data = test_data.split('\n')
        # self.data = data_set

    def run_it(self):
        tiles = {}
        num = 0
        y = 0
        for i in self.data:
            if "Tile" in i:
                num = int(i[5:9])
                print(num)
                tiles[num] = [[0] * 10 for _ in range(10)]
                y = 0
            elif i == "":
                pass
            else:
                x = 0
                for b in i:
                    if b == '#':
                        tiles[num][x][y] = 1
                    x += 1
                y += 1

        sides = {}
        rev_sides = {}
        for k, v in tiles.items():
            a = b = c = d = 0
            e = f = g = h = 0
            for x in range(10):
                if v[0][x] == 1:
                    a |= 1 << x
                if v[0][9-x] == 1:
                    e |= 1 << x
                if v[x][9] == 1:
                    b |= 1 << x
                if v[9-x][9]:
                    f |= 1 << x
                if v[9][9 - x] == 1:
                    c |= 1 << x
                if v[9][x] == 1:
                    g |= 1 << x
                if v[9 - x][0] == 1:
                    d |= 1 << x
                if v[x][0] == 1:
                    h |= 1 << x

            sides[k] = (a, b, c, d)
            rev_sides[k] = (e, f, g, h)
        print(sides)

        conn = {}
        for k, v in sides.items():
            for s in v:
                if s in conn:
                    conn[s].append(k)
                else:
                    conn[s] = [k, ]
        print(conn)
        # print(tiles)

        t_con = {}
        for t in tiles:
            count = 0
            for k, v in conn.items():
                if t in v and len(conn[k]) > 1:
                    count += 1
            t_con[t] = count
        print(t_con)

        for sk, sv in sides.items():
            for rk, rv in rev_sides.items():
                for n in rv:
                    if n in sv:
                        print(f"{n} {sk} {rk}")


if __name__ == "__main__":
    solve_it = Aoc20()
    solve_it.run_it()
