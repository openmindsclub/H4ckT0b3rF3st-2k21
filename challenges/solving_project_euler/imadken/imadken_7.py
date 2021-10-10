from math import sqrt

def PrimePosition(y):
  x=1
  count=0
  while count!=y:
      x+=1
      if all(x%i for i in range(2, int(sqrt(x))+1)): #This condition is equivalent to if x is a prime number
          count+=1

  return x       
          

if __name__=="__main__":
    print(PrimePosition(10001))