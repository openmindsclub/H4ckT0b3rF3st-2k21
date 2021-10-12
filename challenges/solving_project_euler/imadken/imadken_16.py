def SumDigits(x) :
    if x != 0 :
        return x % 10 + SumDigits(x//10)
    return 0    


print(SumDigits(2**1000))

