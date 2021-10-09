def selection_sort(collection):
    """
    Examples:
     implementation of sorting algo using python
     >> selection_sort[-1, 5, 10, 0]
     [-1,0,5,10]
    """
    length = len(collection)
    for i in range(length - 1):
        small = i
        for k in range(i + 1, length):
            if collection[k] < collection[small]:
                small = k
        if small != i:
            collection[small], collection[i] = (collection[i], collection[small])
            
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selection_sort(unsorted))