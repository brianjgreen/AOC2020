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
        # test_data_sched = "7,13,x,x,59,x,31,19".split(',')  # 1068781
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
        ready = False
        time = 0
        buses = []
        offets = {}
        wait = 0
        first_bus = int(self.data_sched[0])
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
        
        current_state = {}
        for i in buses:
            current_state[i] = -1
        print(current_state)        
        t = 0
        while found_it is False:
            for i in buses:
                if time % i == 0:
                    current_state[i] = time
                    # print(f"{time}: bus {i} departed {current_state}")

                    found_it = True
                    t = current_state[first_bus]
                    old_t = t - buses[0]
                    for j in buses[1:]:
                        # print(f"{j} {current_state[j] - t}")
                        if current_state[j] - t != offets[j]:
                            found_it = False
                            break
                    if found_it:
                        print(f"time={current_state[first_bus]}")
                    else:
                        found_it = True
                        for j in buses[1:]:
                            # print(f"{j} {current_state[j] - old_t}")
                            if current_state[j] - old_t != offets[j]:
                                found_it = False
                                break
                        if found_it:
                            print(f"time={current_state[first_bus] - buses[0]}")
            time += 1
            if time % 1000000 == 0:
                print(f"{time:,}")

if __name__ == "__main__":
    solve_it = Aoc13()
    solve_it.run_it()
