import smtplib
from email.mime.text import MIMEText
import time

def send_mail(subject, messagebody, recipentmailid):
    sendermailid = "zoness.info@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    password = "zxwp ffgi xddb pgdp"

    msg = MIMEText(messagebody)
    msg['Subject'] = subject
    msg['From'] = ""
    msg['To'] = recipentmailid

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()

    server.sendmail(sendermailid,recipentmailid,msg.as_string())
    server.quit()


recipentmailid = "zoness.info@gmail.com"
messagebody = "this is my new code test mail from python"

send_mail('My Message',messagebody,recipentmailid)

print("completed")

