# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib
from email.mime.text import MIMEText

mailto_list = ["2517129987@qq.com"]
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "swhwtqwer@163.com"  # 用户名
mail_pass = ""  # 口令
mail_postfix = "163.com"  # 发件箱的后缀


def send_mail(me,you, content):
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['From'] = me
    msg['To'] =you
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me,you, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False


if __name__ == '__main__':
    if send_mail(mail_user,mailto_list[0],  "hello world！"):
        print( "发送成功")

    else:
        print( "发送失败")
