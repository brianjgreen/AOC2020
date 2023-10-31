#
# Advent of Code 2020 - Day 8 Part 1
# 8 Dec 2020 Brian Green
#
# Problem:
# Run your copy of the boot code. Immediately before any instruction is executed a second time,
# what value is in the accumulator?
#
import os


class Aoc08:
    def __init__(self):
        self.test_data = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]
        file_name = "data" + os.sep + "brian_aoc08.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = self.test_data
        self.data = data_set

    def run_it(self):
        program = []
        usage = {}
        for instr in self.data:
            # Split the lines into instruction and data
            program.append(instr.split())
        acc = 0  # accumulator
        ip = 0  # instruction pointer
        while (
            ip not in usage
        ):  # Stop when we attempt to run an instruction a second time
            usage[ip] = 0  # Track the instructions used
            instr = program[ip][0]
            if instr == "acc":
                acc += int(program[ip][1])
                ip += 1
            elif instr == "nop":
                ip += 1
            elif instr == "jmp":
                ip += int(program[ip][1])

        print(acc)


if __name__ == "__main__":
    solve_it = Aoc08()
    solve_it.run_it()
