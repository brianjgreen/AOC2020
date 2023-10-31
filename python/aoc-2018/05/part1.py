# Advent of Code 2018 - Day 5 Part 1
# 20 Oct 2023 Brian Green
#
# Problem:
# How many units remain after fully reacting the polymer you scanned?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

smallest = False
data_set = data_set[0]
while not smallest:
    smallest = True
    ptr = 0
    new_str = ""
    while ptr < len(data_set) - 1:
        curr = data_set[ptr]
        next = data_set[ptr + 1]
        if curr.lower() == next.lower() and curr != next:
            smallest = False
            ptr += 2
        else:
            ptr += 1
            new_str += curr
    data_set = new_str + next

print(len(data_set))
