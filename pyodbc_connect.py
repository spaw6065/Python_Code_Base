import pyodbc

import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = 'msazsp.database.windows.net'

database = 'msazsp'
username = 'msazsp'
password = ''
driver= '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()
#cursor.execute("SELECT name EmpName FROM EMPDTLS where age=29")
cursor.execute("SELECT CLIENT,PSUPNO,ISSUEPRIORITY,ISSUEDESC from IssueList")
row = cursor.fetchone()

while row:
    print str(row[0])   
    body_text = "Hello Sumit,\nRetrieved from Microsoft Azure Database\n\n" + row[0] + "\n" + row[1] + "\n" + row[2] + "\n\nRegards,\nSumit"
    row = cursor.fetchone()

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
tolist = "psumit88@gmail.com"
sub = "Microsoft Azure Database Data Retrieval."

msg = email.MIMEMultipart.MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = "psumit88@gmail.com"
msg['Subject'] = sub  

msg.attach(MIMEText(body_text))

server.sendmail(user,tolist,msg.as_string())
