numberList = [1,2,56,8,4,75,1,23,36,54,-12,-14,52,-7]
sort_list = []

for i in numberList:
    sort_list = [x for x in sort_list if i > x] + [i] + [x for x in sort_list if i <= x]
