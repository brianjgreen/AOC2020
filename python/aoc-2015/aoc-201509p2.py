
# Advent of Code 2015 - Day 9 Part 2
# 22 Nov 2021 Brian Green
#
# Problem:
# What is the distance of the longest route?
#

import random
import os

filename = "data" + os.sep + "brian_aoc201509.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

places = {}
shortest_list = []
longest_distance = 0

for trip in data_set:
    travel = trip.split()
    origin = travel[0]
    destination = travel[2]
    distance = int(travel[4])
    if origin in places:
        places[origin][destination] = distance
    else:
        places[origin] = {destination: distance}
    if destination in places:
        places[destination][origin] = distance
    else:
        places[destination] = {origin: distance}

print(places)
path = list(places.keys())
print(path)


def get_distance(path):
    # print(path)
    distance = 0
    origin = path.pop(0)
    while len(path) > 0:
        destination = path.pop(0)
        distance += places[origin][destination]
        # print(places[origin][destination])
        origin = destination
    # print(distance)
    return distance


for i in range(1000000):
    random.shuffle(path)
    distance = get_distance(path.copy())
    if distance > longest_distance:
        longest_distance = distance
        shortest_list = path.copy()

print(longest_distance)
print(shortest_list)
