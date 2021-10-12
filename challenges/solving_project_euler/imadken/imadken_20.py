from math import factorial

def Sum_Digits_Factorial(x):
    
    return sum([int(i) for i in str(factorial(x))])

print(Sum_Digits_Factorial(100))