import smtplib
from Security.config import *
import traceback

def send(user, token, context):

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, user.email, message.format('Validate your email', 'https://learngram-register.herokuapp.com/validate?tkn='+str(token)))
            print('Sent email!')
    except:
        traceback.print_exc()