#https://www.youtube.com/watch?v=pNBjC32nisg
import pyautogui as p
from time import sleep
from mouseinfo import mouseInfo
#mouseInfo()



def fazerInclusao():
    for rede in range(45,50):
        for ip in range(1,255):
            p.click(1014,68)
            p.write("172.16.{}.{}".format(rede,ip))
            p.press('enter')
    p.click(1442,68)

fazerInclusao()
