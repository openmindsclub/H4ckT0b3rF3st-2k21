
#this function checks whether a number is even or not
def even(x):
  return x % 2 == 0

#A recursive fibonacci function that sums even elements
def fib(x,y):
    
    global s  
    
    if y < 4000000:
    
       if even(y): 
          s = s+y
		 
       fib(y,x+y)   


s =0

fib(1,1)

print(s)

