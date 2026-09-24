import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

from paths import path

def send_files_by_email():
    load_dotenv()
    
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', 465))
    sender_email = os.getenv('SMTP_USER')
    app_password = os.getenv('SMTP_PASSWORD')
    recipient_email = os.getenv('EMAIL_TO')
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Relatório diário de exportação de preços - Arquivos anexados"
    
    body = "Prezados,\n\nSegue em anexo os arquivos de exportação de preços do sistema."
    msg.attach(MIMEText(body, 'plain'))

    zip_base = path('PATH_ZIP_OUTPUT', os.path.join('Output'))
    
    print(f"Searching for files in: {zip_base}")
    attached_something = False

    for root, dirs, files in os.walk(zip_base):
        for file in files:
            if file.endswith(".zip"):
                full_path = os.path.join(root, file)
                print(f"File found and attached: {file}")
                
                with open(full_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={file}")
                    msg.attach(part)
                    attached_something = True

    if not attached_something:
        print("ERROR: No .zip files were found in the folders. Check the path!")
        return

    attempts = 3
    wait_seconds = 15
    for attempt in range(1, attempts + 1):
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(sender_email, app_password)
                server.send_message(msg)
            print("Corporate email sent successfully (via SSL)!")
            break
        except Exception as e:
            print(f"Error sending email (attempt {attempt}/{attempts}): {e}")
            if attempt < attempts:
                print(f"Waiting {wait_seconds}s before trying again...")
                time.sleep(wait_seconds)
            else:
                print("All send attempts failed.")

if __name__ == "__main__":
    send_files_by_email()
