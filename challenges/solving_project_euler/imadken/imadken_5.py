
import time
from numba import njit , prange

@njit(fastmath=True)

def divisible(x):
		for i in prange(2,21):
			if x%i==0:
				continue
			else:
				return False
		return True 


@njit(fastmath=True)               
def divisible_1_20():
	i=2520

	while True :

		if divisible(i):
			return(i)
			break   
		i+=1

if __name__=="__main__":

      print(divisible_1_20())
