
from functools import reduce
import math

def primeFactors(n,d):
	
	# The number of two's that divide n
	while n % 2 == 0:
		if 2 in d:
			d[2] += 1
		else:
			d[2]=1
		n=n//2		
	   

	#Here x is odd 
	#We start from 3 and increment with 2 because the diffrence between two prime factors is >=2
	
	for i in range(3,int(math.sqrt(n))+1,2):   
		
		while n % i== 0:
			if i in d:

				d[i]+=1
				 
			else:
				
				d[i]=1	
			
			n = n // i
			 
	#here n is either prime or == 1 
	if n > 2:
		d[n]=1
	
	
		


   
	

   


def Triangular_Divisors():

    n=7

    while True:

    	d={}

    	t=n*(n+1)//2    # t is the next triangular

    	n+=1

    	primeFactors(t,d)

    	powers = map(lambda x:(x+1),d.values())

    	divisors = reduce(lambda x,y:x*y, powers)

    	if divisors >=500	:	
    		return t
    		break
    
if __name__=="__main__":

     print(Triangular_Divisors())

