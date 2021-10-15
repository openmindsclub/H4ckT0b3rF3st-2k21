def sum_of_squares(n):
    return n*(n+1)*(2*n+1)/6

def square_of_sum(n): # AP
    sum = n*(n+1)/2
    return sum**2

diff = abs(square_of_sum(100) - sum_of_squares(100))
print(diff)