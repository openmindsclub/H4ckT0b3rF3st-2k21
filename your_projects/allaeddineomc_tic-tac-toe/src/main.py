import random
'''
a b c
d e f
g h i
'''
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
straights = [[a,b,c],[d,e,f],[g,h,i],[a,d,g],[b,e,h],[c,f,i],[a,e,i],[g,e,c]]
state = "x"
playerrole = "empty"

def robot():
    global robotrole
    global playerrole
    global state
    if (a.getcontent() == "empty")&(b.getcontent() == "empty")&(c.getcontent() == "empty")&(d.getcontent() == "empty")&(e.getcontent() == "empty")&(f.getcontent() == "empty")&(g.getcontent() == "empty")&(h.getcontent() == "empty")&(i.getcontent() == "empty") :
        writeon = random.randint(0,8)
        slots[writeon].setcontent(robotrole)
        state = playerrole
    elif state==robotrole :
        for straight in range(len(straights)) :
            dangerlevel = 0
            for readon in range(len(straights[straight])) :
                if straights[straight][readon].content == robotrole:
                    dangerlevel = dangerlevel -1
                    if dangerlevel == -2 :
                        close (straight)
                        break
                    if dangerlevel == 2 :
                        close (straight)
                        break
                    elif (straight == 7) & (readon==2) :
                        randommove()
                        break
                if straights[straight][readon].content == playerrole:
                    dangerlevel = dangerlevel +1
                    if dangerlevel == -2 :
                        close (straight)
                        break
                    if dangerlevel == 2 :
                        close (straight)
                        break
                    elif (straight == 7) & (readon==2) :
                        randommove()
                        break
def close(straight):
    global state
    for readon in range(len(straights[straight])):
        if straights[straight][readon].content == "empty":
            straights[straight][readon].setcontent(robotrole)
            state = playerrole
            break
def randommove():
    global slots
    global state
    writeon = random.randint(0,8)
    if slots[writeon].content == "empty" :
        slots[writeon].setcontent(robotrole)
        state = playerrole
    else :
        randommove()
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
def show():
    print ("["+a.content+"]["+b.content+"]["+c.content+"]")
    print ("["+d.content+"]["+e.content+"]["+f.content+"]")
    print ("["+g.content+"]["+h.content+"]["+i.content+"]")
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
def debug():
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
main()
#debug()
