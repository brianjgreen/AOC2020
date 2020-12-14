#
# Advent of Code 2020 - Day 13 Part 2
# 13 Dec 2020 Brian Green
#
# Problem:
# 
import os


class Aoc13:
    def __init__(self):
        test_data_time = int("939")
        test_data_sched = "7,13,x,x,59,x,31,19".split(',')  # 1068781
        # test_data_sched = "17,x,13,19".split(',')  # 3417
        # test_data_sched = "67,7,59,61".strip().split(',')  # 754018
        # test_data_sched = "67,x,7,59,61".strip().split(',')  # 779210
        # test_data_sched = "67,7,x,59,61".strip().split(',')  # 1261476
        # test_data_sched = "1789,37,47,1889".strip().split(',')  # 1202161486

        file_name = "data" + os.sep + "brian_aoc13.dat"
        with open(file_name) as data_file:
            data_set_time = int(data_file.readline())
            data_set_sched = data_file.readline().strip().split(',')

        self.data_time = test_data_time
        self.data_sched = test_data_sched
        # self.data_time = data_set_time
        # self.data_sched = data_set_sched

    def run_it(self):
        found_it = False
        buses = []
        offets = {}
        wait = 0
        for i in self.data_sched:
            print(i)
            if i == 'x':
                pass
            else:
                bus = int(i)
                buses.append(bus)
                offets[bus] = wait
            wait += 1
        print(buses)
        print(offets)
        
        t = 0
        while found_it is False:
            t += buses[0]
            for i in buses[1:]:

                found_it = True
                # print((t + offets[i]) % i)
                if (t + offets[i]) % i != 0:
                    found_it = False
                    break
        print(t)
        for i in buses:
            print(f"{i} {(t + offets[i])/i}")
            

if __name__ == "__main__":
    solve_it = Aoc13()
    solve_it.run_it()
