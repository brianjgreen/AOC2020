
# Advent of Code 2021 - Day 16 Part 2
# 20 Dec 2021 Brian Green
#
# Problem:
# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?
#

import os

filename = "data" + os.sep + "brian_aoc202116.dat"
with open(filename) as data_file:
    data_set = [pos.strip() for pos in data_file.readlines()]

hex2bin = {'0': [0, 0, 0, 0],
           '1': [0, 0, 0, 1],
           '2': [0, 0, 1, 0],
           '3': [0, 0, 1, 1],
           '4': [0, 1, 0, 0],
           '5': [0, 1, 0, 1],
           '6': [0, 1, 1, 0],
           '7': [0, 1, 1, 1],
           '8': [1, 0, 0, 0],
           '9': [1, 0, 0, 1],
           'A': [1, 0, 1, 0],
           'B': [1, 0, 1, 1],
           'C': [1, 1, 0, 0],
           'D': [1, 1, 0, 1],
           'E': [1, 1, 1, 0],
           'F': [1, 1, 1, 1]
           }

packet_type = {0: "sum",
               1: "product",
               2: "min",
               3: "max",
               4: "literal",
               5: "greater",
               6: "less",
               7: "equal"
               }


testdata = ["C200B40A82",  # finds the sum of 1 and 2, resulting in the value 3.
            # finds the product of 6 and 9, resulting in the value 54.
            "04005AC33890",
            # finds the minimum of 7, 8, and 9, resulting in the value 7.
            "880086C3E88112",
            # finds the maximum of 7, 8, and 9, resulting in the value 9.
            "CE00C43D881120",
            "D8005AC2A8F0",  # produces 1, because 5 is less than 15.
            "F600BC2D8F",  # produces 0, because 5 is not greater than 15.
            "9C005AC2F8F0",  # produces 0, because 5 is not equal to 15.
            "9C0141080250320F1802104A08"]


def hex2bin_list(hex):
    message = []
    for h in hex:
        message += hex2bin[h]
    return message.copy()


def bin2int(bins):
    num = 0
    for i in bins:
        num = num << 1
        num |= i
    return num


def decode_literal(message):
    temp_mess = message.copy()
    total = []
    used_bits = 0
    while temp_mess[0] == 1:
        total += temp_mess[1:5]
        temp_mess = temp_mess[5:]
        used_bits += 5
    total += temp_mess[1:5]
    used_bits += 5
    return total.copy(), used_bits


def decode_message(message):
    # global tot_ver
    # print(message)
    # version = bin2int(message[:3])
    type_of = bin2int(message[3:6])
    # print(f"version: {version}")
    # tot_ver += version
    # print(f"total versions: {tot_ver}")
    print(f"type_of: {packet_type[type_of]}")

    if type_of == 4:
        num, used = decode_literal(message[6:])
        value = bin2int(num)
        # print(bin2int(num))
        # print(used+6)
        return value, used+6

    else:
        len_of_subpackets = 0
        num_of_subpackets = 0
        length = message[6]

        if length == 0:
            len_of_subpackets = bin2int(message[7:22])
            # print(f'length of subpackets in bits: {len_of_subpackets}')
            start_sub = 22
        else:
            num_of_subpackets = bin2int(message[7:18])
            # print(f'number of subpackets: {num_of_subpackets}')
            start_sub = 18
        total_used = start_sub

        packet_values = []
        while len_of_subpackets > 0 or num_of_subpackets > 0:
            # print(f'length of subpackets in bits: {len_of_subpackets}')
            # print(f'number of subpackets: {num_of_subpackets}')
            value, used = decode_message(message[start_sub:])
            packet_values.append(value)
            total_used += used
            len_of_subpackets -= used
            num_of_subpackets -= 1
            start_sub += used

        if type_of == 0:
            total = sum(packet_values)
        elif type_of == 1:
            # Need Python 3.8 for math.prod()
            # Or install numpy package
            total = packet_values[0]
            for i in range(1, len(packet_values)):
                total *= packet_values[i]
        elif type_of == 2:
            total = min(packet_values)
        elif type_of == 3:
            total = max(packet_values)
        elif type_of == 5:
            if packet_values[0] > packet_values[1]:
                total = 1
            else:
                total = 0
        elif type_of == 6:
            if packet_values[0] < packet_values[1]:
                total = 1
            else:
                total = 0
        elif type_of == 7:
            if packet_values[0] == packet_values[1]:
                total = 1
            else:
                total = 0
        else:
            print("WHAT!?!?!")

        return total, total_used


for t in testdata:
    print(t)
    # tot_ver = 0
    total, total_used = decode_message(hex2bin_list(t))
    # print(f"SUPRE TOTAL VER: {tot_ver}")
    print(f"total={total}")
    print('====')

# tot_ver = 0

print(data_set)
total, total_used = decode_message(hex2bin_list(data_set[0]))
print(f"total={total}")
# print(f"SUPRE TOTAL VER: {tot_ver}")
