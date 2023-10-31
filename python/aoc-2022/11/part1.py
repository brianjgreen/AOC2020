# Advent of Code 2022 - Day 11 Part 1
# 11 Dec 2022 Brian Green
#
# Problem:
# Monkey in the Middle

import json

monkies = {
    0: {
        "items": [79, 98],
        "op": "multi",
        "param": 19,
        "test": 23,
        "true": 2,
        "false": 3,
        "inspect": 0,
    },
    1: {
        "items": [54, 65, 75, 74],
        "op": "add",
        "param": 6,
        "test": 19,
        "true": 2,
        "false": 0,
        "inspect": 0,
    },
    2: {
        "items": [79, 60, 97],
        "op": "squared",
        "param": None,
        "test": 13,
        "true": 1,
        "false": 3,
        "inspect": 0,
    },
    3: {
        "items": [
            74,
        ],
        "op": "add",
        "param": 3,
        "test": 17,
        "true": 0,
        "false": 1,
        "inspect": 0,
    },
}

filename = "test.json"
with open("test.dat.json", "w") as data_file:
    json.dump(monkies, data_file, indent=4)

print(monkies)

# Data Monkeys
# monkies = json.loads("data.json")

print(monkies)

for monkey_round in range(20):
    for monkey in monkies:
        items = monkies[monkey]["items"]
        num_items = len(items)
        print(items)
        print(num_items)
        if num_items == 0:
            continue

        monkies[monkey]["inspect"] += len(items)
        for worry in range(num_items):
            new_item = monkies[monkey]["items"].pop(0)
            print(new_item)
            operation = monkies[monkey]["op"]
            param = monkies[monkey]["param"]
            if operation == "multi":
                new_item *= param
            elif operation == "add":
                new_item += param
            elif operation == "squared":
                new_item *= new_item
            else:
                print(f"UNKNOWN OPERATION {operation}")

            new_item //= 3

            which_monkey = None
            if new_item % monkies[monkey]["test"] == 0:
                which_monkey = "true"
            else:
                which_monkey = "false"
            monkies[monkies[monkey][which_monkey]]["items"].append(new_item)

print(monkies)

inspections = []
for m in monkies:
    inspections.append(monkies[m]["inspect"])

inspections = sorted(inspections, reverse=True)
print(inspections)
print(inspections[0] * inspections[1])
