""""
made By OPEN MINDS CLUB 
"""

#imports
from pynput.mouse import Button,Controller
import sys
import time

#the typing function 
def write(string): 
    for key in string: # loop throught the caracters of the string 
        if key == ' ': #since the space key is a special object in the pynput library we had to add its condition
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        else: # other than space key we type normaly 
            keyboard.press(key)
            keyboard.release(key)
        time.sleep(0.1) # wait for 0.1 seconds

mouse = Controller() # getting control over the mouse
position = (int(sys.argv[1]),int(sys.argv[2])) #getting the input from the argv
mouse.position = position #positioning the cursor (paste the position here)
mouse.click(Button.left,1) #making to select the box

from pynput.keyboard import Key, Controller
keyboard= Controller() # getting control over the keyboard

#the variable S (paste your text here)
s='paste your text here'
#cleaning the string 
string = s.replace('<section id="word-section">','').replace('<span class="current-word">','').replace('<span>','').replace('</span>',' ').replace('</section>',' ')
write(string) #writing the string