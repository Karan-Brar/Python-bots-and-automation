# 1) Check price of product
# 2) Get notified via email when price goes below a certain point
# 3) Keep checking price and send email automatically after a given period of seconds once the script has been run, 

from email import message
import requests
from lxml import html
import smtplib, ssl
import getpass
import time

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

def send_email(price, password):

    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "senseicode777@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        message = f'Your product is now {price}'
        server.sendmail(sender_email, sender_email, message)
        print("Email sent!")
    except Exception as e:
        print("Error sending email")
        print(e)
        quit()
    finally:
        server.quit() 

if __name__ == "__main__":

    password = getpass.getpass()
    while(True):
        price = get_price()
        if float(price) < float(250):
            send_email(price, password)
        time.sleep(86400)
        