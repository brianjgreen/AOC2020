#
# Advent of Code 2020 - Day 14 Part 1
# 14 Dec 2020 Brian Green
#
# Problem:
#
import os
import re


class Aoc14:
    def __init__(self):
        test_data = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
                     "mem[8] = 11",
                     "mem[7] = 101",
                     "mem[8] = 0"]

        file_name = "data" + os.sep + "brian_aoc14.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        # self.data = test_data
        self.data = data_set

    def run_it(self):
        mask = 0
        mem = {}
        pattern = re.compile(r"mem\[(\d+)\] = (\d+)")
        for i in self.data:
            if 'mask' in i:
                mask = list(i.split(" = ")[1])
                mask.reverse()
                # print(mask)
            else:
                m = re.match(pattern, i)
                # print(m.groups())
                addr, data = m.groups()
                addr = int(addr)
                data = int(data)
                # print(f"{addr}: {data}")
                value = 0
                for j in range(len(mask)):
                    bit = mask[j]
                    # print(bit)
                    if bit == 'X':
                        value |= data & (1 << j)
                        # print(f"X {data & (1 << j)}")
                    else:
                        value |= int(bit) << j
                        # print(f"{int(bit) << j}")
                    # print(f"val:{value}")
                mem[addr] = value

        print(mem)
        print(sum(mem.values()))


if __name__ == "__main__":
    solve_it = Aoc14()
    solve_it.run_it()
