# Advent of Code 2015 - Day 11 Part 1 and 2
# 22 Nov 2021 Brian Green
#
# Problem:
# 1. what should his next password be?
# 2. What's the next one?
#

import string

# Password Rule 1
straight = []
alpha = string.ascii_lowercase
while len(alpha) > 2:
    straight.append(alpha[:3])
    alpha = alpha[1:]
print(straight)

# Password Rule 2
banned = ["i", "o", "l"]

# Password Rule 3
pairs = []
alpha = list(string.ascii_lowercase)
while len(alpha) > 0:
    letter = alpha.pop(0)
    pairs.append(letter + letter)
print(pairs)


def is_valid(password):
    for b in banned:
        if b in password:
            return False

    good = False
    for s in straight:
        if s in password:
            good = True
            break
    if not good:
        return False

    count = 0
    for p in pairs:
        if p in password:
            count += 1
    if count < 2:
        return False

    return True


print(f"hijklmmn {is_valid('hijklmmn')}")
print(f"abbceffg {is_valid('abbceffg')}")
print(f"abbcegjk {is_valid('abbcegjk')}")
print(f"abcdffaa {is_valid('abcdffaa')}")
print(f"ghjaabcc {is_valid('ghjaabcc')}")


def increment_letter(letter):
    b = bytes(letter, "utf-8")
    b = b[0] + 1
    return chr(b)


def increment_password(password):
    index = -1
    if password[index] == "z":
        password = increment_password(password[:-1]) + "a"
    else:
        password = password[:-1] + increment_letter(password[index])

    return password


def get_next_valid_password(password):
    while not is_valid(password):
        # print(password)
        password = increment_password(password)
    return password


# password = "abcdefgh"
# password = "ghijklmn"
# Part 1
password = get_next_valid_password("vzbxkghb")
print(password)
# Part 2
print(get_next_valid_password(increment_password(password)))
