# Advent of Code 2022 - Day 21 Part 2
# 21 Dec 2022 Brian Green
#
# Problem:
# Monkey Math


# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

# print(data_set)
howl = {}


def get_val(monkey):
    oper = howl[monkey]

    if len(oper) == 1:
        return int(oper[0])

    val_1, math, val_2 = oper
    val_1 = get_val(val_1)
    val_2 = get_val(val_2)

    if math == '+':
        return (val_1 + val_2)
    elif math == '-':
        return (val_1 - val_2)
    elif math == '*':
        return (val_1 * val_2)
    elif math == '/':
        return (val_1 / val_2)
    elif math == '=':
        print(f"{val_1} {val_2} {val_2 - val_1} {val_2 / val_1} {howl['humn']}")
        if val_2 > val_1:
            print('OVER')
            return(True)
        return (val_1 == val_2)
    else:
        print(f'UNKNOWN OPERATOR {math}!!!')


for monkey in data_set:
    name, oper = monkey.split(': ')
    howl[name] = oper.split()

# print(howl)
howl['root'][1] = '='

counter = 3699945350000
while get_val('root') == False:
    howl['humn'][0] = str(counter)
    counter += 1

print(get_val('root'))
print(howl['root'])
print(howl['humn'])
