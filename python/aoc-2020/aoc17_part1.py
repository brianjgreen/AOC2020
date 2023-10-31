#
# Advent of Code 2020 - Day 17 Part 1
# 17 Dec 2020 Brian Green
#
# Problem:
# Starting with your given initial configuration, simulate six cycles.
# How many cubes are left in the active state after the sixth cycle?
#


class Aoc17:
    def __init__(self):
        self.old_space = []
        self.new_space = []
        self.check_space = []

        data_set = [
            "..#..#..",
            "#.#...#.",
            "..#.....",
            "##....##",
            "#..#.###",
            ".#..#...",
            "###..#..",
            "....#..#",
        ]

        x = y = z = 0
        # space = test_data
        space = data_set

        for row in space:
            x = 0
            for cube in row:
                if cube == "#":
                    self.old_space.append((z, y, x))
                x += 1
            y += 1

    def activate_cubes(self, space, check_sector=True):
        for z, y, x in space:
            cube_on = False
            total = 0
            if (z, y, x) in self.old_space:
                cube_on = True
                total = -1
            for zz in range(z - 1, z + 2):
                for yy in range(y - 1, y + 2):
                    for xx in range(x - 1, x + 2):
                        if (
                            check_sector
                            and (zz, yy, xx) not in self.check_space
                            and (zz, yy, xx) not in self.old_space
                        ):
                            self.check_space.append((zz, yy, xx))
                        if (zz, yy, xx) in self.old_space:
                            total += 1
            if cube_on:
                if total == 2 or total == 3:
                    self.new_space.append((z, y, x))
            else:
                if total == 3:
                    self.new_space.append((z, y, x))

    def run_it(self):
        for i in range(6):
            self.activate_cubes(self.old_space)
            # print(self.new_space)
            # print(self.check_space)
            self.activate_cubes(self.check_space, check_sector=False)
            # print(self.new_space)
            print(len(self.new_space))
            self.old_space = self.new_space.copy()
            self.new_space = []
            self.check_space = []


if __name__ == "__main__":
    solve_it = Aoc17()
    solve_it.run_it()
