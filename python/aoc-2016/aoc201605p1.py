
# Advent of Code 2016 - Day 5 Part 1
# 20 May 2023 Brian Green
#
# Problem:
# Day 5: How About a Nice Game of Chess?
# Given the actual Door ID, what is the password?
#

import hashlib

data_door = "abc"
# data_door = "INSERT YOUR DOOR NAME HERE"

hashname = "999999"
counter = 0
for password in range(8):
    while not hashname.startswith('00000'):
        check_door = data_door + str(counter)
        hashname = hashlib.md5(check_door.encode('utf-8')).hexdigest()
        counter += 1
    print(hashname[5], end="")
    hashname = "999999"
    counter += 1
print()
