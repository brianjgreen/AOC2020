#
# Advent of Code 2020 - Day 8 Part 1
# 8 Dec 2020 Brian Green
#
# Problem:
#
#
import os


class Aoc01:
    def __init__(self):
        self.test_data = ["nop +0",
                          "acc +1",
                          "jmp +4",
                          "acc +3",
                          "jmp -3",
                          "acc -99",
                          "acc +1",
                          "jmp -4",
                          "acc +6"]
        file_name = "data" + os.sep + "brian_aoc08.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = self.test_data
        self.data = data_set

    def run_it(self):
        prog = []
        usage = {}
        for instr in self.data:
            prog.append(instr.split())
        print(prog)
        acc = 0
        ip = 0
        while ip not in usage:
            usage[ip] = 0
            instr = prog[ip][0]
            if instr == 'acc':
                acc += int(prog[ip][1])
                ip += 1
            elif instr == 'nop':
                ip += 1
            elif instr == 'jmp':
                ip += int(prog[ip][1])

        print(acc)


if __name__ == "__main__":
    solve_it = Aoc01()
    solve_it.run_it()
