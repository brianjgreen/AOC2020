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
    def run_program(program):
        acc = 0
        ip = 0
        usage = {}
        while ip not in usage:
            usage[ip] = 0
            instr = program[ip][0]
            if instr == 'acc':
                acc += int(program[ip][1])
                ip += 1
            elif instr == 'nop':
                ip += 1
            elif instr == 'jmp':
                ip += int(program[ip][1])

            if ip >= len(program):
                print("FOUND IT!")
                print(acc)
                sys.exit()

    def run_it(self):
        program = []
        for instr in self.data:
            program.append(instr.split())
        print(program)

        for i in range(len(program)):
            curr = program[i][0]
            if curr == 'nop':
                program[i][0] = 'jmp'
                self.run_program(program)
                program[i][0] = 'nop'
            elif curr == 'jmp':
                program[i][0] = 'nop'
                self.run_program(program)
                program[i][0] = 'jmp'


if __name__ == "__main__":
    solve_it = Aoc01()
    solve_it.run_it()
