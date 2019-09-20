#!/usr/bin/env python3
import smtplib
import getpass
import time

def main():
    myaddress = input("Enter your mail.com address:")
    mypass = getpass.getpass("Enter your password:")
    target = 'strikeyoface@mail.com'
    target2 = 'airbornepathfinder@mail.com'
    target3 = 'pass_gil_word@mail.com'

    content = f'From:{myaddress}\nSubject: VALUABLE SAVINGS INSIDE\nJust kidding, it\'s a virus'
    mail = smtplib.SMTP('smtp.mail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myaddress, mypass)
   # for i in range(100):
   #     time.sleep(2)
   #     print("emailing...")
    mail.sendmail(myaddress, myaddress, content)
   #     mail.sendmail(myaddress, target2, content)
   #     mail.sendmail(myaddress, target3, content)
    mail.close()

main()
