def multiples_of_3_or_5():
    sum = 0
    for i in range(1000):
        if i%3==0 or i%5==0:
            sum += i
    return sum

if name == '__main__':
    print(multiples_of_3_or_5())