def Multiples_5_3(x): 
    
    return x%3 == 0 or x%5 == 0

print(sum(filter(Multiples_5_3, range(1, 1000))))