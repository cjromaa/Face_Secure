import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    filename = 'log.txt'
    fromaddr = ''  # Enter email address 
    password = ''  # Enter password of email address
    toaddr = ''    # Enter the receiving email address

    # Creating the MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"

    # Attaching the body of the email
    body = "Please find the attached log file."
    msg.attach(MIMEText(body, 'plain'))

    # Opening the file to be sent
    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(part)

    # Establishing the server connection and sending the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    print("Login success")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Email has been sent")
