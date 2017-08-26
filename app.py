import telepot
import pprint
import telepot.loop
import time
import os
from PIL import Image, features
from imgurpython import ImgurClient

client = ImgurClient(os.environ['imgur_client_id'], os.environ['imgur_client_secret'])
bot = telepot.Bot(os.environ['telegram_apikey'])

def handle(msg):
    pprint.pprint(msg)
    if( 'sticker' in msg ):
        path = os.path.dirname(__file__)
        bot.download_file(msg['sticker']['file_id'], os.path.join(path,'temp.webp'))
        img = Image.open(os.path.join(path,'temp.webp'))
        img.save(os.path.join(path,'temp.png'))
        image = client.upload_from_path(os.path.join(path,'temp.png'), anon=True)
        bot.sendMessage(msg['chat']['id'], image['link'])


pprint.pprint(bot.getMe())
telepot.loop.MessageLoop(bot,handle).run_as_thread()

while 1:
    time.sleep(10)
