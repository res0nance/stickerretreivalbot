import app
from PIL import Image, features
from imgurpython import ImgurClient

def test_init():
    app.init()

def test_pillow():
	test_init()
	img = Image.new('RGBA', (50,50))
	img.save('test.jpg')
	image = client.upload_from_path('test.jpg', anon=True)
