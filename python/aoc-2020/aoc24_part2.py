#
# Advent of Code 2020 - Day 24 Part 2
# 24 Dec 2020 Brian Green
#
# Problem:
# How many tiles will be black after 100 days?
#
import os


class Aoc24:
    def __init__(self):
        self.check_white_tiles = []
        self.art = {}
        self.adj = ((2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1))

        """
        file_name = "data" + os.sep + "brian_aoc24_test.dat"
        with open(file_name) as data_file:
            test_data = [x.strip() for x in data_file.readlines()]
        """

        file_name = "data" + os.sep + "brian_aoc24.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        # self.data = test_data
        self.data = data_set

    def count_black_tiles(self, tiles, t, tab_white=False):
        black = 0
        x, y = t
        for off_x, off_y in self.adj:
            hex = (x + off_x, y + off_y)
            if hex in tiles and tiles[hex] == 1:
                black += 1
            elif tab_white and hex not in self.check_white_tiles:
                self.check_white_tiles.append(hex)
        return black

    # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    def flip_to_white(self, tiles):
        self.check_white_tiles = []
        self.art = tiles.copy()
        for t in tiles:
            if tiles[t] == 1:
                black = self.count_black_tiles(tiles, t, tab_white=True)
                if black == 0 or black > 2:
                    self.art[t] = 0
            elif t not in self.check_white_tiles:
                self.check_white_tiles.append(t)

    # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    def flip_to_black(self, tiles):
        for t in self.check_white_tiles:
            if t not in tiles or tiles[t] == 0:
                black = self.count_black_tiles(tiles, t)
                if black == 2:
                    self.art[t] = 1

    def run_it(self):
        tiles = {}
        # e, se, sw, w, nw, and ne
        print(self.data)
        for t in self.data:
            print(t)
            max = len(t)
            pos = 0
            x = y = 0
            print(t[pos : pos + 2])
            while pos < max:
                if t[pos] == "e":
                    x += 2
                    pos -= 1
                elif t[pos : pos + 2] == "se":
                    x += 1
                    y -= 1
                elif t[pos : pos + 2] == "sw":
                    x -= 1
                    y -= 1
                elif t[pos] == "w":
                    x -= 2
                    pos -= 1
                elif t[pos : pos + 2] == "nw":
                    x -= 1
                    y += 1
                elif t[pos : pos + 2] == "ne":
                    x += 1
                    y += 1
                pos += 2
            if (x, y) in tiles and tiles[(x, y)] == 1:
                tiles[(x, y)] = 0
            else:
                tiles[(x, y)] = 1

        print(tiles)
        print(sum(tiles.values()))

        for i in range(100):
            self.flip_to_white(tiles)
            print(len(self.check_white_tiles))
            self.flip_to_black(tiles)
            print(f"Day {i+1}: {sum(self.art.values())}")
            tiles = self.art


if __name__ == "__main__":
    solve_it = Aoc24()
    solve_it.run_it()
