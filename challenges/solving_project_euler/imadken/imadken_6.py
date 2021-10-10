
def diff(x):
    SumSquares = SquareSums = 0
    for i in range(1,x+1):
        
        SumSquares += (i*i)
        
        SquareSums += i   
	
    return   (SquareSums*SquareSums) - SumSquares
   

print(diff(100))   
