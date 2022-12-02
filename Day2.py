# A rock (65)           win - 6p
# B paper  (66)         draw - 3p
# C Scissors  (67)      lose - 0p
# X rock (88) - 1p
# Y paper (89) - 2p
# Z Scissors (90) -3p

# 23 draw
# 22 loss
# 21 win


totalScore = 0
with open('Inputs/Day2.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()    
    # part one
    for index, value in enumerate(data):
        data[index] = data[index].rstrip().split()
        opponent = ord(data[index][0]) - 64
        player = ord(data[index][1]) - 87
        totalScore += player
        if player - opponent == 1 or player - opponent == -2:
            totalScore += 6
        elif player - opponent == 0:
            totalScore += 3
    # print(totalScore)

    # part two
    lossDict = {
        'A' : 3,
        'B' : 1,
        'C' : 2
    }
    drawDict = {
        'A' : 1,
        'B' : 2,
        'C' : 3
    }
    winDict = {
        'A' : 2,
        'B' : 3,
        'C' : 1
    }
    totalScore = 0
    for game in data:
        opponent = game[0]
        result = game[1]
        if result == 'X':
            totalScore += lossDict[opponent]
        elif result == 'Y':
            totalScore += drawDict[opponent]
            totalScore += 3
        else:
            totalScore += winDict[opponent]
            totalScore += 6
    print(totalScore)