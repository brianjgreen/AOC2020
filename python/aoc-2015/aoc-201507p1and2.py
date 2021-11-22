
# Advent of Code 2015 - Day 7 Parts 1 and 2
# 21 Nov 2021 Brian Green
#
# Problem:
# 1. what signal is ultimately provided to wire a?
# 2. What new signal is ultimately provided to wire a?
#

import os
import sys

signals = {}


def get_value(wire):
    print(f"{wire} = {signals[wire]}")
    if len(signals[wire]) == 1:
        value = signals[wire][0]
        if value.isnumeric():
            print(value)
            return int(value)
        else:
            calc = get_value(value)
            signals[wire] = [str(calc), ]
            return calc
    elif 'OR' in signals[wire] or 'AND' in signals[wire] or 'LSHIFT' in signals[wire] or 'RSHIFT' in signals[wire]:
        sig_a = signals[wire][0]
        oper = signals[wire][1]
        sig_b = signals[wire][2]

        if sig_a.isnumeric():
            print(f"sig_a = {sig_a}")
            sig_a = int(sig_a)
        else:
            sig_a = get_value(sig_a)

        if sig_b.isnumeric():
            print(f"sig_b = {sig_b}")
            sig_b = int(sig_b)
        else:
            sig_b = get_value(sig_b)

        if oper == "OR":
            calc = sig_a | sig_b
        elif oper == "AND":
            calc = sig_a & sig_b
        elif oper == "LSHIFT":
            calc = sig_a << sig_b
        elif oper == "RSHIFT":
            calc = sig_a >> sig_b
        else:
            print(signals[wire])
        signals[wire] = [str(calc), ]
        return calc
    elif 'NOT' in signals[wire]:
        sig_a = signals[wire][1]
        if sig_a.isnumeric():
            print(sig_a)
            sig_a = int(sig_a)
        else:
            sig_a = get_value(sig_a)
        calc = ~sig_a
        signals[wire] = [str(calc), ]
        return calc
    else:
        print("WHAT HAPPENED!")


filename = "data" + os.sep + "brian_aoc201507.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

for instruction in data_set:
    steps = instruction.strip().split()
    if steps[-1] in signals:
        print(f'MORE THAN ONE INPUT! {steps[-1]}')
    else:
        signals[steps[-1]] = steps[:-2]
    if steps[-2] != '->':
        print('WHAT!!!!!!')

signal_copy = signals.copy()
part1 = get_value('a')
print(part1)

signals = signal_copy
signals['b'] = [str(part1), ]
part2 = get_value('a')
print(part2)

print(f"part1={part1} part2={part2}")
