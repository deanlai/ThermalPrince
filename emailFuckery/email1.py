# Trial 1 of connecting to some emails
import smtplib
import time
import imaplib
import email


ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "thermalprincepdx" + ORG_EMAIL
FROM_PWD = "Zzxtf3three"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def readmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

    except:
        print("error")

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    print(id_list)
    print("----")
    first_email_id = id_list[0]
    latest_email_id = id_list[-1]

    typ, data = mail.fetch(1, '(RFC822)')
    for response_part in data:
        msg = email.message_from_string(response_part[1])
        email_subject = msg['subject']
        email_from = msg['from']
        print('From; ', email_from, '\n')



readmail()






