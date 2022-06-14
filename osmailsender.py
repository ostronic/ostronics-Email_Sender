#coded by ostronics, Qxchan
#contact us at https://www.disotronics.com , on TELEGRAM @ https://t.me/Qxchan
#visit our groupo on telegram @ hackerbdv https://t.me/hackerbdv

import smtplib 

HOST = "smtp.mydomainname.com"
SUBJECT = "DIOSTRONICS MAILER"
TO = input("Enter the mailof person you wish to send to:- \n")
FROM = "chhan@gmail.com.com"
text = input("ENTER YOUR TEXT HERE. FOR EXAMPLE:- helolo hacker howdy! \n")
BODY = "\r\n".join((
	f"From: {FROM}".,
	f"To: {TO}",
	f"Subject: {SUBJECT}",
	"",
	text)
)
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()
