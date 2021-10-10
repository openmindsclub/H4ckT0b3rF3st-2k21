from tkinter import *
import math
from math import sqrt

#define the colors
floral_white="#FEF9EF"
light_blue = "#A2D2FF"
label_color = "#000000"

#define the font
font=("Arial", 30)

#the variable expression will contain the arithmetic expression to calculate
expression=""

#1-the fonction press will be used when we press on a button
def press(button):
    # if the user will press the button "=", we display the result of the expression
    if button=="=":
        calculate()
        return

    #if the user will press the button "C" to delete, the content of the display screen is deleted
    elif button=="C":
        #for this we call the function delete
        delete()
        return

    #otherwise if the user  will press any another button, it will be included in the expression
    global expression

    #the case of x² 
    if button=="x²":
        expression+='²'

    #the case of √x
    elif button=="√x":
        expression+='√'
    
    #the case of any other button
    else:
        expression+=str(button)

    #display the expression
    equation.set(expression)

#2-the function calculate which allows to calculate the result of the expression
def calculate():
    # point out the global expression variable
    global expression
    try:
        # check if there is a square in the expression
        if expression.find("²") != -1: expression = square(expression)

        if expression.find("√") != -1: expression = squareRoot(expression)
         
        #eval function evaluates the expression 
        total=str(eval(expression))
        #update the equation by using set method
        equation.set(total)
        expression=total
    #if an error is generated, then it will be handled by the except block
    except:
        equation.set("erreur")
        expression=""
#Function that calculates the square

def square(expression):
    index = expression.find("²")
    expression = expression.replace(expression[index], "", 1)
    expression = expression[:index] + "*" + \
    expression[index-1] + expression[index::]
    return expression

#Function that calculates the square root

def squareRoot(expression):
    index = expression.find("√")
    expression = expression.replace(expression[index], "", 1)
    expression = expression[:index] + str(sqrt(int(expression[index]))) + expression[index+1:]
    return expression

#3-the function delete which allows you to delete the content of the display screen
def delete():
    global expression
    expression=""
    equation.set("")

#the design part of the calculator's graphical interface
if __name__ == "__main__":
    gui = Tk()

    #background color
    gui.configure(background=floral_white)

    #the title of the application
    gui.title("calculator")

    #window size
    gui.geometry("190x350")

 
    #variable to store content
    equation=StringVar()

    #result box
    result = Label(gui, bg=floral_white, fg=label_color, textvariable=equation, height=2)
    result.grid(columnspan=4)

    #define buttons
    buttons=['C','x²','√x','/',7,8,9,'*',4,5,6,'-',1,2,3,'+',0,'.']


    #add buttons
    row=1
    column=0
    for button in buttons:
          b = Label(gui, text=str(button), bg=light_blue, fg=label_color, height=4, width=6)
          b.bind("<Button-1>", lambda e,bouton=button: press(bouton))
          b.grid(row=row,column= column)
          column+=1
          if column==4:
             column=0
             row+=1


 #add the button =
    b = Label(gui, text="=", bg=floral_white, fg=label_color, height=4, width=12)
    b.bind("<Button-1>", lambda e: calculate())
    b.grid(row=5, column=2, columnspan=2)

#start the GUI
    gui.mainloop()
