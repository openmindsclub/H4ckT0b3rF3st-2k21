def isPrime(n):
    if n == 1 :
        return False
    if n == 2 :
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def thPrime(n):
    i = 1
    th = 0
    while th != n:
        i += 1
        if isPrime(i):
            th += 1
    print("-------")
    return i


print(thPrime(10001))
