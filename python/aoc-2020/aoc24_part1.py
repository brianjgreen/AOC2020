#
# Advent of Code 2020 - Day 24 Part 1
# 24 Dec 2020 Brian Green
#
# Problem:
# Go through the renovation crew's list and determine which tiles they need to flip.
# After all of the instructions have been followed, how many tiles are left with the black side up?
#
import os


class Aoc24:
    def __init__(self):
        file_name = "data" + os.sep + "brian_aoc24_test.dat"
        with open(file_name) as data_file:
            test_data = [x.strip() for x in data_file.readlines()]

        file_name = "data" + os.sep + "brian_aoc24.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        # self.data = test_data
        self.data = data_set

    def run_it(self):
        tiles = {}
        # e, se, sw, w, nw, and ne
        print(self.data)
        for t in self.data:
            print(t)
            max = len(t)
            pos = 0
            x = y = 0
            print(t[pos:pos+2])
            while pos < max:
                if t[pos] == 'e':
                    x += 2
                    pos -= 1
                elif t[pos:pos+2] == 'se':
                    x += 1
                    y -= 1
                elif t[pos:pos+2] == 'sw':
                    x -= 1
                    y -= 1
                elif t[pos] == 'w':
                    x -= 2
                    pos -= 1
                elif t[pos:pos+2] == 'nw':
                    x -= 1
                    y += 1
                elif t[pos:pos+2] == 'ne':
                    x += 1
                    y += 1
                pos += 2
            if (x, y) in tiles and tiles[(x, y)] == 1:
                tiles[(x, y)] = 0
            else:
                tiles[(x, y)] = 1

        print(tiles)
        print(sum(tiles.values()))


if __name__ == "__main__":
    solve_it = Aoc24()
    solve_it.run_it()
