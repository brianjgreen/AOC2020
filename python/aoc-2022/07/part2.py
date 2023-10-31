# Advent of Code 2022 - Day 7 Part 2
# 7 Dec 2022 Brian Green
#
# Problem:
# No Space Left On Device, min to free up

filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

filesys = {}
cwd = "/"

# build the filesystem
for cmd in data_set:
    if "$ cd .." == cmd:
        # change current directory up one level
        cwd = "/".join(cwd.split("/")[:-2]) + "/"
    elif "$ cd /" == cmd:
        # ignore, change to root directory, only first command
        pass
    elif "$ cd " in cmd:
        # change current directory down one
        cwd += cmd.split()[2] + "/"
    elif "$ ls" == cmd:
        # ignore, show contents of directory
        pass
    elif "dir " in cmd:
        # ignore, make a new directory, will be embedded in filename anyway
        pass
    else:
        # save filename and size
        size, filename = cmd.split()
        filesys[cwd + filename] = size

directories = {}

# add up the file size in each subdirectory
for filename, size in filesys.items():
    node = "/".join(filename.split("/")[:-1])
    if node != "":
        if node in directories:
            directories[node] += int(size)
        else:
            directories[node] = int(size)

sub_by_depth = {}
# find the max subdirectory depth
for name, size in directories.items():
    count = name.count("/")
    if count in sub_by_depth:
        sub_by_depth[count][name] = size
    else:
        sub_by_depth[count] = {name: size}

# sort the dirs by max depth
sorted_sub_by_depth = {k: sub_by_depth[k] for k in sorted(sub_by_depth, reverse=True)}
all_dirs = {}
for value in sorted_sub_by_depth.values():
    all_dirs.update(value)

# add up the totals from each directories child subdirectories
new_dirs = {}
for name, size in all_dirs.items():
    if name.count("/") != 1:
        this_name = "/".join(name.split("/")[:-1])
        if this_name in all_dirs:
            all_dirs[this_name] += size
        elif this_name in new_dirs:
            new_dirs[this_name] += size
        else:
            new_dirs[this_name] = size

all_dirs.update(new_dirs)

# update the subdir sizes to account for the newly discovered subdirs
for name, size in new_dirs.items():
    if name.count("/") != 1:
        this_name = "/".join(name.split("/")[:-1])
        if this_name in all_dirs:
            all_dirs[this_name] += size

# calc the total size of space on the disk in use by files
total_space_in_use = 0
for size in filesys.values():
    total_space_in_use += int(size)

max_disk = 70000000
need_disk = 30000000
free_disk = max_disk - total_space_in_use
remove_disk = need_disk - free_disk
print(
    f"max={max_disk} needed={need_disk} have={total_space_in_use} unused={free_disk} need_to_remove={remove_disk}"
)

# find the smallest dir that could be deleted to free up the required disk space
eligible_dir_size = max_disk
for size in all_dirs.values():
    if size >= remove_disk and size < eligible_dir_size:
        eligible_dir_size = size

print(eligible_dir_size)
