import telepot
import pprint
import telepot.loop
import time
import os
from PIL import Image, features
from imgurpython import ImgurClient

imgur_client_id = 'IMGUR_CLIENTID'
imgur_client_secret = 'IMGUR_SECRET'
telegram_botid = 'TELEGRAM_BOTID'

client = ImgurClient(imgur_client_id, imgur_client_secret)
bot = telepot.Bot(telegram_botid)

def handle(msg):
    pprint.pprint(msg)
    if( 'sticker' in msg ):
        path = os.path.dirname(__file__)
        filename = 'temp.webp'
        bot.download_file(msg['sticker']['file_id'], os.path.join(path,filename))
        img = Image.open('temp.webp')
        img.save('temp.png')
        image = client.upload_from_path('temp.png', anon=True)
        bot.sendMessage(msg['chat']['id'], image['link'])


pprint.pprint(bot.getMe())
telepot.loop.MessageLoop(bot,handle).run_as_thread()

while 1:
    time.sleep(10)
