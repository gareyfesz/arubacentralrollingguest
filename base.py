import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pycentral.base import ArubaCentralBase
from pprint import pprint
from config import central_info
from passwordgen import password
from config import apiPath
from config import apiData
from config import sender_email
from config import recipient_email
from config import smtp_server
from config import smtp_port
from config import subject



ssl_verify = True
central = ArubaCentralBase(central_info=central_info,
                           ssl_verify=ssl_verify)

# Sample API call using 'ArubaCentralBase.command()'


apiMethod = "PUT"

base_resp = central.command(apiMethod=apiMethod,
                            apiPath=apiPath,
                            apiData=apiData)

pprint(base_resp)

name = "name"
sender_email = sender_email
recipient_email = recipient_email
smtp_server = smtp_server
smtp_port = smtp_port
subject = subject
body = f'Username: {name} \nPassword: {password}' 


message = MIMEMultipart()
message['Subject'] = subject

message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Send the email without authentication
    server.sendmail(sender_email, recipient_email, message.as_string())

print('email sent to', recipient_email)

