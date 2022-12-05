def transfer(instruction, stacks):
    howMany = instruction[0]
    fromWhere = instruction[1] - 1
    whereTo = instruction[2] - 1
    # print(stacks)
    # print(howMany)
    # print(fromWhere)
    # print(whereTo)
    for i in range(howMany):
        stacks[whereTo].insert(0, stacks[fromWhere][0])
        stacks[fromWhere].pop(0)
    return stacks

def transferPartTwo(instruction, stacks):
    howMany = instruction[0]
    fromWhere = instruction[1] - 1
    whereTo = instruction[2] - 1
    temp = []
    for i in range(howMany):
        temp.append(stacks[fromWhere][i])
    for i in range(howMany):
        stacks[fromWhere].pop(0)
        stacks[whereTo].insert(0, temp[len(temp) - i - 1])
    return stacks


with open('Inputs/Day5.1.txt', 'r') as file:
    lines = file.readlines()
    stackCount = 9
    stacks = [[] for i in range(stackCount)]
    # print(stacks) 
    for i, line in enumerate(lines):
        for j in range(1, len(line), 4):
            if line[j] != " ":
                stacks[j // 4].append(line[j])

with open('Inputs/Day5.2.txt', 'r') as file:
    lines = file.readlines()
    instructions = []
    for i, value in enumerate(lines):
        lines[i] = lines[i].rstrip().split()
        instructions.append([int(lines[i][1]), int(lines[i][3]), int(lines[i][5])])

  
for instruction in instructions:
    stacks = transferPartTwo(instruction, stacks)

# print(stacks)
# print(transferPartTwo([2,2,1], stacks))

for i in range(stackCount):
    print(stacks[i][0], end='')
print()