
# Advent of Code 2015 - Day 23 Parts 1 and 2
# 17 May 2023 Brian Green
#
# Problem:
# Day 23: Opening the Turing Lock
# What is the value in register b?
#

# filename = "test23.dat"
filename = "data23.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

print(data_set)

"""
The registers are named a and b, can hold any non-negative integer,
(Part 1) and begin with a value of 0.
(Part 2) and a begin with a value of 1, b = 0.
"""

# a = 0   # Part 1
a = 1   # Part 2
b = 0
program_counter = 0

# Program counter points to current instructon
# Finish whem program counter is outside of list of instructions
while program_counter >= 0 and program_counter < len(data_set):
    print(program_counter)
    instruction = data_set[program_counter].split()
    print(instruction)
    action = instruction[0]
    reg = instruction[1]

    if action == 'hlf':
        # hlf r sets register r to half its current value
        if reg == 'a':
            a = a // 2
        else:
            b = b // 2
        program_counter += 1
    elif action == 'tpl':
        # tpl r sets register r to triple its current value
        if reg == 'a':
            a *= 3
        else:
            b *= 3
        program_counter += 1
    elif action == 'inc':
        # inc r increments register r
        if reg == 'a':
            a += 1
        else:
            b += 1
        program_counter += 1
    elif action == 'jmp':
        # jmp offset is a jump; it continues with the instruction offset away relative to itself.
        program_counter += int(reg)
    elif action == 'jie':
        # jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
        check_reg = a
        if reg.startswith('b'):
            check_reg = b
        if check_reg % 2 == 0:
            program_counter += int(instruction[2])
        else:
            program_counter += 1
    elif action == 'jio':
        # jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
        check_reg = a
        if reg.startswith('b'):
            check_reg = b
        if check_reg == 1:
            program_counter += int(instruction[2])
        else:
            program_counter += 1
    else:
        print(f'Unknown instruction {action}')

print(f"a={a}, b={b}")
