def contains(range1, range2):
    if range1[0] >= range2[0] and range1[len(range1) - 1] <= range2[len(range2) - 1]:
        return True
    elif range1[0] <= range2[0] and range1[len(range1) - 1] >= range2[len(range2) - 1]:
        return True
    return False

def overlaps(range1, range2):
    list1 = [i for i in range(range1[0], range1[1] + 1)]
    list2 = [i for i in range(range2[0], range2[1] + 1)]
    if any(i in list1 for i in list2):
        return True
    return False

with open('Inputs/Day4.txt', 'r') as file:
    data = file.readlines()
    for index, value in enumerate(data):
        data[index] = data[index].rstrip().split(',')
        data[index][0] = [int(x) for x in data[index][0].split('-')]
        data[index][1] = [int(x) for x in data[index][1].split('-')]
    #print(data)
    # part one
    count = 0
    for line in data:
        if contains(line[0], line[1]):
             count += 1
             # print(line)
    # print(count)
    
    # part two
    count = 0
    for line in data:
        if overlaps(line[0], line[1]):
            count += 1
    print(count)
