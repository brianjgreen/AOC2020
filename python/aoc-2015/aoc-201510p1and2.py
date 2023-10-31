# Advent of Code 2015 - Day 10 Part 1 and 2
# 22 Nov 2021 Brian Green
#
# Problem:
# 1. apply this process 40 times. What is the length of the result?
# 2. apply this process 50 times. What is the length of the new result?
#
# NOTE: Used code from https://www.rosettacode.org/wiki/Look-and-say_sequence#Python
#

from itertools import groupby, islice


def lookandsay(number="1"):
    while True:
        yield number
        number = "".join(str(len(list(g))) + k for k, g in groupby(number))


# iterations = 40
iterations = 50
number = "\n".join(islice(lookandsay("3113322113"), iterations + 1))
one_number = number.split()
print(one_number)
print(len(one_number[-1]))
