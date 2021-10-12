
def Sum_Divisors(x):
  s = 1
  for i in range(2,(x // 2) + 1):
      if x % i == 0:
        s += i
  return s


def Is_Abundant(n):
    
   return Sum_Divisors(n) > n

abundants = [number for number in range(12,28124) if Is_Abundant(number)]   #list of abundant numbers 


Sum_Abundants = set()  # I used a set() because its much faster than using a list

l = len(abundants)

for i in range(l):

    for j in range(i,l):

        
        if abundants[i]+abundants[j] > 28123:
            break
        else:
            Sum_Abundants.add(abundants[i]+abundants[j])


NonAbSums = [number for number in range(28124) if number not in Sum_Abundants]

print(sum(NonAbSums))