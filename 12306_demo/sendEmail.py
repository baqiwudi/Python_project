
import smtplib

from email.mime.text import MIMEText
from email.header import Header

# 发邮件
from_addr = '357244729@qq.com'
#我的授权码
password = 'ibbccxmtkzclcwwd'
to_addr = '765924760@qq.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText("Test")
msg['From'] = Header("霸气无敌", 'utf-8')
msg['To'] = Header("测试", 'utf-8')
msg['Subject'] = Header("一起愉快的玩耍哦", 'utf-8').encode()
try:
    # 注意端口不是25
    server = smtplib.SMTP_SSL(smtp_server, 465)
#   server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print('发送成功')
except Exception:
    print('发送失败')


