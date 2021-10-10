import math

def primeFactors(x):
	
    factors=[] 

    # we print the number of two's
    while x % 2 == 0:
        # print(2,end="  ")
        factors.append(2) 
        x = x // 2
		 
    #Here x is odd 
    #We start from 3 and increment with 2 because the diffrence between two prime factors is >=2
	
    for i in range(3,int(math.sqrt(x))+1,2):    
		 
		
        while x % i== 0:
            # print(i,end="  ")
            factors.append(i)
            x = x // i
			 
    #Here x is either == 1 or is prime 
    if x > 2:
        factors.append(x)

    return max(factors)    
		 
print(primeFactors(600851475143))
