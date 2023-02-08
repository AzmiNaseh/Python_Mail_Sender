from redmail import outlook


def send_mail_with_outlook_account():
        outlook.username = "USERNAME"
        outlook.password = "PASSWORD"
        outlook.send(
            receivers=["mail@outlook.com"],
            subject="Subject",
            text="Something",
            attachments={'My_file':Path('/path/to/file.txt')}
        )
        print("Mail Sent")


if __name__ == "__main__"
	send_mail_with_outlook_account()
