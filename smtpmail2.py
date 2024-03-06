import threading
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import asyncio

# Email configuration
sender_email = 'zoness.info@gmail.com'
sender_password = 'zxwp ffgi xddb pgdp'
receiver_email = 'zoness.info@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # For starttls

def background_job():
    print('Hello from the background thread')

def scheduled_email():
    # Create a MIMEText object with the content of your email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Test Email Subject'
    body = 'Hello, this is a test email from Python!'
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

async def schedule_checker():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

# Schedule background job
schedule.every().second.do(background_job)

# Schedule email to be sent every day
schedule.every().day.at("11:08").do(scheduled_email)

# Start the schedule checker
asyncio.run(schedule_checker())
