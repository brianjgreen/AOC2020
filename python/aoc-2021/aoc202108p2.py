
# Advent of Code 2021 - Day 8 Part 2
# 8 Nov 2022 Brian Green
#
# Problem:
# Decode the LED segments
#

"""
 0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""

# 0 = 6 segments
# 1 = 2 segments
# 2 = 5 segments
# 3 = 5 segments
# 4 = 4 segments
# 5 = 5 segments
# 6 = 6 segments
# 7 = 3 segments
# 8 = 7 segments
# 9 = 6 segments

# 2 seg = 1
# 3 seg = 7
# 4 seg = 4
# 5 seg = 2, 3, 5
# 6 seg = 0, 6, 9
# 7 seg = 8

# 1 is 2 segments
# 4 is 4 segments
# 7 is 3 segments
# 3 is 5 segments and shares 3 of them with 7
# 2 is 5 segments and shares 3 of them with 4
# 5 is 5 segments and shares 2 of them with 4
# 9 is 6 segments and shares 4 of them with 4
# 6 is 6 segments and shared 5 of them with 5 and only 3 of them with 4
# 0
# 8 is 7 segments


import os

filename = "data" + os.sep + "brian_aoc202108.dat"
with open(filename) as data_file:
    data_set = [pos.split() for pos in data_file.readlines()]

print(data_set)
"""

miswired_data = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]

data_set = [pos.split() for pos in miswired_data]
# print(data_set)
"""

count = 0
for message in data_set:
    led_segments = {2: [], 3: [], 4:[], 5:[], 6:[], 7:[]}
    segment_map = {2: {}, 3: {}, 4:{}, 5:{}, 6:{}, 7:{}}
    
    for data in message[:10]:
        num_segments = len(data)
        # print(num_segments)
        # print(data)
        led_segments[num_segments].append(data)
        # print(led_segments[num_segments])
    # print(led_segments)

    led_nums = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
    
    # 1 is 2 segments
    led_nums[1] = led_segments[2][0]
    segment_map[2][led_nums[1]] = 1
    
    # 7 is 3 segments
    led_nums[7] = led_segments[3][0]
    segment_map[3][led_nums[7]] = 7

    # 4 is 4 segments
    led_nums[4] = led_segments[4][0]
    segment_map[4][led_nums[4]] = 4

    # 8 is 7 segments
    led_nums[8] = led_segments[7][0]
    segment_map[7][led_nums[8]] = 8

    # 3 is 5 segments and shares 3 of them with 7
    # 2 is 5 segments and shares 3 of them with 4
    # 5 is 5 segments and shares 2 of them with 4
    for led in led_segments[5]:
        if len(''.join(set(led_nums[7]).intersection(led))) == 3:
            led_nums[3] = led
            segment_map[5][led] = 3
        elif len(''.join(set(led_nums[4]).intersection(led))) == 3:
            led_nums[5] = led
            segment_map[5][led] = 5
        else:
            led_nums[2] = led
            segment_map[5][led] = 2

    # 9 is 6 segments and shares 4 of them with 4
    # 6 is 6 segments and shared 5 of them with 5 and only 3 of them with 4
    # 0 is 6 segments and shares 3 of them with 7
    for led in led_segments[6]:
        if len(''.join(set(led_nums[4]).intersection(led))) == 4:
            led_nums[9] = led
            segment_map[6][led] = 9
        elif len(''.join(set(led_nums[7]).intersection(led))) == 3:
            led_nums[0] = led
            segment_map[6][led] = 0
        else:
            led_nums[6] = led
            segment_map[6][led] = 6
            
    display_num = 0
    for data in message[11:]:
        display_num *= 10
        possible_segs = segment_map[len(data)]
        for key, value in possible_segs.items():
            if len(''.join(set(key).intersection(data))) == len(data):
                display_num += value
    print(display_num)
    count += display_num
print(count)
