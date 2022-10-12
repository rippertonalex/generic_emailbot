#email spam bot 
import pandas as pd 
import numpy as np 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
from email.message import MIMEPart
from email.mime.image import MIMEImage
import smtplib

def sendMailRequest(subject, bodyMessage,  receiverList):
    try:
        sender_address = 'rippertonalex@gmail.com'
        message = MIMEMultipart()
        message['From'] = sender_address                                       
        message['To'] = ', '.join(receiverList)
        message['Subject'] = subject
            #img_3 = MIMEImage(fp.read())
        #message.attach(img_3)
        #with open(attachment, 'rb') as fp:     If you want to attach an image 
        message.attach(MIMEText(bodyMessage, 'plain'))
        #message.attach(MIMEImage(fig_img_files))
        #print(str(subject)+' :: mailCongig :: sendMailRequest') 
        session = smtplib.SMTP('mailgate.qintra.com', 25)
        #session.starttls()
        text = message.as_string()
        session.sendmail(sender_address, receiverList, text)
        print(str(subject)+' :: mailCongig :: sendMailRequest ==> Mail sent successfully..')
        session.quit()
         
    except Exception as e:
       print("Error: unable to send email::" + str(e))
       print(str(subject)+" :: mailCongig :: Error: unable to send email::" + str(e))

email_body_summary = ("hey there")

emailReceiverList = ['rippertonalex@berkeley.edu' ]

num_times = 0 
while num_times < 10:
    sendMailRequest("you are being messaged by rippo", email_body_summary, emailReceiverList)
    num_times += 1

