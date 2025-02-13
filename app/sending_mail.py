import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


def send_mail(key_id, user_name, user_mail):
    load_dotenv()

    subject = "Action Required: Update or Delete Your Expired OCI API Key"
    body = f"""
            Dear {user_name},
            We have detected that your API key is older than 90 days. For security reasons, 
            please update or delete the key.
            
            Key ID: {key_id}
            
            To manage your API keys, please visit: https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/api-identity-api-keys.html OCI API Key Management
            
            Thank you, 
            Your Security Team
        """

    msg = MIMEMultipart()
    msg["From"] = os.getenv('SENDER_EMAIL')
    msg["To"] = user_mail
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
        server.starttls()  # Secure the connection
        server.login(os.getenv('SENDER_EMAIL'), os.getenv('SENDER_PASSWORD'))
        server.sendmail(os.getenv('SENDER_EMAIL'), user_mail, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    send_mail("hdghdhd", "jirka", "peny753@seznam.cz")
