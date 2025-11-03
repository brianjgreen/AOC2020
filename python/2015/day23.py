# python day23.py ../../data/2015/day23.dat

import sys

def parse_input(input_data):
    instructions = input_data.strip().split("\n")
    return instructions

def execute_instructions(instructions, a):
    b = 0
    ip = 0
    while ip < len(instructions):
        instr = instructions[ip]
        if instr.startswith("hlf"):
            if instr[4] == 'a':
                a //= 2
            else:
                b //= 2
            ip += 1
        elif instr.startswith("tpl"):
            if instr[4] == 'a':
                a *= 3
            else:
                b *= 3
            ip += 1
        elif instr.startswith("inc"):
            if instr[4] == 'a':
                a += 1
            else:
                b += 1
            ip += 1
        elif instr.startswith("jmp"):
            offset = int(instr[4:])
            ip += offset
        elif instr.startswith("jie"):
            reg = instr[4]
            offset = int(instr[7:])
            if (reg == 'a' and a % 2 == 0) or (reg == 'b' and b % 2 == 0):
                ip += offset
            else:
                ip += 1
        elif instr.startswith("jio"):
            reg = instr[4]
            offset = int(instr[7:])
            if (reg == 'a' and a == 1) or (reg == 'b' and b == 1):
                ip += offset
            else:
                ip += 1
    return b

def part1(instructions):
    return execute_instructions(instructions, 0)

def part2(instructions):
    return execute_instructions(instructions, 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = ""
    input_data = parse_input(input_data)
    print("Day 23 Part 1:", part1(input_data))
    print("Day 23 Part 2:", part2(input_data))
