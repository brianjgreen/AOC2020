#
# Advent of Code 2020 - Day 11 Part 2
# 11 Dec 2020 Brian Green
#
# Problem:
# Given the new visibility method and the rule change for occupied seats becoming empty,
# once equilibrium is reached, how many seats end up occupied?
#
import os


class Aoc11:
    def __init__(self):
        self.vectors = ((-1, -1), (-1, 0), (-1, 1),
                        (0, -1), (0, 1),
                        (1, -1), (1, 0), (1, 1))
        self.empty = 'L'
        self.occupied = '#'
        self.floor = '.'
        self.test_data = ["L.LL.LL.LL",
                          "LLLLLLL.LL",
                          "L.L.L..L..",
                          "LLLL.LL.LL",
                          "L.LL.LL.LL",
                          "L.LLLLL.LL",
                          "..L.L.....",
                          "LLLLLLLLLL",
                          "L.LLLLLL.L",
                          "L.LLLLL.LL"]
        file_name = "data" + os.sep + "brian_aoc11.dat"
        with open(file_name) as data_file:
            data_set = [list(x.strip()) for x in data_file.readlines()]

        # self.data = [list(x) for x in self.test_data]
        self.data = data_set

        # Whats tricky is that the seat map is not real time.
        # You must create a new seat map while applying the rules to the old seat map.
        self.cur_set = [row[:] for row in self.data]
        self.new_set = [row[:] for row in self.data]

    # If a seat is empty (L) and there are no occupied seats in view of it, the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats in view of it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    def apply_seat_rules(self):
        num_changed_seats = 0
        max_x = len(self.data)
        max_y = len(self.data[0])
        for x in range(max_x):
            for y in range(max_y):
                occupied_count = 0
                # print(f"x{x} y{y}")
                if self.cur_set[x][y] == self.floor:
                    # print("floor")
                    continue
                for adj_x, adj_y in self.vectors:
                    check_x = (x + adj_x) 
                    check_y = (y + adj_y)
                    # print(f"{check_x} c {check_y}")
                    # *** PART 2 ADDED THIS WHILE LOOP ***
                    while 0 <= check_x < max_x and 0 <= check_y < max_y and self.cur_set[check_x][check_y] == self.floor:
                        check_x += adj_x
                        check_y += adj_y
                    if 0 <= check_x < max_x and 0 <= check_y < max_y and self.cur_set[check_x][check_y] == self.occupied:
                        occupied_count += 1
                # print(f"o{occupied_count}")
                if self.cur_set[x][y] == self.empty and occupied_count == 0:
                    self.new_set[x][y] = self.occupied
                    num_changed_seats += 1
                    # print("e -> o")
                elif self.cur_set[x][y] == self.occupied and occupied_count >= 5:  # *** PART 2 CHANGED THIS TO 5 (from 4) ***
                    self.new_set[x][y] = self.empty
                    num_changed_seats += 1
                    # print("o -> e")
        return num_changed_seats
                
    def print_seat_chart(self, data):
        for x in data:
            print(x)
                    
    def run_it(self):
        seats_changed = 1
        while seats_changed != 0:
            seats_changed = self.apply_seat_rules()
            # self.print_seat_chart(self.new_set)
            self.cur_set = [row[:] for row in self.new_set]
        
        seats_taken = 0
        for x in range(len(self.new_set)):
            for y in range(len(self.new_set[0])):
                if self.new_set[x][y] == self.occupied:
                    seats_taken += 1
        print(f"seats taken: {seats_taken}")


if __name__ == "__main__":
    solve_it = Aoc11()
    solve_it.run_it()
