# Advent of Code 2022 - Day 8 Part 2
# 8 Dec 2022 Brian Green
#
# Problem:
# Treetop Tree House, best scenic view

# filename = 'test.dat'
filename = "data.dat"
with open(filename) as data_file:
    data_set = [list(num.strip()) for num in data_file.readlines()]

# print(data_set)

east_west = []
for row in data_set:
    east_west.append(list(map(int, row)))
north_south = [
    [east_west[j][i] for j in range(len(east_west))] for i in range(len(east_west[0]))
]

max_east = len(north_south)
max_south = len(east_west)

scenic_score = 0

for x in range(1, max_east - 1):
    for y in range(1, max_south - 1):
        tree = east_west[y][x]
        score = 1
        west = east_west[y][:x].copy()
        west.reverse()
        north = north_south[x][:y].copy()
        north.reverse()
        directions = [west, east_west[y][x + 1 :], north, north_south[x][y + 1 :]]
        # print(directions)

        for dir in directions:
            num_of_trees = 0
            found_limit = False
            if dir is not None and dir != []:
                # print(dir)
                for t in dir:
                    # print(f"t={t} tree={tree} x={x} y={y} num={num_of_trees} s={score} {found_limit}")
                    if found_limit is False:
                        num_of_trees += 1
                    if t >= tree:
                        # print('SKIP')
                        found_limit = True
            score *= num_of_trees

        # print(score)
        if score > scenic_score:
            scenic_score = score

print(scenic_score)
