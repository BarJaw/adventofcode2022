data = [line.rstrip() for line in open('Inputs/Day6.txt', 'r', encoding="UTF-8")]

for line in data:
    for index, value in enumerate(line):
        if index <= len(line) - 14:
            four = line[index:index + 14]
            if len(set(four)) == len(four):
                print(index + 14)
                break
        
                