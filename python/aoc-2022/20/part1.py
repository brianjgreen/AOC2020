# Advent of Code 2022 - Day 20 Part 1
# 20 Dec 2022 Brian Green
#
# Problem:
# Grove Positioning System


class Node:
    def __init__(self, val, seq):
        self.val = val
        self.next_node = None
        self.prev_node = None
        self.seq = seq

        
# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [int(num.strip()) for num in data_file.readlines()]

head = None
tail = None
num_nodes = 0

for val in data_set:
    temp = Node(val, num_nodes)
    num_nodes += 1
    if head is None:
        head = temp
    if tail != None:
        tail.next_node = temp
        temp.prev_node = tail
    tail = temp

head.prev_node = tail
tail.next_node = head
this_node = head
max_nodes = num_nodes

for num_nodes in range(max_nodes):
    while this_node.seq != num_nodes:
        this_node = this_node.next_node

    val = this_node.val
    if val > 0:
        for _ in range(val):
            # L T S R
            left_node = this_node.prev_node
            swap_node = this_node.next_node
            right_node = swap_node.next_node

            left_node.next_node = swap_node
            swap_node.prev_node = left_node
            swap_node.next_node = this_node
            this_node.prev_node = swap_node
            this_node.next_node = right_node
            right_node.prev_node = this_node
    elif val < 0:
        for _ in range(abs(val)):
            # L S T R
            swap_node = this_node.prev_node
            left_node = swap_node.prev_node
            right_node = this_node.next_node

            left_node.next_node = this_node
            right_node.prev_node = swap_node
            this_node.prev_node = left_node
            this_node.next_node = swap_node
            swap_node.next_node = right_node
            swap_node.prev_node = this_node
    else:
        pass

while this_node.val != 0:
    this_node = this_node.next_node

total = 0
for _ in range(1000):
    this_node = this_node.next_node
total += this_node.val
print(this_node.val)
for _ in range(1000):
    this_node = this_node.next_node
total += this_node.val
print(this_node.val)
for _ in range(1000):
    this_node = this_node.next_node
total += this_node.val
print(this_node.val)

print(total)
