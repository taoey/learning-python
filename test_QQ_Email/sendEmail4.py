#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = 'swhwtqwer@163.com'
you =["2517129987@qq.com", '741494582@qq.com'] #联系人列表


# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link的"
msg['From'] = "黄为涛"
msg['To'] =  ",".join( you )

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHereni你好e link you wanted:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">链接</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.163.com')
s.set_debuglevel(True)
s.login('swhwtqwer@163.com', '')   #输入你的邮箱口令
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
