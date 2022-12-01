with open("Inputs/Day1.txt", mode='r', encoding="UTF-8") as file:
    data = file.readlines()

    for num, line in enumerate(data):
        data[num] = data[num].rstrip()

    maxSum = 0
    sumOfCallories = 0
    elves = []


    for index, line in enumerate(data):
        if data[index] == "":
            elves.append(sumOfCallories)
            sumOfCallories = 0
        else:
            sumOfCallories += int(data[index])
    # print(elves)
    print(elves[-1]+elves[-2]+elves[-3])