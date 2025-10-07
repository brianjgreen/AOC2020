# python day07.py ../../data/2015/day07.dat

import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


signals = {}


def get_value(wire):
    if len(signals[wire]) == 1:
        value = signals[wire][0]
        if value.isnumeric():
            return int(value)
        else:
            calc = get_value(value)
            signals[wire] = [
                str(calc),
            ]
            return calc
    elif (
        "OR" in signals[wire]
        or "AND" in signals[wire]
        or "LSHIFT" in signals[wire]
        or "RSHIFT" in signals[wire]
    ):
        sig_a = signals[wire][0]
        oper = signals[wire][1]
        sig_b = signals[wire][2]

        if sig_a.isnumeric():
            sig_a = int(sig_a)
        else:
            sig_a = get_value(sig_a)

        if sig_b.isnumeric():
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
        signals[wire] = [
            str(calc),
        ]
        return calc
    elif "NOT" in signals[wire]:
        sig_a = signals[wire][1]
        if sig_a.isnumeric():
            sig_a = int(sig_a)
        else:
            sig_a = get_value(sig_a)
        calc = ~sig_a
        signals[wire] = [
            str(calc),
        ]
        return calc
    else:
        print("WHAT HAPPENED!")


def part1(data):
    global signals
    signals.clear()
    for instruction in data:
        steps = instruction.strip().split()
        if steps[-1] in signals:
            print(f"MORE THAN ONE INPUT! {steps[-1]}")
        else:
            signals[steps[-1]] = steps[:-2]
        if steps[-2] != "->":
            print("WHAT!!!!!!")

    return get_value("a")


def part2(data, new_b):
    global signals
    signals.clear()
    for instruction in data:
        steps = instruction.strip().split()
        if steps[-1] in signals:
            print(f"MORE THAN ONE INPUT! {steps[-1]}")
        else:
            signals[steps[-1]] = steps[:-2]
        if steps[-2] != "->":
            print("WHAT!!!!!!")

    signals["b"] = [
        str(new_b),
    ]
    return get_value("a")


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

    data = parse_input(input_data)
    print("Day 07 Part 1:", part1(data))
    print("Day 07 Part 2:", part2(data, part1(data)))
