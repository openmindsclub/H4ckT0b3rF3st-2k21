""""
made By OPEN MINDS CLUB 
"""

#imports
from pynput.mouse import Button,Controller 
import sys
import time

position = (int(sys.argv[1]),int(sys.argv[2])) #getting the input from the argv
mouse.position = position #positioning the cursor (paste the position here) #
timer = 30 #specified time

wanted_speed = 100 #

nb_clicks = timer*wanted_speed

sleeptime= timer/nb_clicks
for i in range(nb_clicks):
    mouse.click(Button.left,1)
    time.sleep(sleeptime)