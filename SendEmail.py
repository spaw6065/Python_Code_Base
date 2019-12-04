import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP()
server.connect(smtp_host,smtp_port)
server.ehlo()
server.starttls()
user="psumit88@gmail.com"
passw=9617231371
server.login(user,passw)
fromaddr = "Sumit"
tolist = "Sumit.Pawar@netcracker.com"
sub = "Dummy"

msg = email.MIMEMultipart.MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = "psumit88@gmail.com.com"
msg['Subject'] = sub  
body_txt = "Hello Sumit,\nHow are you ? \n\nRegards,\nSumit"
msg.attach(MIMEText(body_txt))
server.sendmail(user,tolist,msg.as_string())
