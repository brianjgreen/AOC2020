# Advent of Code 2022 - Day 13 Part 1
# 13 Dec 2022 Brian Green
#
# Problem:
# Distress Signal

import json

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

# print(data_set)
index = 1


# If both values are integers, the lower integer should come first.
# If both values are lists, compare the first value of each list, then the second value, and so on.
# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value,
# then retry the comparison.
def in_order(right, left):
    if len(left) == 0 and len(right) > 0:
        return "good"
    if len(right) == 0 and len(left) > 0:
        return "bad"
    if len(left) == 0 and len(right) == 0:
        return "unknown"

    right_element = right.pop(0)
    left_element = left.pop(0)

    print(f"{left_element} {right_element}")
    if type(right_element) == int and type(left_element) == int:
        if right_element < left_element:
            return "bad"
        elif left_element < right_element:
            return "good"
        else:
            return in_order(right, left)
    
    if type(right_element) == int:
        right_element = [right_element, ]
    elif type(left_element) == int:
        left_element = [left_element, ]

    result = in_order(right_element, left_element)
    if result == "good":
        return "good"
    elif result == "bad":
        return "bad"
    else:
        return in_order(right, left)
    

good_vals = []
while len(data_set) > 0:
    left = json.loads(data_set.pop(0))
    right = json.loads(data_set.pop(0))
    if len(data_set) > 0:
        data_set.pop(0)

    if in_order(right, left) == "good":
        good_vals.append(index)
    index += 1

print(good_vals)
print(sum(good_vals))
