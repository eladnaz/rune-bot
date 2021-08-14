from PIL.Image import NONE
import pyautogui
import win32gui
import ctypes
import time
import discord
from discord.ext import commands
SCREEN_X1 = 0
SCREEN_X2 = 0
SCREEN_Y1 = 0
SCREEN_Y2 = 0
MAPLE_X1 = 0
MAPLE_X2 = 0
MAPLE_Y1 = 0
MAPLE_Y2 = 0
MAPLE_NAME = "Swordie"
PLAYERX_SAVED = 0
PLAYERY_SAVED = 0
RUNE_EXIST = False
BOT_STATUS = 0
CHANNEL_ID = "876090831356952596"
chatid = ''
client = discord.Client()
Token ='ODc2MDkxNDE0OTQ0MDM0ODU2.YRfBtg.ekYuxDhZhGZfUVhWm3CAOsIgC90'
currentuser = 'pull'
bot = commands.Bot(command_prefix=currentuser)

SendInput = ctypes.windll.user32.SendInput


UP = 0xC8
DOWN = 0xD0
LEFT = 0xCB
RIGHT = 0xCD
SPACE = 0x39
F10 = 0x44

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

def flashJump():
    pressKey(SPACE)
    print("JUMP")
    time.sleep(0.1)
    releaseKey(SPACE)

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
    pressKey(N)
    time.sleep(0.5)
    releaseKey(N)
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
 #temporary fix for one way communication

def toggleMacro():
    pyautogui.keyDown('f10')
    time.sleep(0.5) #to be made adaptive
    pyautogui.keyUp('f10')


def placeholder_start():
    moveRune()
    time.sleep(0.5)
    #captureimg(chatid,'checkposition')
    
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
    await ctx.send('RuneBot is starting for '+currentuser)
    BOT_STATUS = 1
    try: 
        main()
    except Exception as e:
        print ("fuckingfailed",e)
    finally:
        myScreenshot= pyautogui.screenshot('images/captureimg.png')
        await ctx.send(file=discord.File('images/captureimg.png'))
        await ctx.send("Please input the following, based on the arrow keys: UP - U, Down - D, Left - L, Right - R")
        await ctx.send("Example, shinobusolve R R L L")

@bot.command(name='dorune')
async def discorddorune(ctx):
    await ctx.send("Opening Rune...")
    pressRune()
    myScreenshot= pyautogui.screenshot('images/captureimg.png')
    await ctx.send(file=discord.File('images/captureimg.png'))
    await ctx.send("Please input the following, based on the arrow keys: UP - U, Down - D, Left - L, Right - R")
    await ctx.send("Example, shinobusolve R R L L")

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

bot.run(Token)
#------------- DISCORD Region --------------------#


# #/start command
# def start(update, context):
#     global BOT_STATUS
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Runebot is starting Now.")
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Position saved")
#     #context.bot.send_message(chat_id=update.effective_chat.id, text="Please run /dorune after reaching rune.")
#     user = update.message.from_user
#     changechatid(user['id'])
#     BOT_STATUS = 1
#     main()
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)    
# #end of /start command

# #/dorune command
# def dorune(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Opening Rune...")
#     sendRuneImg()
# dorune_handler = CommandHandler('dorune', dorune)
# dispatcher.add_handler(dorune_handler)    
# #end of /dorune command

# def done(update, context):
#     global RUNE_EXIST
#     returnToPosition()
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Returning to position")
#     RUNE_EXIST = 0
# dispatcher.add_handler(CommandHandler("done",done)) 

#rune solving /solve command
# def runesolve(update,context):
#     try:
#         action1=str(context.args[0])
#         action2=str(context.args[1])
#         action3=str(context.args[2])
#         action4=str(context.args[3])
#         result = action1+action2+action3+action4
#         update.message.reply_text(str(result))
        
#         pressKey(convertaction(action1))
#         time.sleep(0.3)
#         releaseKey(convertaction(action1))

#         pressKey(convertaction(action2))
#         time.sleep(0.3)
#         releaseKey(convertaction(action2))

#         pressKey(convertaction(action3))
#         time.sleep(0.3)
#         releaseKey(convertaction(action3))

#         pressKey(convertaction(action4))
#         time.sleep(0.3)
#         releaseKey(convertaction(action4))
#         time.sleep(0.5)
#         captureimg(chatid,'checkrune')

#     except(IndexError,ValueError):
#         update.message.reply_text('wrong input, Example, /solve R R L L')

# dispatcher.add_handler(CommandHandler('solve',runesolve))
#end of rune solving command



# #/reporight command
# def reporight(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Repositioning to the right")
#     #repositionright()
#     captureimg(chatid,'back in position')

# reporight_handler = CommandHandler('reporight', reporight)
# dispatcher.add_handler(reporight_handler)
# #end of /reporight command
