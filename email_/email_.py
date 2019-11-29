"""
https://docs.python.org/3/library/email.examples.html
"""

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


# Open the plain text file whose name is in textfile for reading.
# with open(textfile) as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())


def send_message():
    msg = EmailMessage()
    msg.set_content("hi,i'm python script.")
    me = "y22222ly@163.com"
    you = "support@jadewirelesshelp.zendesk.com"
    msg['Subject'] = f'The contents of python script'
    msg['From'] = me
    msg['To'] = you
    print("start send.")
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.163.com')
    # todo 需要填写自己的密码
    s.login(me, "xxx")
    s.send_message(msg)
    s.quit()
    print("end send.")


if __name__ == '__main__':
    send_message()
