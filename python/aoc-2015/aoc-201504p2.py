
# Advent of Code 2015 - Day 4 Part 2
# 17 Nov 2021 Brian Green
#
# Problem:
#

import hashlib

prefix = '111111'
base = -1
while prefix != '000000':
    base += 1
    xhash = hashlib.md5()
    xhash.update(b'iwrupvqb')
    xhash.update(str(base).encode())
    prefix = xhash.hexdigest()[:6]
    # print(f"{base} {prefix}")

print(base)
