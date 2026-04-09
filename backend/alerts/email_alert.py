import smtplib
from email.message import EmailMessage

def send_email(event, risk):
    msg = EmailMessage()
    msg.set_content(
        f"Attack detected!\nUser: {event['username']}\nIP: {event['ip']}\nRisk: {risk}"
    )
    msg["Subject"] = "Security Alert"
    msg["From"] = "yourmail@gmail.com"
    msg["To"] = "admin@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("yourmail@gmail.com", "APP_PASSWORD")
    server.send_message(msg)
    server.quit()
