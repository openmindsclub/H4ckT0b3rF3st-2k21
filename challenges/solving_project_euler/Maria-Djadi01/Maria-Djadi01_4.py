n = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        x = i * j
        if x > n:
            s = str(i * j)
            if s == s[::-1]:
                n = i * j
print(n)
