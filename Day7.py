from collections import defaultdict

def get_sizes():
    lines = [line.rstrip() for line in open('Inputs/Day7.txt', 'r', encoding="UTF-8")]
    lines = [line for line in lines if not lines == "$ ls"]
    path = []
    sizes = defaultdict(int)

    for line in lines:
        # print(line)
        if line.startswith("$ cd"):
            match line:
                case "$ cd /":
                    path.clear()
                    path.append("/")
                case "$ cd ..":
                    path.pop()
                case _:
                    dir = line.split()[-1]
                    path.append(dir)
        else:
            filesize = line.split()[0]
            # print(filesize)
            if filesize.isdigit():
                filesize = int(filesize)
                for i in range(len(path)):
                    dir = '/'.join(path[:i + 1]).replace("//", "/")
                    sizes[dir] += filesize
    return sizes
sizes = get_sizes()

# part one
dirs_below_threshold = {directory: size for (directory, size) in sizes.items() if size <= 100000}
print(sum(dirs_below_threshold.values()))

# part two
total_disk_space = 70000000
required_disk_space = 30000000
space_to_free = sizes["/"] + required_disk_space - total_disk_space
dirs_above_threshold = {directory: size for (directory, size) in sizes.items() if size >= space_to_free}
print(min(dirs_above_threshold.values()))