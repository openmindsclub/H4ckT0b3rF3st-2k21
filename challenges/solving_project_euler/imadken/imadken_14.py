

from numba import njit


@njit(fastmath=True) 
def even(x):
    return x % 2 == 0

@njit(fastmath=True) 
def N_is_Even(x):
    return x/2

@njit(fastmath=True) 
def N_is_Odd(x):
    return 3 * x + 1


@njit(fastmath=True)
def longestCollatz(x):
    NbrElements=0
    Nbr=0
    i=2
    while True and i<x:
	
        n=i
        NbrElements=0
	
        while n != 1:
            if even(n):
                NbrElements += 1
                n=N_is_Even(n)
            else :
                NbrElements += 1
                n=N_is_Odd(n)	
		
		
	
        NbrElements += 1
	
        if NbrElements>Nbr:
            longest={i:NbrElements}
            Nbr = NbrElements
        i+=1
		
	
	
    print(longest)		


    
if __name__ == "__main__":

    longestCollatz(1000000)  


