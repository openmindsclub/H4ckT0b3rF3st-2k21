import math

def is_prime(n):
    if n <= 1:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True
    
sum = 2
for i in range(3, 2000000):
    if is_prime(i):
        sum = sum + i        
print(sum)