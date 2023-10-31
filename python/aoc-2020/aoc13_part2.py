#
# Advent of Code 2020 - Day 13 Part 2
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

    def run_it(self):
        found_it = False
        buses = []
        offets = {}
        wait = 0
        for i in self.data_sched:
            print(i)
            if i == "x":
                pass
            else:
                bus = int(i)
                buses.append(bus)
                offets[bus] = wait
            wait += 1
        print(buses)
        result = 1
        for i in buses:
            result *= i
        print(f"{result:,}")
        print(f"{100000000000000:,}")
        return
        print(offets)

        t = 0
        new_t = 0  # round(100000000000000 / max(buses)) * max(buses)
        big_t = max(buses)
        print(f"big {new_t}")
        big_t_offset = offets[big_t]
        # print(big_t_offset)
        # print(big_t)
        while found_it is False:
            # if new_t % (big_t * 1000000) == 0:
            #     print(f"{new_t:,}")
            new_t += big_t
            t = new_t - big_t_offset
            # print(t)
            found_it = True
            for i in buses:
                my_bus = (t + offets[i]) % i
                # my_bus = t % i
                # print(f"{i} {t % i}")
                if my_bus != 0:
                    # print(f"{my_bus} NOT IT?")
                    found_it = False
                    break
            """
            t += buses[0]
            for i in buses[1:]:

                found_it = True
                # print((t + offets[i]) % i)
                if (t + offets[i]) % i != 0:
                    found_it = False
                    break
            """
        print(f"{t:,}")
        result = 1
        for i in buses:
            print(f"{i} {round(t/i)} R{t % i}")
            result *= i
        print(f"result {result:,}")


if __name__ == "__main__":
    solve_it = Aoc13()
    solve_it.run_it()
