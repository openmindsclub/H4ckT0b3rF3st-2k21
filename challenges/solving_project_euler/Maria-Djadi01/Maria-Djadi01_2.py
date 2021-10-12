fibList = [1,2]
sum = 0

for i in range(4000000):
    if i == fibList[-1] + fibList[-2] :
        fibList.append(i)

for i in fibList:
    if i % 2 == 0:
        sum += i

print(sum)