#
# Advent of Code 2020 - Day 8 Part 2
# 8 Dec 2020 Brian Green
#
# Problem:
#
#
import os
import sys


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

    @staticmethod
    def run_prog(prog):
        acc = 0
        ip = 0
        usage = {}
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

            if ip >= len(prog):
                print("FOUND IT!")
                print(acc)
                sys.exit()

        return acc

    def run_it(self):
        prog = []
        for instr in self.data:
            prog.append(instr.split())
        print(prog)

        for i in range(len(prog)):
            curr = prog[i][0]
            if curr == 'nop':
                prog[i][0] = 'jmp'
                self.run_prog(prog)
                prog[i][0] = 'nop'
            elif curr == 'jmp':
                prog[i][0] = 'nop'
                self.run_prog(prog)
                prog[i][0] = 'jmp'

        # print(self.run_prog(prog))


if __name__ == "__main__":
    solve_it = Aoc01()
    solve_it.run_it()
