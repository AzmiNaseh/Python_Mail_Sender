from redmail import gmail

def send_mail_with_gmail_account():
        gmail.username = "USERNAME"
        gmail.password = "PASSWORD"
        gmail.send(
            receivers=["mail@yourdomain.com"],
            subject="Subject",
            text="Something",
            attachments={'My_File':Path('/path/to/file.txt')}
        )
        print("Mail Sent")

if __name__ == "__main__"
    send_mail_with_gmail_account()
