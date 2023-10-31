#
# Advent of Code 2020 - Day 14 Part 2
# 14 Dec 2020 Brian Green
#
# Problem:
# Execute the initialization program using an emulator for a version 2 decoder chip.
# What is the sum of all values left in memory after it completes?
#
import os
import re


class Aoc14:
    def __init__(self):
        file_name = "data" + os.sep + "brian_aoc14.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        self.data = data_set

    def run_it(self):
        mask = 0
        mem = {}
        pattern = re.compile(r"mem\[(\d+)\] = (\d+)")
        for i in self.data:
            if "mask" in i:
                mask = list(i.split(" = ")[1])
                mask.reverse()
            else:
                m = re.match(pattern, i)
                addr, data = m.groups()
                addr = int(addr)
                data = int(data)
                bunch_of_masks = []
                for j in range(len(mask)):
                    bit = mask[j]
                    if bit == "X":
                        bunch_of_masks.append(1 << j)
                    else:
                        addr |= int(bit) << j
                memory_map = [
                    addr,
                ]

                for j in bunch_of_masks:
                    # Check all combinations of mask bits (0 and 1)
                    temp_map = memory_map.copy()
                    for k in memory_map:
                        # flip the mask bit for each memory location in the list and then add those to the list too
                        temp_addr = k & ~(j)
                        temp_map.append(temp_addr)  # floating bit 0
                        temp_map.append(temp_addr | j)  # floating bit 1
                    # remove duplicate entries
                    memory_map = list(set(temp_map.copy()))

                for j in memory_map:
                    mem[j] = data

        print(mem)
        print(sum(mem.values()))


if __name__ == "__main__":
    solve_it = Aoc14()
    solve_it.run_it()
