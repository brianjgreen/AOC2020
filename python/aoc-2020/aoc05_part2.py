#
# Advent of Code 2020 - Day 5 Part 1
# 5 Dec 2020 Brian Green
#
# Problem:
# What is the ID of your seat?
#
import os


class Aoc05:
    def __init__(self):
        file_name = "data" + os.sep + "brian_aoc05.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        self.data = data_set

    def run_it(self):
        seats_taken = []
        seat_map = [[0] * 8 for _ in range(128)]

        highest_seat = 0
        row = 0
        column = 0
        for i in self.data:
            # Find the row
            low = 0
            high = 127
            for j in range(7):
                if i[j] == 'F':
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
                if i[j] == 'L':
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

            seat_map[row][column] = 1
            seat = row * 8 + column
            print(f"{seat}")
            seats_taken.append(seat)
            if seat > highest_seat:
                highest_seat = seat

            print(f"HIGHEST SEAT = {highest_seat}")

        # Print a map of seats occupied
        for i in range(128):
            for j in range(7):
                print(seat_map[i][j], end="")
            print("")

        seats_taken.sort()
        # print(seats_taken)

        # Look for an empty seat with occupied seats on both sides
        for i in range(len(seats_taken)):
            if seats_taken[i] + 1 != seats_taken[i+1]:
                # The statement above will cause an out of bounds error if we go to the end of the array
                # but we are expecting our seat to be somewhere in the middle
                print(seats_taken[i] + 1)
                break


if __name__ == "__main__":
    solve_it = Aoc05()
    solve_it.run_it()
