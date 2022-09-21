import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

account = input('请输入邮箱账户：')
token = input('请输入邮箱授权码：')

smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
smtp.login(account, token)

content = '我是一篇正文'

email_content = MIMEText(content, 'plain', 'utf-8')
message = MIMEMultipart()
message.attach(email_content)
message['From'] = ''
message['To'] = ''
message['Subject'] = ''

smtp.sendmail(account, 'liuchaoenglish@126.com', message.as_string())

smtp.quit()