import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000) # generate random number for file name
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(url, full_name)

download_web_image(r'https://previews.123rf.com/images/byrdyak/byrdyak1602/byrdyak160200106/53678958-lion-on-dark-background-black-and-white-image.jpg')