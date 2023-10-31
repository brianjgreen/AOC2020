# Advent of Code 2021 - Day 21 Part 1
# 23 Dec 2021 Brian Green
#
# Problem:
# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?
#

roll = 0


def get_roll():
    global roll
    roll += 1
    totla = (roll - 1) % 100 + 1
    print(f"roll: {totla}")
    return totla


player_1_space = 3
player_2_space = 10
# player_1_space = 4
player_1_score = 0
# player_2_space = 8
player_2_score = 0
# for i in range(4):
while player_1_score < 1000 and player_2_score < 1000:
    moves = get_roll() + get_roll() + get_roll() + player_1_space
    print(f"p1_moves {moves}")
    player_1_space = moves % 10
    if player_1_space == 0:
        player_1_space = 10
    player_1_score += player_1_space

    if player_1_score >= 1000:
        break

    moves = get_roll() + get_roll() + get_roll() + player_2_space
    print(f"p2_moves {moves}")
    player_2_space = moves % 10
    if player_2_space == 0:
        player_2_space = 10
    player_2_score += player_2_space
    # print(i % 5)
print(f"p1 {player_1_space} {player_1_score}")
print(f"p2 {player_2_space} {player_2_score}")
print(f"Number of rolls: {roll}")
if player_1_score < 1000:
    loser = player_1_score
else:
    loser = player_2_score
print(roll * loser)
