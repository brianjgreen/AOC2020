# Advent of Code 2018 - Day 2 Part 1
# 19 Oct 2023 Brian Green
#
# Problem:
# What is the checksum?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

num_doubles = 0
num_triples = 0
for box in data_set:
    found_double = False
    found_triple = False
    for id in box:
        count = box.count(id)
        if count == 2:
            found_double = True
        elif count == 3:
            found_triple = True
    if found_double:
        num_doubles += 1
    if found_triple:
        num_triples += 1
print(num_doubles * num_triples)
