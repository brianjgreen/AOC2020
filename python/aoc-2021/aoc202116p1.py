
# Advent of Code 2021 - Day 16 Part 1
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

testdata = ["D2FE28",
            "38006F45291200",
            "EE00D40C823060",
            "8A004A801A8002F478",
            "620080001611562C8802118E34",
            "C0015000016115A2E0802F182340",
            "A0016C880162017C3686B18A3D4780"]

# data_set = testdata

"""
message = []
for hex in data_set:
    message += hex2bin[hex]
"""


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
    global tot_ver
    print(message)
    version = bin2int(message[:3])
    type_of = bin2int(message[3:6])
    print(f"version: {version}")
    tot_ver += version
    print(f"total versions: {tot_ver}")
    print(f"type_of: {type_of}")

    if type_of == 4:
        num, used = decode_literal(message[6:])
        print(bin2int(num))
        # print(used+6)
        return(used+6)

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
        while len_of_subpackets > 0 or num_of_subpackets > 0:
            print(f'length of subpackets in bits: {len_of_subpackets}')
            print(f'number of subpackets: {num_of_subpackets}')
            used = decode_message(message[start_sub:])
            total_used += used
            len_of_subpackets -= used
            num_of_subpackets -= 1
            start_sub += used

        return total_used


for t in testdata:
    print(t)
    tot_ver = 0
    decode_message(hex2bin_list(t))
    print(f"SUPRE TOTAL VER: {tot_ver}")
    print('====')

tot_ver = 0
print(data_set)
decode_message(hex2bin_list(data_set[0]))
print(f"SUPRE TOTAL VER: {tot_ver}")
