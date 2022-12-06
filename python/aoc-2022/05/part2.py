
# Advent of Code 2022 - Day 5 Part 2
# 5 Dec 2022 Brian Green
#
# Problem:
# Supply Stacks, move multiple crates at once

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
test = {1: ['Z', 'N'],
        2: ['M', 'C', 'D'],
        3: ['P',]}
test_start_pos = 5
test_num_stacks = 3

"""
    [B]             [B] [S]        
    [M]             [P] [L] [B] [J]
    [D]     [R]     [V] [D] [Q] [D]
    [T] [R] [Z]     [H] [H] [G] [C]
    [P] [W] [J] [B] [J] [F] [J] [S]
[N] [S] [Z] [V] [M] [N] [Z] [F] [M]
[W] [Z] [H] [D] [H] [G] [Q] [S] [W]
[B] [L] [Q] [W] [S] [L] [J] [W] [Z]
 1   2   3   4   5   6   7   8   9 
"""
data = {1: ['B', 'W', 'N'],
        2: ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
        3: ['Q', 'H', 'Z', 'W', 'R'],
        4: ['W', 'D', 'V', 'J', 'Z', 'R'],
        5: ['S', 'H', 'M', 'B'],
        6: ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
        7: ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
        8: ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
        9: ['Z', 'W', 'M', 'S', 'C', 'D', 'J']}
data_start_pos = 10
data_num_stacks = 9

# Test
# data_set = data_set[test_start_pos:]
# stacks = test
# num_stacks = test_num_stacks

# Data
data_set = data_set[data_start_pos:]
stacks = data
num_stacks = data_num_stacks

# Sorry for hard coding these stacks.  I did not feel like debugging a parser

for move in data_set:
    steps = move.split()
    print(steps)
    num = int(steps[1])
    old = int(steps[3])
    new = int(steps[5])

    stacks[new] += stacks[old][-num:]
    stacks[old] = stacks[old][:-num]
    
print(stacks)
for pile in range(num_stacks):
    print(stacks[pile + 1][-1], end='')

print()
