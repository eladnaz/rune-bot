from PIL.Image import NONE
import pyautogui
import win32gui
import ctypes
import time
import sys
import discord
import subprocess
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import configparser
import pygetwindow as pgw
FIREBASE_JSON = {
  "type": "service_account",
  "project_id": "cock-rune",
  "private_key_id": "e60b89da0d048a414ddbc9cd688558e6a1821a52",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+Q7hMsfchaOsc\nELUizGK0HHtCRUwvXeA8QTl7O0vKsAKU98eBaEFQilVkKOtTg3A72hWgIlD4BFuV\nBVcAfMJoooZx1geUBBgSL723QJh5aY9h+lGdFeRjcHYlYHcouXkOUb0kweIhHXUt\n1RZCTv74NGJXTJaSW8BPuRZUQ+6Ei3EG+G7IQ2gh4rJIjPDmzTWK1SggynX28UI4\n2huNWRm2DwJieLsYroopg+qqXdUAoNnTCEFlDH2IZLJ0ad0htWCyLbGnRx7Lja84\n45k+MPBGiN3EQnrssygNoeCjhJk7VIf71jXhcJtdCUHzBPd4eWZa5VLh5r17AE/x\n7FG4HdLxAgMBAAECggEACLY/b0eWKhyh6Kg9MF7icB5+aFjq9Z+bSmGu2PKB9Gxz\nGdDEp6tsk4cEr5rjYkYPnWCi19u/uwjcC//xbWTJCWh+YSJXONL9KoFZcwAisICB\ntQ9KAw2DESiPna4ulpnzgzvWk3h15bqcaHZW2BTCPlQ2YoqaZGY4xo2834E4H9p8\nZ4Gho8B7tVOVnn+z8AdCXCra1xTYPLC4a2q/DO7spMmp60ZhC5Nl209tmSMnIKuL\nSXg10yk+BgCVfx0IqtpzIfzYYG4ISIcgc7CRSfDiQUeUaWIEOd4Aj6J77UBq+E0i\napyCaPoGLXvd0edDXYx19tYh9PLl7VuTEEBge4+PVwKBgQDvJ1rQnZydtmz4+/c3\nJIixFYPXxJ5fgUuahTrIOOum6Kx87guMkq0+pdk6TYOqyy/qKIsQE0aPkGXIgZQA\n7eWDZkOdE5vnq28yG/Ki0YO7BzGgaVecGTDHaNLxgMbwtyCVFL0uk4vO2Mv15bnD\nX9Dk+oFPwtxJJH6HyMpetpszOwKBgQDLqr/FmpTdZzZJWgIEdMaGTHbkZFT7Enpv\ntmxl/04MRTud32+rylCCv6+sUbKoe2xOAMer2Wjl25Bzw4ALDAiRbuSpGxsJv/RR\nrXuJJGPwUUi8JIZET9tnfD1gXTg6tEe8fzJrqHSeJmxrQJJtp1p5ciB277TUD9sx\nbvMNNyqXwwKBgHKueZMecZMDfuAq25K61z2r5oxageOked/AUb7f5MkmPEiwUiN3\n1tH6799Qeno1c2WjSYRM6gJAKT7sPE/xxKStLnEtjQ6cG/d4hXLka3oNahPVUCjP\nv59wOe+LZFrcRiiXSF0Ebf+j4LKrFdiFowOayNW5yK7ebDqq47hlcqkvAoGBAJ+y\nV4TeXPPuRkbl6McNucz8kA0uDuR/7LlD1WN0+QHuF30HAk016kNbgqgft3MctCPF\nwMsjQnlZ3L6pAPGokd9XkLx4oI7YkP6qhT9X5XU+h0XfbdiKtYNDi+zPq5N8YPOQ\n2TxJbofDoSfIDgklPHAV6RbZhnTxqfHtCW/HXgJ5AoGBAJ5J27yDjBvGBewogtgt\nRZ3XWEvhLDovALNpKein3AlnErEo7lkzorlMXon+u5NZ2qFJjFuNTbuKek3La1Ap\ne8iVxaIl9JnRaIFHeMZzhFcz+9ODydIHgbxbx8u2KMulX/uwL+r1LxvGKbSS5+qE\ncPPadeItZqTXsn5wE6Z8Ba8P\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-2h2l4@cock-rune.iam.gserviceaccount.com",
  "client_id": "102033677986236482170",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2h2l4%40cock-rune.iam.gserviceaccount.com"
}
MAPLE_NAME = ''
PLAYERX_SAVED = 0
PLAYERY_SAVED = 0
RUNE_EXIST = False
BOT_STATUS = 0
CHANNEL_ID = ""
ROPE_LIFT = ""
JUMP = ""
INTERACT = ""
PLAY_PAUSE = ""
MACRO_HYBRID = ""
client = discord.Client()
BOT_TOKEN =''
CURRENT_USER = ''
APP_AUTH = ''
MAPLE_WIN = None
KEYSCAN_DICT = {'LCTRL':0x1D,
             'MINUS':0x0C,
             'EQUAL':0x0D,
             'P':0x19,
             'F':0x21,
             'Q':0x10,
             'LALT':0x38,
             'SPACE':0x39,
             'N':0x31,
             'Y':0x15,
             'F9':0x43,
             'F10':0x44,
             'F11':0x57,
             'F12':0x58}

MACRO_DICT = {'LCTRL':'ctrlleft',
             'MINUS':'-',
             'EQUAL':'=',
             'SPACE':'space',
             'P':'p',
             'F':'f',
             'Q':'q',
             'LALT':'altleft',
             'N':'n',
             'Y':'y',
             'F9':'f9',
             'F10':'f10',
             'F11':'f11',
             'F12':'f12'}

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except Exception as e:
    sys.exit()
finally:
    MAPLE_NAME = config['USER']['MAPLE_NAME']
    BOT_TOKEN = config['USER']['BOT_TOKEN']
    CHANNEL_ID = config['USER']['CHANNEL_ID']
    CURRENT_USER = config['USER']['CURRENT']
    APP_AUTH = config['USER']['AUTH_CODE']
    ROPE_LIFT = config['USER']['ROPE_LIFT']
    JUMP = config['USER']['JUMP']
    INTERACT = config['USER']['INTERACT']
    PLAY_PAUSE = config['USER']['PLAY_PAUSE']
    MACRO_HYBRID = config['USER']['MACRO_HYBRID']

bot = commands.Bot(command_prefix=CURRENT_USER)

SendInput = ctypes.windll.user32.SendInput

# initializate AUTHENTICATION
cred = credentials.Certificate(FIREBASE_JSON)
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('authenusers')
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

docs = doc_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict()))
    print(APP_AUTH)
    if APP_AUTH ==doc.id:
        #print ('authenticated')
        #print ('hwid')
        set_ref = db.collection('authenusers').document(doc.id)
        set_ref.set({
            'hwid':hwid
        })
        log_ref = db.collection('logs')
        log_ref.add({
            'authencode':APP_AUTH,
            'hwid':hwid,
            'datetime':firestore.SERVER_TIMESTAMP
        })
        break
    else:
        print('ure a fucker')
        logfailentry_ref = db.collection('failedlogs')
        logfailentry_ref.add({
            'authencode':APP_AUTH,
            'hwid':hwid,
            'datetime':firestore.SERVER_TIMESTAMP
        })
        sys.exit()

MAPLE_WIN = pgw.getWindowsWithTitle(MAPLE_NAME)[0]
MAPLE_WIN.moveTo(0,0)

UP = 0xC8
DOWN = 0xD0
LEFT = 0xCB
RIGHT = 0xCD

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
        rune_loc = pyautogui.locateOnScreen('images/minirunev3.png',confidence=0.8,region=(0,0,330,220))
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
        player_loc = pyautogui.locateOnScreen('images/minimev3.png',confidence=0.8,region=(0,0,330,220))
    except Exception as e:
        player_status = 0
        print("Player not found",e)
    finally:
        if player_status == 1:
            return player_loc.left, player_loc.top

#----------------PLAYER MOVEMENTS--------------#
def downJump():
    print(KEYSCAN_DICT[JUMP])
    key = KEYSCAN_DICT[JUMP]
    pressKey(DOWN)
    time.sleep(0.5)
    pressKey(key)
    time.sleep(0.5)
    releaseKey(DOWN)
    time.sleep(0.5)
    releaseKey(key)

def ropeLift():
    key = KEYSCAN_DICT[ROPE_LIFT]
    pressKey(key)
    time.sleep(0.5)
    releaseKey(key)

def flashJump():
    print(KEYSCAN_DICT[JUMP])
    key = KEYSCAN_DICT[JUMP]
    pressKey(key)
    time.sleep(0.1)
    releaseKey(key)

def moveRune():
    #0 = same pos, 1= player right of rune, 2=player left of rune
    goToFloor()
    player_to_rune = 0 
    playerX,playerY = findPlayer()
    runeX,runeY = findRune()
    if runeX < playerX:
        player_to_rune = 1
    elif runeX > playerX:
        player_to_rune = 2
    if player_to_rune == 2:
        while(playerX < runeX-2):
            pressKey(RIGHT)
            if not (playerX > runeX-25):
                flashJump()
            playerX,playerY = findPlayer()
        releaseKey(RIGHT)
    elif player_to_rune == 1:
        while(playerX > runeX+2):
            pressKey(LEFT)
            if not (playerX < playerX+25):
                flashJump()
            playerX,playerY = findPlayer()
        releaseKey(LEFT)
    time.sleep(0.5)
    while(playerY > runeY+2 or playerY < runeY-2):
        if(playerY < runeY):
            downJump()
            time.sleep(0.5)
            playerX,playerY = findPlayer()
        elif(playerY > runeY):
            ropeLift()
            time.sleep(3)
            playerX,playerY = findPlayer()
    print("rune reached")

def returnToPosition():
    print("going back")
    global RUNE_EXIST
    goToFloor()
        #0 = same pos, 1= player right of rune, 2=player left of rune
    player_to_saved = 0 
    playerX,playerY = findPlayer()
    if PLAYERX_SAVED < playerX:
        player_to_saved = 1
    elif PLAYERX_SAVED > playerX:
        player_to_saved = 2
    if player_to_saved == 2:
        while(playerX < PLAYERX_SAVED-2):
            pressKey(RIGHT)
            print(playerX,PLAYERX_SAVED)
            if not (playerX > PLAYERX_SAVED-25): 
                flashJump()
            playerX,playerY = findPlayer()
        releaseKey(RIGHT)
        pressKey(LEFT)
        time.sleep(0.1)
        releaseKey(LEFT)
    elif player_to_saved == 1:
        while(playerX > PLAYERX_SAVED+2):
            print(playerX,PLAYERX_SAVED)
            pressKey(LEFT)
            if not (playerX < PLAYERX_SAVED+25):
                flashJump()
            playerX,playerY = findPlayer()
        releaseKey(LEFT)
        pressKey(RIGHT)
        time.sleep(0.1)
        releaseKey(RIGHT)
    time.sleep(0.5)
    while(playerY > PLAYERY_SAVED+2 or playerY < PLAYERY_SAVED-2):
        if(playerY < PLAYERY_SAVED+2):
            downJump()
            time.sleep(0.5)
            playerX,playerY = findPlayer()
        elif(playerY > PLAYERY_SAVED-2):
            ropeLift()
            time.sleep(3)
            playerX,playerY = findPlayer()
    RUNE_EXIST = 0
    time.sleep(0.5)
    toggleMacro()

def pressRune():
    key = KEYSCAN_DICT[INTERACT]
    pressKey(key)
    time.sleep(0.5)
    releaseKey(key)
    #captureimg(chatid,'dorune')

def goToFloor():
    while(True):
        playerX,playerY = findPlayer()
        downJump()
        newPlayerX,newPlayerY = findPlayer()
        if(playerY == newPlayerY):
            break

def convertaction(action):
    if(action == 'R') :
        return RIGHT

    elif(action =='L'):
         return LEFT
    
    elif(action =='U'):
         return UP
    
    elif(action =='D'):
         return DOWN


def main():
    global PLAYERX_SAVED
    global PLAYERY_SAVED
    global RUNE_EXIST
    PLAYERX_SAVED,PLAYERY_SAVED = findPlayer()
    sleepTime = 1
    while(BOT_STATUS == 1):
        if(RUNE_EXIST == 1):
            sleepTime = 1
        else:
            sleepTime = 1
        time.sleep(sleepTime)
        if(findRune() != None):
            RUNE_EXIST = 1
            toggleMacro()
            time.sleep(0.5)
            moveRune()
            time.sleep(0.5)
            pressRune()

def toggleMacro():
    key = MACRO_DICT[PLAY_PAUSE]
    if(MACRO_HYBRID == "TRUE"):
        keyArr = PLAY_PAUSE.split("+")
        keyOne = MACRO_DICT[keyArr[0]]
        keyTwo = MACRO_DICT[keyArr[1]]
        pyautogui.hotkey(keyOne,keyTwo)
    else:
        pyautogui.keyDown(key)
        time.sleep(0.5) #to be made adaptive
        pyautogui.keyUp(key)

    
#------------- DISCORD Region --------------------#
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.get_channel(int(CHANNEL_ID)).send("bot is online")
    await bot.get_channel(int(CHANNEL_ID)).send(file=discord.File('images/captureimg.png'))

@bot.command(name='lanjiao')
async def discordlanjiao(ctx):
    myScreenshot= pyautogui.screenshot('images/captureimg.png')
    await ctx.send(file=discord.File('images/captureimg.png'))

@bot.command(name='start')
async def discordstart(ctx):
    global BOT_STATUS
    await ctx.send('RuneBot is starting for '+CURRENT_USER)
    BOT_STATUS = 1
    try: 
        main()
    except Exception as e:
        if hasattr(e,'message'):
            print(e.message)
        else:
            print('fucking failed')
            print(e)
    finally:
        myScreenshot= pyautogui.screenshot('images/captureimg.png')
        await ctx.send(file=discord.File('images/captureimg.png'))
        await ctx.send("Please input the following, based on the arrow keys: UP - U, Down - D, Left - L, Right - R")
        await ctx.send("Example, kotorisolve R R L L")

@bot.command(name='dorune')
async def discorddorune(ctx):
    await ctx.send("Opening Rune...")
    pressRune()
    myScreenshot= pyautogui.screenshot('images/captureimg.png')
    await ctx.send(file=discord.File('images/captureimg.png'))
    await ctx.send("Please input the following, based on the arrow keys: UP - U, Down - D, Left - L, Right - R")
    await ctx.send("Example, kotorisolve R R L L")

@bot.command(name='done')
async def discorddone(ctx):
    global RUNE_EXIST
    await ctx.send("Returning to position")
    returnToPosition()
    myScreenshot= pyautogui.screenshot('images/captureimg.png')
    await ctx.send(file=discord.File('images/captureimg.png'))
    RUNE_EXIST = 0

@bot.command(name='solve')
async def discordsolve(ctx,arg1,arg2,arg3,arg4):
    try:
        action1=str(arg1)
        action2=str(arg2)
        action3=str(arg3)
        action4=str(arg4)
        result = action1+action2+action3+action4
        await ctx.send(result)
        
        pressKey(convertaction(action1))
        time.sleep(0.3)
        releaseKey(convertaction(action1))

        pressKey(convertaction(action2))
        time.sleep(0.3)
        releaseKey(convertaction(action2))

        pressKey(convertaction(action3))
        time.sleep(0.3)
        releaseKey(convertaction(action3))

        pressKey(convertaction(action4))
        time.sleep(0.3)
        releaseKey(convertaction(action4))
        time.sleep(0.5)
        
        myScreenshot= pyautogui.screenshot('images/captureimg.png')
        await ctx.send(file=discord.File('images/captureimg.png'))
        await ctx.send("Please check if the rune has been solved. If not, run <ign>dorune again.")
        await ctx.send("If rune is solved, type <ign>done to go back to position")

    except(IndexError,ValueError):
        await ctx.send('wrong input, Example, shinobu R R L L')

@bot.command(name='positionalright')
async def discordpositionalfix(ctx):
    await ctx.send("Repositioning to the right")
    #epositionright()
    myScreenshot= pyautogui.screenshot('images/captureimg.png')
    await ctx.send(file=discord.File('images/captureimg.png'))
    await ctx.send('back in position')

@bot.command(name='positionalleft')
async def discordpositionalfix(ctx):
    await ctx.send("Repositioning to the left")
    #repositionleft()
    myScreenshot= pyautogui.screenshot('images/captureimg.png')
    await ctx.send(file=discord.File('images/captureimg.png'))
    await ctx.send('back in position')

bot.run(BOT_TOKEN)
#------------- DISCORD Region --------------------#


