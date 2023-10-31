#
# Advent of Code 2020 - Day 5 Part 1
# 5 Dec 2020 Brian Green
#
# Problem:
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
#
import os


class Aoc05:
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
            # Find the row
            low = 0
            high = 127
            for j in range(7):
                if i[j] == "F":
                    # Front
                    high -= (high - low + 1) / 2
                else:
                    # Back
                    low += (high - low + 1) / 2
            if high == low:
                row = int(low)
                print(f"ROW {row}")
            else:
                print("ERROR")

            # Find the column
            low = 0
            high = 7
            for j in range(7, 10):
                if i[j] == "L":
                    # Left
                    high -= (high - low + 1) / 2
                else:
                    # Right
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
    solve_it = Aoc05()
    solve_it.run_it()
