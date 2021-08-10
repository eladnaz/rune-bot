import pyautogui as gui
import win32gui
MAPLE_X1 = 0
MAPLE_X2 = 0
MAPLE_Y1 = 0
MAPLE_Y2 = 0
MAPLE_NAME = "Swordie"

def getMapleSize():
    maple_win = win32gui.FindWindow(None,MAPLE_NAME)
    MAPLE_X1,MAPLE_Y1,MAPLE_X2,MAPLE_Y2 = win32gui.GetWindowRect(maple_win)
    print(MAPLE_X1)
    print(MAPLE_X2)
    print(MAPLE_Y1)
    print(MAPLE_Y2)

getMapleSize()