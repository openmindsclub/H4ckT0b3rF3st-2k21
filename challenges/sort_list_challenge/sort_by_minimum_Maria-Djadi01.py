def sort(list):
    Index = len(list)

    for i in range(len(list)):
        minimum = min(list[0:Index])
        minInedx = list.index(minimum)
        list.remove(minimum)
        list.append(minimum)
        Index -= 1
    return list
