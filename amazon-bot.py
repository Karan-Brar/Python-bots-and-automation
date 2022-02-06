# 1) Check price of product
# 2) Get notified via email when price goes below a certain point

from itertools import product
import requests
from lxml import html

def get_price():

    url = 'https://www.amazon.ca/SoundLink-Around-Ear-Wireless-Headphones-Black/dp/B0117RGG8E/ref=sr_1_8?crid=3ENGSFC9SR1YZ&keywords=bose%2Bheadphones&qid=1644181423&sprefix=bose%2Bheadphones%2Caps%2C104&sr=8-8&th=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Accept-Encoding': None
    }

    response = requests.get(url, headers=headers)
    tree = html.fromstring(response.content)
    price = tree.xpath('//span[@class="a-offscreen"]/text()')[0]
    return price.replace("$","")


if __name__ == "__main__":

    price = get_price()

    if float(price) < float(250):
        print('Send email')