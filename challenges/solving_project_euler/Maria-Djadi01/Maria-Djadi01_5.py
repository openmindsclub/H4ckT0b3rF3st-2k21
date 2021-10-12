def devided(n):
    for i in range(1,20):
        if n % i != 0:
            return False
    return True

i = 0
n = 1
while not devided(n):
    n = n+1

print(n)