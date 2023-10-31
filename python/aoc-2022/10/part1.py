# Advent of Code 2022 - Day 10 Part 1
# 10 Dec 2022 Brian Green
#
# Problem:
# Cathode-Ray Tube, signal strength

# filename = "test.dat"
# filename = "test2.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip().split() for num in data_file.readlines()]

# print(data_set)

register_V = 1
execute = {}
program_counter = 1

for instruction in data_set:
    execute[program_counter] = register_V
    program_counter += 1
    if instruction[0] == "addx":
        register_V += int(instruction[1])
        execute[program_counter] = register_V
        program_counter += 1

# print(execute)

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
signal = 0
cycles = [19, 59, 99, 139, 179, 219]
for state in cycles:
    reg = execute[state]
    # print(f"cycle={state} V={reg}")
    signal += reg * (state + 1)
    # print(signal)

print(signal)
