
# Advent of Code 2016 - Day 5 Part 2
# 20 May 2023 Brian Green
#
# Problem:
# Day 5: How About a Nice Game of Chess?
# Given the actual Door ID and this new method, what is the password?
#

import hashlib

data_door = "abc"
# data_door = "INSERT YOUR DOOR NAME HERE"

hashname = "999999"
counter = 0
code = list("xxxxxxxx")

while 'x' in code:
    while not hashname.startswith('00000'):
        check_door = data_door + str(counter)
        hashname = hashlib.md5(check_door.encode('utf-8')).hexdigest()
        counter += 1
    position = hashname[5]
    print(position)
    if position in '01234567':
        if code[int(position)] == 'x':
            # Discard if we already have a number in this position
            code[int(position)] = hashname[6]
        print("".join(code))
    hashname = "999999"
    counter += 1
print("".join(code))
