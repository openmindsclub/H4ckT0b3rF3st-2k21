numberList = [1, 2, 56, 8, 4, 75, 1, 23, 36, 54, -12, -14, 52, -7]

for i in range(len(numberList)):
    for j in range(i + 1, len(numberList)):
        if(numberList[i] > numberList[j]):
            temp = numberList[i]
            numberList[i] = numberList[j]
            numberList[j] = temp
