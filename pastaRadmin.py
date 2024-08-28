import pyautogui as p
from time import sleep
from mouseinfo import mouseInfo
mouseInfo()


p.click(1365,9)

for x in range(1,255):
    
    p.press('F7')
    p.write("{}".format(x))
    p.press('enter')
    
