naturelNumbersList = list(range(1,1000))
multiples= 0

for number in naturelNumbersList:
    if number % 3 == 0 or number % 5 == 0:
        multiples += number

print(multiples)
