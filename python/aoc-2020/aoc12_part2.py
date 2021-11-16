#
# Advent of Code 2020 - Day 12 Part 2
# 12 Dec 2020 Brian Green
#
# Problem:
# Figure out where the navigation instructions actually lead.
# What is the Manhattan distance between that location and the ship's starting position?
#
import os


class Aoc12:
    def __init__(self):
        self.north = 'N'
        self.south = 'S'
        self.east = 'E'
        self.west = 'W'
        self.left = 'L'
        self.right = 'R'
        self.forward = 'F'
        self.movement = {
            self.north: (0, 1), self.south: (0, -1), self.east: (1, 0), self.west: (-1, 0)
        }
        self.rotate_right = [self.east, self.south, self.west, self.north]
        self.rotate_left = [self.east, self.north, self.west, self.south]
        test_data = ["F10", "N3", "F7", "R90", "F11"]
        file_name = "data" + os.sep + "brian_aoc12.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        #   self.data = test_data
        self.data = data_set

    def run_it(self):
        ship_x = 0
        ship_y = 0
        x = 10
        y = 1
        for i in self.data:
            dir = i[0]
            dist = int(i[1:])

            if dir == self.left:
                for j in range(int(dist/90) % 4):
                    new_x = y * -1
                    new_y = x
                    x = new_x
                    y = new_y
            elif dir == self.right:
                for j in range(int(dist/90) % 4):
                    new_x = y
                    new_y = x * -1
                    x = new_x
                    y = new_y
            elif dir == self.forward:
                ship_x += x * dist
                ship_y += y * dist
            else:
                x_adj, y_adj = self.movement[dir]
                x += x_adj * dist
                y += y_adj * dist
            print(f"way_x:{x} way_y:{y} ship_x:{ship_x} ship_y:{ship_y}")

        print(f"M-Dist={abs(ship_x) + abs(ship_y)}")


if __name__ == "__main__":
    solve_it = Aoc12()
    solve_it.run_it()
