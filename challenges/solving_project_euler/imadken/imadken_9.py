
# We try to solve c = 1000 - a - b


check=0

for a in range(1000//3): #We divise by 3 because a < b < c < 1000

    for b in range(a+1, 1000//2):

        c= 1000 - a - b

        if c*c == a*a + b*b:

            print(f"{a} + {b} + {c} = 1000 ") 
            print(f"product= {c*a*b}")
            
            check=1
            
            break

    if check : break 