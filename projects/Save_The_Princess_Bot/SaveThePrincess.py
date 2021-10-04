from initialization.UI import start
from initialization.PrincessPosition import PrincessPositionGen

# Princess contains the position of the princess in the grid 
# i contains a value necessary for the UI don't worry about it 
i, Princess = PrincessPositionGen()

#Knight contains the initial position of the knight in the grid you can't change it
Knight = (2,2)

#this function find the shortest path to save the princess by calculating euclidian distance 
def FindThePath():
    #convert the tuple to a list so we can move the knight on th grid
    Kp = list(Knight)
    #We Copy the position of the princess to not interfer with the intial position
    Pp = Princess.copy()
    #PTP (Path To the Princess) a list that will contain all the case of the grid that knight came across to reach the princess
    PTP = [Kp.copy()]

    while Pp != Kp:
        #the list testPath will contain the euclidian between the knight and the princess 
        #the euclidian distance will be calculated after supposing that the knight moved to right, left, top and bottom 
        testPath = []
        testPath.append(((((Pp[0] - (Kp[0]+1) )**2) + ((Pp[1]-Kp[1])**2) )**0.5))
        testPath.append(((((Pp[0] - (Kp[0]-1) )**2) + ((Pp[1]-Kp[1])**2) )**0.5))
        testPath.append(((((Pp[0] - Kp[0] )**2) + ((Pp[1]-(Kp[1]+1))**2) )**0.5))
        testPath.append(((((Pp[0] - Kp[0] )**2) + ((Pp[1]-(Kp[1]-1))**2) )**0.5))
        
        #after that we find the shortest distance
        index = 0
        min = testPath[0]
        for i in range(4):
            if testPath[i]<=min:
                min=testPath[i]
                index=i
        #if the shortest distance was after going to the top we go up
        if index == 0:
            Kp[0]+=1
        #if the shortest distance was after going to the bottom we go down
        elif index == 1:
            Kp[0]-=1
        #if the shortest distance was after going to the right we go right
        elif index == 2:
            Kp[1]+=1
        #if the shortest distance was after going to the left we go left
        elif index == 3:
            Kp[1]-=1
        
        #we save the knight current position
        PTP.append(Kp.copy())
    return PTP

def YourFunction():
    path = []
    #your code
    return path

#After finishing your function replace FindThePath by the name of your Function
start(i,FindThePath())
