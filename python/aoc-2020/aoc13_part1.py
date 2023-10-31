#
# Advent of Code 2020 - Day 13 Part 1
# 13 Dec 2020 Brian Green
#
# Problem:
#
import os


class Aoc13:
    def __init__(self):
        file_name = "data" + os.sep + "brian_aoc13.dat"
        with open(file_name) as data_file:
            data_set_time = int(data_file.readline())
            data_set_sched = data_file.readline().strip().split(",")

        self.data_time = data_set_time
        self.data_sched = data_set_sched
        print(self.data_time)
        print(self.data_sched)

    def run_it(self):
        found_it = False
        ready = False
        time = 0
        buses = []
        for i in self.data_sched:
            print(i)
            if i == "x":
                pass
            else:
                buses.append(int(i))
        print(buses)
        while found_it is False:
            if time >= self.data_time:
                ready = True
            for i in buses:
                if time % i == 0:
                    print(f"{time}: bus {i} departed")
                    if ready:
                        print(f"bus:{i} at:{time} is {(time - self.data_time) * i}")
                        return
            time += 1


if __name__ == "__main__":
    solve_it = Aoc13()
    solve_it.run_it()
