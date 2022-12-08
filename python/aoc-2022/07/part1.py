# Advent of Code 2022 - Day 7 Part 1
# 7 Dec 2022 Brian Green
#
# Problem:
# No Space Left On Device

# import pprint

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

print(data_set)

filesys = {}
cwd = '/'

# build the filesystem
for cmd in data_set:
    if '$ cd ..' == cmd:
        # change current directory up one level
        cwd = '/'.join(cwd.split('/')[:-2]) + '/'
    elif '$ cd /' == cmd:
        # ignore, change to root directory, only first command
        pass
    elif '$ cd ' in cmd:
        # change current directory down one
        cwd += cmd.split()[2] + '/'
    elif '$ ls' == cmd:
        # ignore, show contents of directory
        pass
    elif 'dir ' in cmd:
        # ignore, make a new directory, will be embedded in filename anyway
        pass
    else:
        # save filename and size
        size, filename = cmd.split()
        filesys[cwd + filename] = size

# pprint.pprint(filesys)

directories = {}

# add up the file size in each subdirectory
for filename, size in filesys.items():
    node = '/'.join(filename.split('/')[:-1])
    print(node)
    if node != '':
        if node in directories:
            directories[node] += int(size)
        else:
            directories[node] = int(size)

# print(directories)

sub_by_depth = {}
# find the max subdirectory depth
for name, size in directories.items():
    count = name.count("/")
    if count in sub_by_depth:
        sub_by_depth[count][name] = size
    else:
        sub_by_depth[count] = {name: size}
print(sub_by_depth)

# sort the dirs by max depth
sorted_sub_by_depth = {k: sub_by_depth[k] for k in sorted(sub_by_depth, reverse=True)}
print(sorted_sub_by_depth)
all_dirs = {}
for value in sorted_sub_by_depth.values():
    all_dirs.update(value)
print(all_dirs)

# add up the totals from each directories child subdirectories
new_dirs = {}
for name, size in all_dirs.items():
    if name.count("/") != 1:
        this_name = '/'.join(name.split('/')[:-1])
        print(this_name)
        if this_name in all_dirs:
            all_dirs[this_name] += size
        elif this_name in new_dirs:
            new_dirs[this_name] += size
        else:
            new_dirs[this_name] = size

# print(all_dirs)
# print(new_dirs)
all_dirs.update(new_dirs)
# print(all_dirs)

# update the subdir sizes to account for the newly discovered subdirs
for name, size in new_dirs.items():
    if name.count("/") != 1:
        this_name = '/'.join(name.split('/')[:-1])
        # print(this_name)
        if this_name in all_dirs:
            all_dirs[this_name] += size

total = 0
# find all subdirectories with total size below 100000
for name, size in all_dirs.items():
    if size <= 100000:
        total += size
        print(name)

print(total)
