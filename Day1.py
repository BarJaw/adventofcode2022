with open("Day1.txt") as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()

      
    maxSum = 0
    sum = 0
    elves = []
    for i in range(len(dane)):
        if dane[i] == "":
            elves.append(sum)
            sum = 0
        else:
            sum += int(dane[i])
    elves = sorted(elves)
    print(elves[-1]+elves[-2]+elves[-3])

    
