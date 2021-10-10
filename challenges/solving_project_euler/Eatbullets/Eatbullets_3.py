i = 2

def largest_prime_factor(n):
    global i
    while (i**2 < n):
        while (n % i == 0):
            n /= i
        i += 1
    return n

print(largest_prime_factor(600851475143))