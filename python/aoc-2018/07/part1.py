
# Advent of Code 2018 - Day 7 Part 1
# 25 Oct 2023 Brian Green
#
# Problem:
# What is the size of the largest area that isn't infinite?
#

import collections

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

# Each step has a done flag and a list of preceeding steps
steps = {}
for inst in data_set:
    pred = inst[5]  # Preceeding step
    next = inst[36] # Current step
    if pred not in steps:
        steps[pred] = {'done': False, 'pred': []}
    if next in steps:
        steps[next]['pred'].append(pred)
        steps[next]['pred'] = sorted(steps[next]['pred'])
    else:
        steps[next] = {'done': False, 'pred': [pred, ]}

all_steps = collections.OrderedDict(sorted(steps.items()))
print(all_steps)
order = []
done = False
# 

def find_done_steps(step):
    if step not in order and not all_steps[step]['done']:
        for pred in all_steps[step]['pred']:
            if not all_steps[pred]['done']:
                return(None)
        all_steps[step]['done'] = True
        return(step)
    else:
        return(None)
            
while len(order) < len(steps.keys()):
    for step in all_steps:
        print(step)
        found = find_done_steps(step)
        if found is not None:
            print(found)
            order.append(found)
            break

    print(order)
print(''.join(order))
