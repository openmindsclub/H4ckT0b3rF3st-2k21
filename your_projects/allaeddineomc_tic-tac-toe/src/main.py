#! "/usr/bin/python3"

#imports needed by some functions to work
import random

#just reference for the names and position of the 9 slots of the tic-tac-toe matrix
'''
a b c
d e f
g h i
'''

# the slot class is not very different from the string class but it allows only some specific values to be inserted
class slot():
    def __init__(self):
        self.content = str
        self.content = "empty"
    def setcontent(self,content):
        if content == ("x" or "X"):
            self.content = "x"
        if content == ("o" or "O"):
            self.content = "o"
    def getcontent(self):
        return self.content

#declaring the slots in alphabetical order

a=slot()
b=slot()
c=slot()
d=slot()
e=slot()
f=slot()
g=slot()
h=slot()
i=slot()
slots = [a,b,c,d,e,f,g,h,i]

# straights is a list containing the possible straight lines that the first one to complete one of these will be winner
straights = [[a,b,c],[d,e,f],[g,h,i],[a,d,g],[b,e,h],[c,f,i],[a,e,i],[g,e,c]]
# state is the variable that tells the main function weather it's the player's or the robot's turn and takes either "x" or "o" as a value
state = "x"
#playerrole is the variable that determins what role the player will take and it should be either "x" or "o" for the game to start
playerrole = "empty"
#robot is the function that have the main functionality of the bot that plays aginst the player 
def robot():
    #first , the function takes the global values that it needs to operate
    global robotrole
    global playerrole
    global state
    #the function checks if every slot is empty which means the robot will be the first to play
    if (a.getcontent() == "empty")&(b.getcontent() == "empty")&(c.getcontent() == "empty")&(d.getcontent() == "empty")&(e.getcontent() == "empty")&(f.getcontent() == "empty")&(g.getcontent() == "empty")&(h.getcontent() == "empty")&(i.getcontent() == "empty") :
        #in this case it will do a random move so the game won't be so repetitive 
        writeon = random.randint(0,8)
        slots[writeon].setcontent(robotrole)
        #than it sets the state to playerrole which should be "o" in this case so in the next loop of the main function the player gets to choose a slot
        state = playerrole
    #otherwise it checks if it's the role for the bot , i nthis case it will alwais be the role for the bot because if it was the players role it won't even get to this point so it's pointless but it works
    elif state==robotrole :
        #in this case it will look for straight lines that require only a last move for the bot to win 
        for straight in range(len(straights)) :
            dangerlevel = 0
            for readon in range(len(straights[straight])) :
                if straights[straight][readon].content == robotrole:
                    dangerlevel = dangerlevel -1
                    #in this case it will look for straight lines that require only a last move for the bot to win 
                    if dangerlevel == -2 :
                        #if it finds any it will call the call the close function and the bot wins
                        close (straight)
                        break
                    if dangerlevel == 2 :
                        close (straight)
                        break
                    elif (straight == 7) & (readon==2) : 
                        randommove()
                        break
                #otherwise it will check for straight lines that the player need only one move to finish and calls the close function on them to stop the player from having an easy win
                if straights[straight][readon].content == playerrole:
                    dangerlevel = dangerlevel +1
                    if dangerlevel == -2 :
                        close (straight)
                        break
                    if dangerlevel == 2 :
                        close (straight)
                        break
                    # if it doesn't find any of the these it will take a random move
                    elif (straight == 7) & (readon==2) :
                        randommove()
                        break
# the close function is a function that the bot uses to find the hole in a line so it can close it to either win or stop the player from winning
def close(straight):
    global state
    for readon in range(len(straights[straight])):
        if straights[straight][readon].content == "empty":
            straights[straight][readon].setcontent(robotrole)
            state = playerrole
            break
#the random move function is a function that the bot uses to make sure it won't overwrite a used slot when it decides to choose a slot randomly , the function need a better rewrite
def randommove():
    global slots
    global state
    writeon = random.randint(0,8)
    if slots[writeon].content == "empty" :
        slots[writeon].setcontent(robotrole)
        state = playerrole
    else :
        randommove()
#the player function is the function that main calls when it's the player turn , it checks if the slot the player choosed is empty so it lets them take it , otherwise it will ask to choose another slot, this function is horribly coded and need a complete rewrite 
def player():
    global robotrole
    global playerrole
    global state
    state = robotrole
    writeon = input('play on slot a,b,c,d,e,f,g,h,i ? select an empty slot ...'  )
    if writeon == "a":
        if a.content == "empty":
            a.setcontent(playerrole)
        else :
            print ("slot a not empty")
            player()
    elif writeon == "b":
        if b.content == "empty":
            b.setcontent(playerrole)
        else :
            print ("slot b not empty")
            player()
    elif writeon == "c":
        if c.content == "empty":
            c.setcontent(playerrole)
        else :
            print ("slot c not empty")
            player()
    elif writeon == "d":
        if d.content == "empty":
            d.setcontent(playerrole)
        else :
            print ("slot d not empty")
            player()
    elif writeon == "e":
        if e.content == "empty":
            e.setcontent(playerrole)
        else :
            print ("slot e not empty")
            player()
    elif writeon == "f":
        if f.content == "empty":
            f.setcontent(playerrole)
        else :
            print ("slot f not empty")
            player()
    elif writeon == "g":
        if g.content == "empty":
            g.setcontent(playerrole)
        else :
            print ("slot g not empty")
            player()
    elif writeon == "h":
        if h.content == "empty":
            h.setcontent(playerrole)
        else :
            print ("slot h not empty")
            player()
    elif writeon == "i":
        if i.content == "empty":
            i.setcontent(playerrole)
        else :
            print ("slot i not empty")
            player()
    else :
        print ("slot "+ writeon + " does not exist")
        player()
#roles is the first function to be called by main , it's job is to let the player choose either "x" or "o" and informs them that "x will always be the fist to play" 
def roles():
    global robotrole
    global playerrole
    playerrole = input("player uses x or o ?  x always plays first ... : ")
    if playerrole == "x":
        robotrole = "o"
    elif playerrole == "o":
        robotrole = "x"
    else :
        print("choose x or o")
        roles()
# show is the function responsible of showing what's going on in the board ' it will be great if someone replaces it with a GUI
def show():
    print ("["+a.content+"]["+b.content+"]["+c.content+"]")
    print ("["+d.content+"]["+e.content+"]["+f.content+"]")
    print ("["+g.content+"]["+h.content+"]["+i.content+"]")
# the main function , it will tell the player or the boot to pick a slot intercahngeably and checks if there is a winner every loop by checking if any straight line is full of the symbol of the robot or the player 
def main():
    global state
    global playerrole
    global robotrole
    while True:
        draw = 0
        if playerrole=="empty":
            roles()
            show()
        if state == robotrole :
            robot()
            show()
        elif state == playerrole :
            player()
            show()
        for checker in range (len (straights)) :
            winlevel = 0
            for halfchecker in range(len (straights[checker])):
                if straights[checker][halfchecker].content == playerrole :
                    winlevel = winlevel +1
                if straights[checker][halfchecker].content == robotrole :
                    winlevel = winlevel -1
            if winlevel == 3 :
                print ("you win")
                break
            if winlevel == -3 :
                print (" loooooooooser :p ")
                break
        for checker in range(len(slots)) :
            if slots[checker].content=="empty":
                draw = draw +1
                if draw == 9 :
                    print (draw)
                    break

#program start
main()
#program end
