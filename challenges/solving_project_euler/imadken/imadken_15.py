
import math

def Lattice_Paths(n):

    # We notice that number of ups == number of downs == n
    #So it's like how many possibilities to have n (ups | downs) from 2n
    #we use this formula : n!/p!(n-p)!


    return math.factorial(2 * n) // (math.factorial(n) ** 2)   




print(Lattice_Paths(20))