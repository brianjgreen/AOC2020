# Advent of Code 2018 - Day 7 Part 1
# 31 Oct 2023 Brian Green
#
# Problem:
# What is the size of the largest area that isn't infinite?
#

import bisect
import collections


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_steps(data_set):
    # Each step has a done flag and a list of preceeding steps
    steps = {}
    for inst in data_set:
        pred = inst[5]  # Preceeding step
        next = inst[36]  # Current step
        if pred not in steps:
            # Add a new step if the preceeding step is not already in the dict
            steps[pred] = {"done": False, "pred": []}
        if next in steps:
            # Update the sorted list of preceeding steps
            bisect.insort(steps[next]["pred"], pred)
        else:
            # Add a new step if the next step is not already in the dict
            steps[next] = {
                "done": False,
                "pred": [
                    pred,
                ],
            }
    return steps


def get_all_steps_alpha(steps):
    return collections.OrderedDict(sorted(steps.items()))  # Place steps in alpha order


def get_steps_in_order(steps, all_steps):
    order = []
    while len(order) < len(steps.keys()):
        for step in all_steps:
            if step not in order and not all_steps[step]["done"]:
                blockers = 0
                for pred in all_steps[step]["pred"]:
                    if not all_steps[pred]["done"]:
                        blockers += 1
                        break  # Not all preceeding steps done, no need to check further
                if blockers == 0:
                    all_steps[step]["done"] = True
                    order.append(step)
                    break  # Need to check for newly unblocked steps in alpha order
    return order


if __name__ == "__main__":
    steps = get_steps(get_data())
    all_steps_alpha = get_all_steps_alpha(steps)
    print("".join(get_steps_in_order(steps, all_steps_alpha)))
