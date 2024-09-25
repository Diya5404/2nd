import yagmail
import os
from dotenv import load_dotenv

load_dotenv()
sender = "venombot851@gmail.com"
receiver = "04emvb1bzc@freeml.net"
subject = 'Test mail using python'
content = '''
This is the content for side for sending mail
'''
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=content)
print("Email send!")
