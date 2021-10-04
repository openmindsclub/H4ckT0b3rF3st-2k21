from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def start(i, KnightPath):
    root = Tk()
    root.title('Save The Princess Bot')

    #initializing the color of the grid
    backgroungcolor = [['SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace'], 
                    ['SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace'], 
                    ['SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace'], 
                    ['SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace'], 
                    ['SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace', 'SystemButtonFace']]

    #coloring the path that the knight took to save the princess
    for kp in KnightPath:
        backgroungcolor[kp[0]][kp[1]] = '#00FF00'

    #loading the picture of the knight
    KnightImage = Image.open("images\knightImage.png")
    KnightImage  = ImageTk.PhotoImage(KnightImage)

    #loading the picture of the princess
    PrincessImage = Image.open("images\princessImage.png")
    PrincessImage  = ImageTk.PhotoImage(PrincessImage)

    #Positionnig the princess on the grid
    borders = [[None, 7, 14], [None, 7, 14], [None, 7, 14], [None, 7, 14]]
    borders[i] = [PrincessImage, 110, 100]

    # Build our buttons
    b1 = Button(root, height=borders[0][1], width=borders[0][2], bg=backgroungcolor[0][0], image = borders[0][0])
    b2 = Button(root, height=7, width=14, bg=backgroungcolor[0][1])
    b3 = Button(root, height=7, width=14, bg=backgroungcolor[0][2])
    b4 = Button(root, height=7, width=14, bg=backgroungcolor[0][3])
    b5 = Button(root, height=borders[1][1], width=borders[1][2], bg=backgroungcolor[0][4], image = borders[1][0])

    b6 = Button(root, height=7, width=14, bg=backgroungcolor[1][0])
    b7 = Button(root, height=7, width=14, bg=backgroungcolor[1][1])
    b8 = Button(root, height=7, width=14, bg=backgroungcolor[1][2])
    b9 = Button(root, height=7, width=14, bg=backgroungcolor[1][3])
    b10 = Button(root, height=7, width=14, bg=backgroungcolor[1][4])

    b11 = Button(root, height=7, width=14, bg=backgroungcolor[2][0])
    b12 = Button(root, height=7, width=14, bg=backgroungcolor[2][1])
    b13 = Button(root, height=110, width=100, bg=backgroungcolor[2][2], image = KnightImage )
    b14 = Button(root, height=7, width=14, bg=backgroungcolor[2][3])
    b15 = Button(root, height=7, width=14, bg=backgroungcolor[2][4])

    b16 = Button(root, height=7, width=14, bg=backgroungcolor[3][0])
    b17 = Button(root, height=7, width=14, bg=backgroungcolor[3][1])
    b18 = Button(root, height=7, width=14, bg=backgroungcolor[3][2])
    b19 = Button(root, height=7, width=14, bg=backgroungcolor[3][3])
    b20 = Button(root, height=7, width=14, bg=backgroungcolor[3][4])

    b21 = Button(root, height=borders[2][1], width=borders[2][2], bg=backgroungcolor[4][0], image = borders[2][0])
    b22 = Button(root, height=7, width=14, bg=backgroungcolor[4][1])
    b23 = Button(root, height=7, width=14, bg=backgroungcolor[4][2])
    b24 = Button(root, height=7, width=14, bg=backgroungcolor[4][3])
    b25 = Button(root, height=borders[3][1], width=borders[3][2], bg=backgroungcolor[4][4], image =borders[3][0])

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)
    b5.grid(row=0, column=4)

    b6.grid(row=1, column=0)
    b7.grid(row=1, column=1)
    b8.grid(row=1, column=2)
    b9.grid(row=1, column=3)
    b10.grid(row=1, column=4)

    b11.grid(row=2, column=0)
    b12.grid(row=2, column=1)
    b13.grid(row=2, column=2)
    b14.grid(row=2, column=3)
    b15.grid(row=2, column=4)

    b16.grid(row=3, column=0)
    b17.grid(row=3, column=1)
    b18.grid(row=3, column=2)
    b19.grid(row=3, column=3)
    b20.grid(row=3, column=4)

    b21.grid(row=4, column=0)
    b22.grid(row=4, column=1)
    b23.grid(row=4, column=2)
    b24.grid(row=4, column=3)
    b25.grid(row=4, column=4)

    root.mainloop()
