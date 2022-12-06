
# Advent of Code 2022 - Day 6 Part 2
# 1 Dec 2022 Brian Green
#
# Problem:
# Tuning Trouble, message = 14 chars

from collections import Counter

test1 = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb'] # 7
test2 = ['bvwbjplbgvbhsrlpgdmjqwftvncz'] # 5
test3 = ['nppdvjthqldpwncqszvftbrmjlhg'] # 6
test4 = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'] # 10
test5 = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'] # 11

filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

print(data_set)

found_it = False
pos = 0
first_marker = 0

# data = data_set[0]
data = test1[0]
while not found_it:
    signal = data[pos:pos+14]
    print(signal)
    freq = Counter(signal)
    if len(freq) == len(signal):
        found_it = True
        first_marker = pos + 14
    pos += 1

print(first_marker)
