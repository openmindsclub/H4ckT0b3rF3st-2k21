def Sum_Divisors(x):
  s = 0
  for i in range(1,(x // 2) + 1):
      if x % i == 0:
        s += i
  return s


def Amicable(x,y):
    
    if x!=y:

      if Sum_Divisors(x) == y  and Sum_Divisors(y) == x :
        return True

    return False

   
def Sum_Amicable():
   l=[]

   for i in range(284,10000):
   
       if Amicable(i,Sum_Divisors(i)):

        if i not in l:

          l.append(i)

        if Sum_Divisors(i) not in l:
            
          l.append(Sum_Divisors(i))  
             
   
   print(sum(l))

Sum_Amicable()   
