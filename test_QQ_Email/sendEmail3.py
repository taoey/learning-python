import smtplib
from email.mime.text import MIMEText


s = smtplib.SMTP('smtp.163.com')
s.set_debuglevel(True)
s.login('swhwtqwer@163.com', '')  #输入你的邮箱口令(不是密码哦)
sub="Pythonr"
text="""

秦皇岛
22日白天
 晴 24℃
22日夜间
多云 10℃


 沧州
22日白天
 晴 27℃

"""
msg = MIMEText(text)

msg['Subject'] = '%s' % sub
msg['From'] = 'swhwtqwer@163.com'
msg['To'] = '741494582@qq.com'

s.send_message(msg)
s.quit()