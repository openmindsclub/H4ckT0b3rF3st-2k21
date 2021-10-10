def ispalindrome(n):
    return str(n) == str(n)[::-1]

l = []
for first_num in range(100,1000):
    for second_num in range(100,1000):
        prod = first_num * second_num
        if ispalindrome(prod):
            l.append(prod)

print(max(l))