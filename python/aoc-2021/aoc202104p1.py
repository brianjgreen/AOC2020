# Advent of Code 2021 - Day 4 Part 1
# 5 Dec 2021 Brian Green
#
# Problem:
# Figure out which board will win first. What will your final score be if you choose that board?
#

import os

filename = "data" + os.sep + "brian_aoc202104.dat"
with open(filename) as data_file:
    data_set = [bingo.split() for bingo in data_file.readlines()]

testcase = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

# data_set = testcase.split()

temp_data_set = []
for row in data_set:
    for column in row:
        temp_data_set.append(column)

data_set = temp_data_set

print(data_set)
order = data_set.pop(0)
order = [int(x) for x in order.split(",")]
print(order)

all_cards = []
num_cards = int(len(data_set) / 25)
# print(num_cards)
for z in range(num_cards):
    column = []
    for y in range(5):
        row = []
        for x in range(5):
            row.append(int(data_set.pop(0)))
        column.append(row)
    all_cards.append(column)

# print(all_cards)


def check_row(row, called_nums):
    matches = 0
    for num in row:
        if num in called_nums:
            matches += 1
    return matches


def check_column(column, called_nums):
    return check_row(column, called_nums)


def check_card(card, called_nums):
    for row in card:
        if check_row(row, called_nums) == 5:
            return True
    for column in range(5):
        col_nums = []
        for num in range(5):
            col_nums.append(card[num][column])
        if check_column(col_nums, called_nums) == 5:
            return True
    return False


def play_bingo():
    for bingo in range(5, len(order)):
        for card in all_cards:
            if check_card(card, order[:bingo]):
                # print(f"card {card} bingo!")
                return (card, order[:bingo])


card, nums_called = play_bingo()

print(card)
print(nums_called)

total_card_sum = 0
for row in card:
    for column in row:
        print(column)
        if column not in nums_called:
            total_card_sum += column
print(nums_called[-1] * total_card_sum)
