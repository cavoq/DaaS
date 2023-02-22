import smtplib, ssl
from src.log import log

SMTP_SERVER = "smtp.gmail.com"
PORT = 587

context = ssl.create_default_context()

class MailSender:
    def __init__(self, sender_email: str, password: str):
        self.sender_email = sender_email
        self.password = password
        
    def connect(self):
        try:
            self.server = smtplib.SMTP(SMTP_SERVER, PORT)
            self.server.starttls(context=context)
            self.server.login(self.sender_email, self.password)
        except:
            log.error(f"Not able to connect to {SMTP_SERVER}:{PORT} with {self.sender_email}")
        
    def send_mail(self, receiver_email: str, message: str):
        self.server.sendmail(self.sender_email, receiver_email, message)
        
    def disconnect(self):
        self.server.quit()
         