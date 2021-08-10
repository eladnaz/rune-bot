import pyautogui
import win32gui
import ctypes
import time
from telegram.ext import Updater, CommandHandler
SCREEN_X1 = 0
SCREEN_X2 = 0
SCREEN_Y1 = 0
SCREEN_Y2 = 0
MAPLE_X1 = 0
MAPLE_X2 = 0
MAPLE_Y1 = 0
MAPLE_Y2 = 0
MAPLE_NAME = "Swordie"



SendInput = ctypes.windll.user32.SendInput


UP = 0xC8
DOWN = 0xD0
LEFT = 0xCB
RIGHT = 0xCD
SPACE = 0x39

N = 0x31
LCTRL = 0x1D

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def pressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, 
ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


#------------- WINDOW HANDLERS --------------------#
def getMapleSize():
    maple_win = win32gui.FindWindow(None,MAPLE_NAME)
    MAPLE_X1,MAPLE_Y1,MAPLE_X2,MAPLE_Y2 = win32gui.GetWindowRect(maple_win)
    print(MAPLE_X1)
    print(MAPLE_X2)
    print(MAPLE_Y1)
    print(MAPLE_Y2)

def getScreenSize():
    SCREEN_X2,SCREEN_Y2 = pyautogui.size()


#----------------- LOCATION HANDLERS ------------------#
def findRune():
    rune_status = 1
    rune_loc = 0
    try:
        rune_loc = pyautogui.locateOnScreen('images/minirune.png',confidence=0.65,region=(0,0,330,220))
    except Exception as e:
        rune_status = 0 
        print("Rune not found,",e)
    finally:
        if rune_status == 1:
            return rune_loc.left,rune_loc.top

def findPlayer():
    player_status = 1
    player_loc = 0
    try:
        player_loc = pyautogui.locateOnScreen('images/minime.png',confidence=0.65,region=(0,0,330,220))
    except Exception as e:
        player_status = 0
        print("Player not found",e)
    finally:
        if player_status == 1:
            return player_loc.left, player_loc.top

#----------------PLAYER MOVEMENTS--------------#
def downJump():
    pressKey(DOWN)
    time.sleep(0.5)
    pressKey(SPACE)
    time.sleep(0.5)
    releaseKey(DOWN)
    time.sleep(0.5)
    releaseKey(SPACE)

def ropeLift():
    pressKey(LCTRL)
    time.sleep(0.5)
    releaseKey(LCTRL)

def moveRune():
    #0 = same pos, 1= player right of rune, 2=player left of rune
    player_to_rune = 0 
    playerX,playerY = findPlayer()
    runeX,runeY = findRune()
    interval = 2.0
    if runeX < playerX:
        player_to_rune = 1
    elif runeX > playerX:
        player_to_rune = 2
    if player_to_rune == 2:
        while(playerX < runeX-2):
            if(playerX > runeX-25):
                interval = 0.1
            pressKey(RIGHT)
            time.sleep(interval)
            releaseKey(RIGHT)
            playerX,playerY = findPlayer()
    elif player_to_rune == 1:
        while(playerX > runeX+2):
            if(playerX < playerX+25):
                interval = 0.1
            pressKey(LEFT)
            time.sleep(interval)
            releaseKey(LEFT)
            playerX,playerY = findPlayer()
    time.sleep(0.5)
    while(playerY > runeY+2 or playerY < runeY-2):
        if(playerY < runeY):
            print("rune too low" )
            downJump()
            time.sleep(0.5)
            playerX,playerY = findPlayer()
            print(playerY,runeY)
        elif(playerY > runeY):
            print("rune too high")
            ropeLift()
            time.sleep(3)
            playerX,playerY = findPlayer()
            print(playerY,runeY)

def sendRuneImg():
    pressKey(N)
    time.sleep(0.5)
    releaseKey(N)

def main():
    moveRune()
    time.sleep(0.5)
    sendRuneImg()

if __name__ == "__main__":
    main()