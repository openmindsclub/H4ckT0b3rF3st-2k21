
#For this problem i propose 02 solutions
#The 1st solution is the simple one because we will be using datetime module which is going to do all the work for us


#1st solution:

from datetime import datetime

count = 0

for i in range(1901,2001):

    for j in range(1,13):

        if datetime(i,j,1).strftime("%a") == "Sun":
            
            count+=1

print(count)



#2nd solution:
#i've done a quick search and found out that 01-01-1901 was a tuesday.

def IsLeap(Year):  

  # Checking if the given year is leap year
  #   
  if Year % 400 == 0 or  Year % 100 != 0 and  Year % 4 == 0 :   
    return True
  else:return False 


months={1:31,
2:28,
3:31,
4:30,
5:31,
6:30,
7:31,
8:31,
9:30,
10:31,
11:30,
12:31
}


days=2
Sunday_Count=0

for i in range(1901,2001):

    for j in range(1,13):

            days += months[j] % 7

            if IsLeap(i) and j == 2:
                days += 1

            

            if days % 7 == 0:
                Sunday_Count += 1
        
print(Sunday_Count)      