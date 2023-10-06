
# Advent of Code 2015 - Day 17 Parts 1 and 2
# 2 May 2022 Brian Green
#
# Problem:
#

import itertools

# numbers = [20, 15, 10, 5, 5]
numbers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
# target = 25
target = 150

result = [seq for i in range(len(numbers), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) == target]

# Part 1
print(result)
print(len(result))

# Part 2
fewest = 10
for group in result:
    fewest = min(fewest, len(group))

min_containers = 0
for group in result:
    if len(group) == fewest:
        min_containers += 1

print(fewest)
print(min_containers)
