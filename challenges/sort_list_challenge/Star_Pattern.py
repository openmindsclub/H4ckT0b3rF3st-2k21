"""
Problem Decription: Write a program to print the following pattern.
  
Print the pattern:
        
            *   
           ***
          *****
         *******
        *********


"""

def starpattern(n):
    numbercheck = n
    n=n-1
 
    for i in range(0, numbercheck):
        for j in range(0, n):
            print(end=" ")
     
        n = n - 1

        for j in range(0, i+1):
         
         
            print("* ", end="")
     
        print("\r")

starpattern(6)

