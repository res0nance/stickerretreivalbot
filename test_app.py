import app
from PIL import Image, features
from imgurpython import ImgurClient

def test_init():
    app.init()

def test_pillow():
	img = Image.new('RGB', (50,50))
	img.save('test.jpg')
	return app.convert_to_png('test.jpg')

def test_imgur():
	app.init()
	file = test_pillow()
	app.upload_to_imgur(file)