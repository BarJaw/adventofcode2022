import string
data = [line.rstrip() for line in open('Inputs/Day3.txt', 'r', encoding="UTF-8")]

sum = 0
for line in data:
    comp1 = line[:int(len(line) / 2)]
    comp2 = line[int(len(line) / 2):]
    # print(line)
    # print(comp1)
    # print(comp2)
    for item in comp1:
        if item in comp2:
            both = item
    if both in list(string.ascii_lowercase):
        sum += ord(both) - 96
    if both in list(string.ascii_uppercase):
        sum += ord(both) - (65 - 27)
# print(sum)
sum = 0
for i in range(0, len(data) - 2, 3):
    r1 = data[i]
    r2 = data[i + 1]
    r3 = data[i + 2]
    for item in r1:
        if item in r2 and item in r3:
            badge = item
    if badge in list(string.ascii_lowercase):
        # print(ord(badge) - 96)
        sum += ord(badge) - 96
    if badge in list(string.ascii_uppercase):
        # print(ord(badge) - 38)
        sum += ord(badge) - 38
print(sum)