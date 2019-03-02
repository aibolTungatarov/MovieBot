#imports
import telepot
import random
from telepot.loop import MessageLoop
import requests
import time
#constants
BASE_URL = "https://api.telegram.org/bot720395112:AAENzgp5sJ0YcogmLXLFN_AOBgcPdjqD908/"
TOKEN = "720395112:AAENzgp5sJ0YcogmLXLFN_AOBgcPdjqD908"
movies = ["Forest Gamp", "13 Reasons why", "Startrek", "Vikings", "Naruto"]

bot = telepot.Bot(TOKEN)

def getRandomMovie(msg):
    chat = bot.getUpdates()[-1]["message"]["chat"]["id"]
    randomMovie = random.choice(movies)
    bot.sendMessage( chat, randomMovie)
MessageLoop(bot, getRandomMovie).run_as_thread()


# Keep the program running.
while 1:
    time.sleep(10)
