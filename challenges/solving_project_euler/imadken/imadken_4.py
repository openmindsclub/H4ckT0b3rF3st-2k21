
def palindrom(x):
    x=str(x)
    return x == x[::-1]


max=0
for i in range(999,100,-1):

    for z in range(i,99,-1):

        if palindrom(z*i) and z*i > max:
            

            max=z*i
            largest = f"{z} * {i} = {max}"

print(largest)            