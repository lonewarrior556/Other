import time
import datetime
import random
from twilio.rest import TwilioRestClient
import pickle
print 'loaded successfull'
def sendtext(message):
    # Your Account Sid and Auth Token from twilio.com/user/account     
    account_sid = "AC37ba247f8aa60226af2e70d5d958d007"
    auth_token  = "4df42e03649da308a5ac2c95edba73dc"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.sms.messages.create(body=message,
       to="+12016542357",    # Replace with your phone number                 
       from_="+12013555397") # Replace with your Twilio number                
    print message.sid

f=open('grewords')
temp=f.read()
d=pickle.loads(temp)
f.close()
#43200 seconds

while True:
    time.sleep(80)
    temp=str(datetime.datetime.now())
    hour=temp[11:13].replace(':','')
    a=random.randint(1,100)
    print a
    if a==1:
        if int(hour)>13 or int(hour)<2:
            word=random.choice(d.keys())
            message=str((word,d.get(word)))
            message=message.replace('(','')
            message=message.replace(')','')
            message=message.replace("'",'')
            sendtext(message)
        else:print'wrong time'
    else:print 'wrong number'
    
