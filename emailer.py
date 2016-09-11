#!/usr/bin/python
# Python emailer component for the
# security.sh script using yagmail
# Gmail/SMTP client
import yagmail
import keyring
# variable for Gmail account
yag = yagmail.SMTP('somebody@gmail.com', 'yourpasswd')

# Variables for email alert
to = 'someone@gmail.com'
subject = 'Security Alert!'
body = 'This is an automated message informing you of a potential security breech!'
attach = '/tmp/.theft/theft.tar.gz'

# Register your email password with keyring (uncomment below)
# keyring.set_password('yagmail', 'someone@gmail.com', 'yourpasswd')

# Send the message
yag.send(to = to, subject = subject, contents = [body , attach])




