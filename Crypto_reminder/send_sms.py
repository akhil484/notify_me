import os
from twilio.rest import Client
from scraper import *
from datetime import datetime
import time


now = datetime.now()
today8am = (now.replace(hour=00, minute=38, second=0)).time()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
price_of_crypto = get_crypto_price("ethereum")
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
while True:
     now = datetime.now()
     current_time = now.time()
     print("Current Time =", current_time)
     if current_time > today8am:
          client = Client(account_sid, auth_token)
     
          message = client.messages \
                         .create(
                              body=("Price of Ethereum is %s")%price_of_crypto,
                              from_='+1930203xxxx',
                              to='+91xxxxxxxxxx'
                         )

          print(message.sid)
          break
     print("Sleep")
     time.sleep(3)