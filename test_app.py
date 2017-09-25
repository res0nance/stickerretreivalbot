import app
from PIL import Image, features
from imgurpython import ImgurClient

def test_init():
    app.init()

def test_pillow():
	test_init()
	img = Image.new('RGB', (50,50))
	img.save('test.jpg')

def test_imgur():
	test_pillow()
	img = Image.open('test.jpg')
	img.save('test.png')
	image = app.client.upload_from_path('test.png', anon=True)