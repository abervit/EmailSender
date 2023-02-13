# Sending email with python

"""Go over to our gmail account and setup 2 factor authentication password"""
"""generate up password"""
"""create a function to send an email"""

from email.message import EmailMessage
from app import password
import ssl
import smtplib

"""Setting up our email"""
email_sender = "vitaliy.kachkovskiy@gmail.com"
email_password = password
email_receiver = "witalij.kaczkowski@gmail.com"

"""Creating a template email information"""
subject = "Hello it`s a test email"
body = """
This is my first Python project I`m happy to email you about.
Hope it works well !!!\n\nBest regards,\nVitaliy
 """
"""Now we creating an instance of this email message library package that we are importing"""
em = EmailMessage() # creating our instance
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body) # setting a context of our email

"""
Now we finished our app. Now we going are going to create a context.
First we need to import SSL and SMT library.
 """
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password) # login with email our login and password
    # now we converting this em which is the instance of EmailMessage(), that already has all details now
    # send as string
    smtp.sendmail(email_sender, email_receiver, em.as_string())

