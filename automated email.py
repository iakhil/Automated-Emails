from googletrans import Translator
import random
translator=Translator()
import smtplib, ssl
k=['Father','Mother','Brother','Children','Dog','Cat','Table','Newspaper','Computer','Chips',
   'Telephone','Lamp','Hello','Chair','A boy','A girl','Bye','Good morning','Good night','How are you',
   'Please','Sorry','Thank you','Welcome','Apple','Banana','King','Queen','Tree','Forest',
   'Clock']
#y=random.choice(k)
#message=translator.translate(y)
#h=message.text
m="""Subject: German Word of the Day 
        
    Here is your daily foregin language word of the day:

    English: {} \n  German: {}"""
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "vaguelyamusing.co.in@gmail.com"
receiver_email = "akhilkashyap16@gmail.com"
#te=   f"German word {y} English translation: {message.text}"
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email,'Swalbardgeorgetown')

    #server.sendmail(sender_email,receiver_emai,k)
   # t=f"German word: {y} \n English translation: {message.text}"
    y=random.choice(k)
    tr=translator.translate(y,dest='de')
    server.sendmail(sender_email,receiver_email,m.format(y,tr.text))
    