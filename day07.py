from collections import defaultdict

with open("day07.txt") as raw:
    data = raw.read().strip().split("\n")

dirs = defaultdict(list)  # defaultdict to instantiate when key doesn't exist
naive_dirsizes = defaultdict()
dirsizes = defaultdict()
part1 = 0
part2 = 999_999_999  # arbitrarily large

for line in data:
    match line.split():
        case "$", "cd", "/":
            cur_dir = ["root"]
        case "$", "cd", "..":
            cur_dir.pop()
        case "$", "cd", x:
            cur_dir.append(x)
        case "$", "ls":
            pass
        case "dir", dir:
            dirs["/".join(cur_dir)].append(0)  # to include empty directories
        case size, _:
            dirs["/".join(cur_dir)].append(int(size))

for k, v in dirs.items():  # compute size of files in directory
    naive_dirsizes[k] = sum([x for x in v])

for k, v in naive_dirsizes.items():  # compute size including nested directories
    dirsizes[k] = sum([entry[1] for entry in naive_dirsizes.items() if k in entry[0]])

to_del = dirsizes["root"] - 40_000_000

for k, v in dirsizes.items():
    if v <= 100_000:
        part1 += v
    if v >= to_del and v < part2:
        part2 = v

print(part1, part2)
