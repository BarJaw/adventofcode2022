def checkCycle(cycle, meaningfulCycles):
    if cycle in meaningfulCycles:
        return cycle
    return 0

data = [line.rstrip().split() for line in open('Inputs/Day10-example.txt', 'r', encoding="UTF-8")]

cycle = 0
registerX = 1
sum = 0
meaningfulCycles = [20, 60, 100, 140, 180, 220]
i = 0
while i < len(data):
    instruction = data[i]
    # print(instruction)
    if instruction[0] == 'noop':
        cycle += 1
        sum += checkCycle(cycle, meaningfulCycles) * registerX
        i += 1
    else:
        sum += checkCycle(cycle, meaningfulCycles) * registerX
        cycle += 1
        sum += checkCycle(cycle, meaningfulCycles) * registerX
        registerX += int(instruction[1])
        cycle += 1
        sum += checkCycle(cycle, meaningfulCycles) * registerX
        i += 1
    
print(sum)

    # instruction = data[i]
    # cycle += 1
    # # if cycle == 20:
    # #     print(instruction)
    # #     print(registerX)
    # #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    # # if cycle == 60:
    # #     print(instruction)
    # #     print(registerX)
    # #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    # # if cycle == 100:
    # #     print(instruction)
    # #     print(registerX)
    # #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    # # if cycle == 140:
    # #     print(instruction)
    # #     print(registerX)
    # #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    # # if cycle == 180:
    # #     print(instruction)
    # #     print(registerX)
    # #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    # # if cycle == 220:
    # #     print(instruction)
    # #     print(registerX)
    # #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    # if instruction[0] != 'noop':
    #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    #     cycle += 1
    #     registerX += int(instruction[1])
    #     sum += checkCycle(cycle, meaningfulCycles) * registerX
    # sum += checkCycle(cycle, meaningfulCycles) * registerX
    # i += 1
print(sum)