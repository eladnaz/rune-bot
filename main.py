from discord import player
import pyautogui
import PIL.ImageGrab as grab
import PIL.ImageDraw as draw
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
BOT_TOKEN =''
CURRENT_USER = ''
APP_AUTH = ''
USER_MENTION = ''
TIME_INTERVAL = ''
MAPLE_WIN = None
RUNEY = 0
RUNEX = 0
PLAYERX = 0
PLAYERY = 0
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
print("Reading Config")
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
    TIME_INTERVAL = config['USER']['TIME_INTERVAL']
    RE_FACE = config['USER']['RE_FACE']
    USER_MENTION = '<@' + config['USER']['USER_MENTION'] + '>'

if BOT_STATUS == 0:
    client = discord.Client()
    bot = commands.Bot(command_prefix=CURRENT_USER)

SendInput = ctypes.windll.user32.SendInput
print("Attempting Authentication")
# initializate AUTHENTICATION
cred = credentials.Certificate(FIREBASE_JSON)
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('authenusers')
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

docs = doc_ref.stream()
exit_status = 1
for doc in docs:
    if APP_AUTH==doc.id:
        db.collection('authenusers').document(doc.id)
        exit_status = 0
        set_ref = db.collection('authenusers').document(doc.id)
        set_ref.set({
            'hwid':hwid
        })
        if (doc.get('hwid')!=None):
            if (doc.get('hwid') != hwid):
                dupeset_ref = db.collection('authenusers').document(doc.id)
                dupeset_ref.set({
                'hwid': doc.get('hwid'),
                'hwidduper':hwid
                })
                print('ure a slut')
                sys.exit()

        log_ref = db.collection('logs')
        log_ref.add({
            'authencode':APP_AUTH,
            'hwid':hwid,
            'datetime':firestore.SERVER_TIMESTAMP
        })
        break

if(exit_status == 1):
    print('ure a fucker')
    logfailentry_ref = db.collection('failedlogs')
    logfailentry_ref.add({
            'authencode':APP_AUTH,
            'hwid':hwid,
            'datetime':firestore.SERVER_TIMESTAMP
        })
    sys.exit()

print("Authenticated")
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
def checkNumLock():
    hllDll = ctypes.WinDLL("User32.dll")
    NUM_KEY = 0x90
    if hllDll.GetKeyState(NUM_KEY) == 1:
        pyautogui.press('numlock')
    

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


#----------------- LOCATION HANDLERS ------------------#
def findRune():
    global RUNE_EXIST
    global RUNEX
    global RUNEY
    image = grab.grab(bbox=(0,0,330,220))
    pixels = image.load()
    width,height = image.size
    for y in range(height):
        for x in range(width):
            if pixels[x,y] == (221,102,255):
                RUNE_EXIST = 1
                break
        if RUNE_EXIST == 1:
            RUNEX = x
            RUNEY = y
            break
    image.close()
    del image
    del pixels
    


def findPlayer(mode=0):
    global PLAYERX
    global PLAYERY
    global PLAYERX_SAVED
    global PLAYERY_SAVED
    image = grab.grab(bbox=(0,0,330,220))
    pixels = image.load()
    width,height = image.size
    player_found = 0
    for y in range(height):
        for x in range(width):
            if pixels[x,y] == (255,221,68):
                player_found = 1
                break
        if player_found == 1:
            if mode == 1:
                PLAYERX_SAVED = x
                PLAYERY_SAVED = y
            else:
                PLAYERX = x
                PLAYERY = y
            break
    image.close()
    del image
    del pixels

#----------------PLAYER MOVEMENTS--------------#
def downJump():
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
    key = KEYSCAN_DICT[JUMP]
    pressKey(key)
    time.sleep(0.1)
    releaseKey(key)

async def moveRune():
    #0 = same pos, 1= player right of rune, 2=player left of rune
    goToFloor()
    player_to_rune = 0 
    findPlayer()
    if RUNEX < PLAYERX:
        player_to_rune = 1
    elif RUNEX > PLAYERX:
        player_to_rune = 2
    if player_to_rune == 2:
        while(PLAYERX < RUNEX-2):
            pressKey(RIGHT)
            if not (PLAYERX > RUNEX-25):
                flashJump()
            findPlayer()
        releaseKey(RIGHT)
    elif player_to_rune == 1:
        while(PLAYERX > RUNEX+2):
            pressKey(LEFT)
            if not (PLAYERX < RUNEX+25):
                flashJump()
            findPlayer()
        releaseKey(LEFT)
    time.sleep(0.5)
    while(PLAYERY > RUNEY+3 or PLAYERY < RUNEY-3):
        if(PLAYERY < RUNEY):
            downJump()
            time.sleep(0.5)
            findPlayer()
        elif(PLAYERY > RUNEY):
            ropeLift()
            time.sleep(3)
            findPlayer()
    print("Reached the rune!")
    await discordsendrune()

def returnToPosition():
    print("Going back to position")
    global RUNE_EXIST
    goToFloor()
        #0 = same pos, 1= player right of rune, 2=player left of rune
    player_to_saved = 0 
    findPlayer()
    if PLAYERX_SAVED < PLAYERX:
        player_to_saved = 1
    elif PLAYERX_SAVED > PLAYERX:
        player_to_saved = 2
    if player_to_saved == 2:
        while(PLAYERX < PLAYERX_SAVED-1):
            pressKey(RIGHT)
            if(PLAYERX < PLAYERX_SAVED-25): 
                flashJump()
            findPlayer()
        releaseKey(RIGHT)
        if RE_FACE == "YES":
            pressKey(LEFT)
            time.sleep(0.1)
            releaseKey(LEFT)
    elif player_to_saved == 1:
        while(PLAYERX > PLAYERX_SAVED+1):
            pressKey(LEFT)
            if(PLAYERX > PLAYERX_SAVED+25):
                flashJump()
            findPlayer()
        releaseKey(LEFT)
        if RE_FACE == "YES":
            pressKey(RIGHT)
            time.sleep(0.1)
            releaseKey(RIGHT)
    time.sleep(0.5)
    while(PLAYERY > PLAYERY_SAVED+3 or PLAYERY < PLAYERY_SAVED-3):
        if(PLAYERY < PLAYERY_SAVED+3):
            downJump()
            time.sleep(0.5)
            findPlayer()
        elif(PLAYERY > PLAYERY_SAVED-3):
            ropeLift()
            time.sleep(3)
            findPlayer()
    RUNE_EXIST = 0
    time.sleep(0.5)
    toggleMacro()

def pressRune():
    key = KEYSCAN_DICT[INTERACT]
    pressKey(key)
    time.sleep(0.2)
    releaseKey(key)

def goToFloor():
    while(True):
        findPlayer()
        oldPlayerY = PLAYERY
        downJump()
        findPlayer()
        newPlayerY = PLAYERY
        if(oldPlayerY == newPlayerY):
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


async def main():
    global RUNE_EXIST
    findPlayer(1)
    sleepTime = int(TIME_INTERVAL)
    checkNumLock()
    while(RUNE_EXIST == 0):
        findRune()
        if(RUNE_EXIST == 1):
            toggleMacro()
            time.sleep(0.5)
            await moveRune()
            time.sleep(0.5)
        else:
            time.sleep(sleepTime)

def toggleMacro():
    if(MACRO_HYBRID == "TRUE"):
        keyArr = PLAY_PAUSE.split("+")
        keyOne = MACRO_DICT[keyArr[0]]
        keyTwo = MACRO_DICT[keyArr[1]]
        pyautogui.hotkey(keyOne,keyTwo)
    else:
        key = MACRO_DICT[PLAY_PAUSE]
        pyautogui.keyDown(key)
        time.sleep(0.5) #to be made adaptive
        pyautogui.keyUp(key)

    
#------------- DISCORD Region --------------------#
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.get_channel(int(CHANNEL_ID)).send("Bot is online")
    await bot.get_channel(int(CHANNEL_ID)).send("Type <ign>start to have the bot start scanning")

@bot.command(name='lanjiao')
async def discordlanjiao(ctx):
    myScreenshot= pyautogui.screenshot('images/captureimg.png',region=(0,0,1366,768))
    await ctx.send(file=discord.File('images/captureimg.png'))

@bot.command(name='start')
async def discordstart(ctx):
    global BOT_STATUS
    if BOT_STATUS == 0:
        await ctx.send('RuneBot is starting for '+CURRENT_USER)
        await ctx.send('It will scan every '+ TIME_INTERVAL + ' seconds')
        BOT_STATUS = 1
        await main()
    else:
        await ctx.send("RuneBot was already started, this command won't do anything")
    

async def discordsendrune():
    await bot.get_channel(int(CHANNEL_ID)).send("Rune found! {}".format(USER_MENTION))
    myScreenshot= pyautogui.screenshot('images/captureimg.png',region=(0,0,1366,768))
    await bot.get_channel(int(CHANNEL_ID)).send(file=discord.File('images/captureimg.png'))
    await bot.get_channel(int(CHANNEL_ID)).send("Check if you've reached the rune, run <ign>open if you are")
    await bot.get_channel(int(CHANNEL_ID)).send("If you aren't, run <ign>again")

@bot.command(name='again')
async def discordgorune(ctx):
    print("Trying to go to rune again")
    await ctx.send("Going to rune again")
    returnToPosition()
    await main()
    await ctx.send("Check if you've reached the rune, run <ign>open if you are")
    await ctx.send("If you aren't, run <ign>again")

@bot.command(name='open')
async def discorddorune(ctx):
    await ctx.send("Opening Rune...")
    pressRune()
    time.sleep(0.3)
    myScreenshot= pyautogui.screenshot('images/captureimg.png',region=(450,160,450,160))
    await ctx.send(file=discord.File('images/captureimg.png'))
    await ctx.send("Please input the following, based on the arrow keys: UP - u, Down - d, Left - l, Right - r")
    await ctx.send("Example, <ign>do ruru")

@bot.command(name='end')
async def discorddone(ctx):
    global RUNE_EXIST
    global RUNEX
    global RUNEY
    await ctx.send("Returning to position")
    returnToPosition()
    myScreenshot= pyautogui.screenshot('images/captureimg.png',region=(0,0,1366,768))
    await ctx.send(file=discord.File('images/captureimg.png'))
    RUNE_EXIST = 0
    RUNEX = 0
    RUNEY = 0
    await main()

@bot.command(name='do')
async def discordsolve(ctx,arg1):
    try:
        input = str(arg1) 
        action1=str(input[0]).upper()
        action2=str(input[1]).upper()
        action3=str(input[2]).upper()
        action4=str(input[3]).upper()

        result = action1+action2+action3+action4
        await ctx.send(result)
        
        pressKey(convertaction(action1))
        time.sleep(0.1)
        releaseKey(convertaction(action1))

        pressKey(convertaction(action2))
        time.sleep(0.1)
        releaseKey(convertaction(action2))

        pressKey(convertaction(action3))
        time.sleep(0.1)
        releaseKey(convertaction(action3))

        pressKey(convertaction(action4))
        time.sleep(0.1)
        releaseKey(convertaction(action4))
        time.sleep(0.5)
        
        myScreenshot= pyautogui.screenshot('images/captureimg.png',region=(0,0,1366,768))
        await ctx.send(file=discord.File('images/captureimg.png'))
        await ctx.send("Please check if the rune has been solved. If not, run <ign>open again.")
        await ctx.send("If you aren't on the rune anymore, run <ign>again")
        await ctx.send("If rune is solved, type <ign>end to go back to position")

    except(IndexError,ValueError):
        await ctx.send('wrong input, Example, <ign>do ruru')

# @bot.command(name='positionalright')
# async def discordpositionalfix(ctx):
#     await ctx.send("Repositioning to the right")
#     #epositionright()
#     myScreenshot= pyautogui.screenshot('images/captureimg.png')
#     await ctx.send(file=discord.File('images/captureimg.png'))
#     await ctx.send('back in position')

# @bot.command(name='positionalleft')
# async def discordpositionalfix(ctx):
#     await ctx.send("Repositioning to the left")
#     #repositionleft()
#     myScreenshot= pyautogui.screenshot('images/captureimg.png')
#     await ctx.send(file=discord.File('images/captureimg.png'))
#     await ctx.send('back in position')
if BOT_STATUS == 0:
    bot.run(BOT_TOKEN)
#------------- DISCORD Region --------------------#