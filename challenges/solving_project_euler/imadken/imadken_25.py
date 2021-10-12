
def fib():
    
    x = y = 1

    c=2

    while len(str(y)) < 1000:

        x , y = y , y+x

        c += 1

    return c    


print(fib())