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
        seats_taken = []
        seat_map = [[0] * 8 for _ in range(128)]
        for i in range(128):
            for j in range(7):
                print(seat_map[i][j], end="")
            print("")

        highest_seat = 0
        row = 0
        column = 0
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

            seat_map[row][column] = 1
            seat = row * 8 + column
            print(f"{seat}")
            seats_taken.append(seat)
            if seat > highest_seat:
                highest_seat = seat

            print(f"HIGHEST SEAT = {highest_seat}")

        for i in range(128):
            for j in range(7):
                print(seat_map[i][j], end="")
            print("")

        seats_taken.sort()
        print(seats_taken)

        for i in range(len(seats_taken)):
            if seats_taken[i] + 1 == seats_taken[i+1]:
                pass
            else:
                print(seats_taken[i] + 1)
                break


if __name__ == "__main__":
    solve_it = Aoc04()
    solve_it.run_it()
