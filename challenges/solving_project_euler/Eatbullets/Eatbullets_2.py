fib = [1, 2]
i = 2

# generate the fibonacci terms
while True:
    t = fib[i-1] + fib[i-2]
    if t < 4000000:
        fib.append(t)
    else:
        break
    i += 1

# find the sum of even terms
sum = 0
for i in fib:
    if i%2==0:
        sum += i

if __name__ == 'main':
    print(fib)
    print(sum)