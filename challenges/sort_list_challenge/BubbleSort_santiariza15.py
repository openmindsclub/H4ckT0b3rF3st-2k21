import array
a = array.array('i', [])
k = int(input("Enter size of array:"))
for i in range(0, k):
    num = int(input("Enter %d array element:" % (i + 1)))
    a.append(num)

print("All array elements are:", end="")
for i in a:
    print(i, end=" ")

def bubbleSort(arr):
	n = len(arr)

	for i in range(n-1):

		for j in range(0, n-i-1):

			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubbleSort(a)

print ("Sorted array is:")
for i in range(len(a)):
	print ("% d" % a[i]),
