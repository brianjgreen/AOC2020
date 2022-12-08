
# Advent of Code 2022 - Day 8 Part 1
# 1 Dec 2022 Brian Green
#
# Problem:
# Tuning Trouble

# filename = 'test.dat'
filename = "data.dat"
with open(filename) as data_file:
    data_set = [list(num.strip()) for num in data_file.readlines()]

print(data_set)

east_west = []
for row in data_set:
    east_west.append(list(map(int, row)))
north_south = [[east_west[j][i] for j in range(len(east_west))] for i in range(len(east_west[0]))]

for row in east_west:
    print(row)
print()
for col in north_south:
    print(col)

visible = len(east_west) * 2
visible += ((len(north_south) - 2) * 2)

print(visible)

max_east = len(north_south)
max_south = len(east_west)
print(f"{max_east} {max_south}")

print(east_west[1][3:])
for x in range(1, max_east - 1):
    for y in range(1, max_south - 1):
        # print(f"{x} {y}")
        tree = east_west[y][x]
        if max(east_west[y][:x]) < tree or max(east_west[y][x+1:]) < tree or max(north_south[x][:y]) < tree or max(north_south[x][y+1:]) < tree:
            visible += 1
            print(f"{x} {y}")

print(visible)
