# Advent of Code 2015 - Day 23 Parts 1 and 2
# 17 May 2023 Brian Green
#
# Problem:
# Day 24: It Hangs in the Balance
# What is the quantum entanglement of the first group of packages in the ideal configuration?
#

import itertools
import math

# filename = "test24.dat"
filename = "data24.dat"
with open(filename) as data_file:
    data_set = [int(num.strip()) for num in data_file.readlines()]

print(data_set)
# num_groups = 3    # part 1
num_groups = 4  # part 2
target = sum(data_set) // num_groups
print(target)

# Try all combinations of number groupings of that equal 1/3 (or 1/4) of the sum of all numbers
result = [
    seq
    for i in range(len(data_set), 0, -1)
    for seq in itertools.combinations(data_set, i)
    if sum(seq) == target
]

print(result)

smallest = 1000000  # smallest quantum value
fewest = len(data_set)  # group with the fewest numbers

for group in result:
    number = len(group)
    quantum = math.prod(group)
    if number < fewest:
        # Group with the fewest members, so far
        fewest = number
        smallest = quantum
        print(f"{group} {quantum}")
    if number == fewest and quantum < smallest:
        # Smallest quantum number amoung the groups with the fewest numbers
        smallest = quantum

print(smallest)
