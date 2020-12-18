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
        test_data = [".#.",
                     "..#",
                     "###"]

        data_set = ["..#..#..",
                    "#.#...#.",
                    "..#.....",
                    "##....##",
                    "#..#.###",
                    ".#..#...",
                    "###..#..",
                    "....#..#"]

        self.data = []
        x = y = z = 0
        space = test_data
        # space = data_set

        for row in space:
            x = 0
            for cube in row:
                if cube == '#':
                    self.data.append((z, y, x))
                x += 1
            y += 1

    def activate_cubes(self, space):
        new_space = []
        print(min(space))
        print(max(space))
        min_z, min_y, min_x = min(space)
        max_z, max_y, max_x = max(space)
        for z in range(-9, 10):
            for y in range(-9, 10):
                for x in range(-9, 10):
                    cube_on = False
                    total = 0
                    if (z, y, x) in space:
                        cube_on = True
                        total = -1
                    for zz in range(z-1, z+2):
                        for yy in range(y-1, y+2):
                            for xx in range(x-1, x+2):
                                if (zz, yy, xx) in space:
                                    total += 1
                    if cube_on:
                        if total == 2 or total == 3:
                            new_space.append((z, y, x))
                    else:
                        if total == 3:
                            new_space.append((z, y, x))
        return new_space

    def run_it(self):
        space = self.data
        for _ in range(6):
            space = self.activate_cubes(space)
            print(space)
            print(len(space))
        print(min(space))
        print(max(space))
        min_z, min_y, min_x = min(space)
        max_z, max_y, max_x = max(space)
        num_min_z = num_max_z = num_min_y = num_max_y = num_min_x = num_max_x = 0
        for cube in space:
            if min_z == cube[0]:
                num_min_z += 1
            if max_z == cube[0]:
                num_max_z += 1
            if min_y == cube[1]:
                num_min_y += 1
            if max_y == cube[1]:
                num_max_y += 1
            if min_x == cube[2]:
                num_min_x += 1
            if max_x == cube[2]:
                num_max_x += 1

        print(
            f"{num_min_z} {num_max_z} {num_min_y} {num_max_y} {num_min_x} {num_max_x}")


if __name__ == "__main__":
    solve_it = Aoc17()
    solve_it.run_it()
