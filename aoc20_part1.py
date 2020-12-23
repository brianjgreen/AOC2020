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

        self.edge = ("top", "bottom", "left", "right")
        # self.data = test_data.split('\n')
        self.data = data_set

    def run_it(self):
        tiles = {}
        num = 0
        new_tile = True
        whole_tile = []
        for i in self.data:
            if "Tile" in i:
                num = int(i[5:9])
                whole_tile = []
            elif i == "":
                tiles[num] = (whole_tile[0], whole_tile[9], "".join(
                    [x[0] for x in whole_tile]), "".join([x[9] for x in whole_tile]))
            else:
                whole_tile.append(i)
        # print(tiles)

        sides = {}
        s_tiles = tiles.copy()
        for k, v in tiles.items():
            sides[k] = []
            for k1, v1 in s_tiles.items():
                if k != k1:
                    # print(f"k{k}")
                    for i, v2 in enumerate(v):
                        for j, v3 in enumerate(v1):
                            if v2 == v3:
                                sides[k].append(
                                    [(k, self.edge[i]), (k1, self.edge[j])])
                            if v2[::-1] == v3:
                                sides[k].append(
                                    [(k, "flip-"+self.edge[i]), (k1, self.edge[j])])

        corners = []
        for k, v in sides.items():
            num_sides = len(v)
            place = "ERROR"
            if num_sides == 4:
                place = "Middle"
            elif num_sides == 3:
                place = "Mid-edge"
            elif num_sides == 2:
                place = "Corner"
                corners.append(k)
            print(f"{k}: {place} {v}")

        print(corners)
        total = 1
        for i in corners:
            print
            total *= i
        print(f"total {total}")


if __name__ == "__main__":
    solve_it = Aoc20()
    solve_it.run_it()
