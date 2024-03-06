import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import schedule


# Email configuration
sender_email = 'zoness.info@gmail.com   '
sender_password = 'zxwp ffgi xddb pgdp'
receiver_email = 'zoness.info@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # For starttls

def scheduled_email():
# Create a MIMEText object with the content of your email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Test Email Subject'
    body = 'Hello, this is a test email from Python!'
    #print(message)
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)


    

    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

    # Close the connection
    server.quit()   

schedule.every().day.at("11:05:00").do(scheduled_email)

while True:
    schedule.run_pending()
    time.sleep(1)