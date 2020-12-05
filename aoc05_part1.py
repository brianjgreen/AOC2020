#
# Advent of Code 2020 - Day 5 Part 1
# 5 Dec 2020 Brian Green
#
# Problem:
#
#
import os


class Aoc04:
    def __init__(self):
        # test_data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
        file_name = "data" + os.sep + "brian_aoc05.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = test_data
        self.data = data_set

    def run_it(self):
        row = 0
        column = 0
        highest_seat = 0
        for i in self.data:
            low = 0
            high = 127
            for j in range(7):
                if i[j] == 'F':
                    # print("Front")
                    high -= (high - low + 1) / 2
                else:
                    # print("Back")
                    low += (high - low + 1) / 2
                # print(i[j])
                # print(f"{high} - {low}")
            if high == low:
                row = int(low)
                print(f"ROW {row}")
            else:
                print("ERROR")

            low = 0
            high = 7
            for j in range(7, 10):
                if i[j] == 'L':
                    high -= (high - low + 1) / 2
                else:
                    low += (high - low + 1) / 2
            if high == low:
                column = int(low)
                print(f"COLUMN {column}")
            else:
                print("ERROR")

            seat = row * 8 + column
            print(f"{seat}")
            if seat > highest_seat:
                highest_seat = seat

            print(f"HIGHEST SEAT = {highest_seat}")


if __name__ == "__main__":
    solve_it = Aoc04()
    solve_it.run_it()
