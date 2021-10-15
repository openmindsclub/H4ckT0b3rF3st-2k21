from math import pow

def squareOfSum(n):
    return(pow(((n+1) * n / 2),2))

def sumOfSquares(n):
    sum = 0
    for i in range(n + 1):
        sum += pow(i,2)
        print(i)
    return sum

print(squareOfSum(100) - sumOfSquares(100))