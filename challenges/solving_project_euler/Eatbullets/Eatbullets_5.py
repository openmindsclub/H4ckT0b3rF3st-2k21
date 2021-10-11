from collections import Counter

primes_below_20 = [2, 3, 5, 7, 11, 13, 17, 19]

def prime_factors(n):
    if n == 1:
        return []
    for prime in primes_below_20:
        if n % prime == 0:
            return [prime] + prime_factors(n / prime)

primes_needed = Counter()

for n in range(2, 21):
     primes = Counter(prime_factors(n))
     primes_needed = primes_needed | primes  # | gives the max of existing values

total = 1
for prime, amount in primes_needed.items():
    total *= prime ** amount

print(total)