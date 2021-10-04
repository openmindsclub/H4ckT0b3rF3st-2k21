from random import randrange

#initializing the position of the princess on one of the edges of the grid randomly 
def PrincessPositionGen():
    i = randrange(4)
    PP = [[0,0],[0,4],[4,0],[4,4]]
    return i, PP[i]