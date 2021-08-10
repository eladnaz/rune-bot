import logging
import os
import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch_loop
from telegram.ext import Updater
from telegram.ext import CommandHandler

#Added for basic logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Token = bot token
#will try to make this dynamic sooner or later, currently static
updater = Updater(token='1943796758:AAEIOnVHudYvaXieLICpDVStbBHNpjPcIbs', use_context=True)
dispatcher = updater.dispatcher
#end of tokens

#/start command for the luls
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#end of /start command
updater.start_polling()

#start of captureimg cmd
def captureimg(update,context):
    myScreenshot= pyautogui.screenshot('images/captureimg.png')
    context.bot.sendPhoto(chat_id=update.effective_chat.id,photo=open("images/captureimg.png",'rb'),caption="this is a img sent")

captureimg_handler = CommandHandler('captureimg',captureimg)
dispatcher.add_handler(captureimg_handler)
#end of captureimg cmd

#start of holdkey function
def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)
#end of holdkey function

#start of sendkeyboardinput <-- can be used with multiple keys idk for now just hold a
def sendkeyboardinput(update,context):
    hold_key('a', 5)
#end of sendkeyboardinput

#start of /keyboardinput command
keyboardinput_handler = CommandHandler('keyboardinput',sendkeyboardinput)
dispatcher.add_handler(keyboardinput_handler)
#end of /keyboardinput command



pos = imagesearch_loop("images/minime.png", 1)
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
else:
    print("image not found")