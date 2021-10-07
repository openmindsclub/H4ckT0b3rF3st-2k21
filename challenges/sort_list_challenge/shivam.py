# Python3 program to sort an array without comparison operator.
 
def sortArr(arr, n, min_no, max_no):
    # Count of elements in given range
    m = max_no - min_no + 1
     
    # Count frequencies of all elements
    c = [0] * m
    for i in range(n):
        c[arr[i] - min_no] += 1
 
    # Traverse through range. For every
    # element, print it its count times.
    for i in range(m):
        for j in range((c[i])):
            print((i + min_no), end=" ")
            
arr = [10, 10, 1, 4, 4, 100, 0]
min_no,max_no = 0,100
n = len(arr)
sortArr(arr, n, min_no, max_no)
