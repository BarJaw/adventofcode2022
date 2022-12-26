data = [line.rstrip().split() for line in open('Inputs/Day7-example.txt', 'r', encoding="UTF-8")]

directories = {}
path = ''
i = 0
while i < len(data):
    if data[i][0] == '$':
        if data[i][1] == 'cd':
            if data[i][2] == "..":
                # print(path)                
                path = path[:path.rfind('/', len(path) - 2)]
                # print(path)
            elif data[i][2] != '/':
                path += data[i][2] + '/'
            else:
                path += '/'
            if path not in directories and data[i][2] != '..':
                directories[path] = 0
    i += 1
    print(path)
print(directories)
# $ cd /
# $ cd a
# $ cd e
# $ cd ..
# $ cd ..
# $ cd d