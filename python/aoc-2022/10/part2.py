# Advent of Code 2022 - Day 10 Part 2
# 10 Dec 2022 Brian Green
#
# Problem:
# Cathode-Ray Tube, sprite

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

print("#", end="")
for cycle, val in execute.items():
    h_sync = cycle % 40
    if h_sync >= val - 1 and h_sync <= val + 1:
        print("#", end="")
    else:
        print(".", end="")
    if h_sync == 39:
        print()
