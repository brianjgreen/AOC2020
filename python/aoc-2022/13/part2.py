# Advent of Code 2022 - Day 13 Part 2
# 13 Dec 2022 Brian Green
#
# Problem:
# Distress Signal, decoder key

import copy
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
        return -1
    if len(right) == 0 and len(left) > 0:
        return 1
    if len(left) == 0 and len(right) == 0:
        return 0

    right_element = right.pop(0)
    left_element = left.pop(0)

    # print(f"{left_element} {right_element}")
    if isinstance(right_element, int) and isinstance(left_element, int):
        if right_element < left_element:
            return 1
        elif left_element < right_element:
            return -1
        else:
            return in_order(right, left)

    if isinstance(right_element, int):
        right_element = [
            right_element,
        ]
    elif isinstance(left_element, int):
        left_element = [
            left_element,
        ]

    result = in_order(right_element, left_element)
    if result == -1:
        return -1
    elif result == 1:
        return 1
    else:
        return in_order(right, left)


packets = []
while len(data_set) > 0:
    packets.append(json.loads(data_set.pop(0)))
    packets.append(json.loads(data_set.pop(0)))
    if len(data_set) > 0:
        data_set.pop(0)

sorted_packets = [[[2]], [[6]]]
for message in packets:
    for index in range(len(sorted_packets)):
        if (
            in_order(
                left=copy.deepcopy(message), right=copy.deepcopy(sorted_packets[index])
            )
            == -1
        ):
            sorted_packets.insert(index, message)
            break
    if message not in sorted_packets:
        sorted_packets.append(message)

print(sorted_packets)
for pack in sorted_packets:
    print(pack)
pos_2 = sorted_packets.index([[2]]) + 1
pos_6 = sorted_packets.index([[6]]) + 1
print(pos_2 * pos_6)
