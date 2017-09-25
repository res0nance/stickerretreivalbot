import telepot
import pprint
import telepot.loop
import time
import os
from PIL import Image, features
from imgurpython import ImgurClient

client = None
bot = None

def init():
    global client, bot
    imgur_client_id = os.environ['IMGUR_CLIENTID']
    imgur_client_secret = os.environ['IMGUR_SECRET']
    telegram_botid = os.environ['TELEGRAM_BOTID']
    client = ImgurClient(imgur_client_id, imgur_client_secret)
    bot = telepot.Bot(telegram_botid)
    pprint.pprint(bot.getMe())

def convert_to_png(file):
    img = Image.open(file)
    new_file = os.path.basename(file) + '.png'
    img.save(new_file)
    return new_file

def upload_to_imgur(file):
    return client.upload_from_path(file, anon=True)

def handle(msg):
    pprint.pprint(msg)
    if 'sticker' in msg:
        path = os.path.dirname(__file__)
        bot.download_file(msg['sticker']['file_id'], os.path.join(path,'temp.webp'))
        file = convert_to_png(filename)
        image = upload_to_imgur(file)
        bot.sendMessage(msg['chat']['id'], image['link'])

def main():
    init()
    telepot.loop.MessageLoop(bot,handle).run_as_thread()
    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()
