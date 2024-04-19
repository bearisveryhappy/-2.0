# -*-coding=utf-8-*-
# @Time : 2022/4/22 21:52
# @Author:熊金海
# @File : 邮箱轰炸.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText


aim = input("请输入您要轰炸的邮箱账号：")

sender ="1565328657@qq.com"
passwaord= "xjh2468."

body = "我在暗处偷偷地注视着你，你和我近在咫尺，却天各一方，我知道你的一切，但是你却不知道我是谁？"

msg = MIMEText(body,"html")
msg['subject'] = "猜猜我是谁？" #主题
msg['form'] = sender    #发送人
msg['to'] = aim     #接受人

buildlink = smtplib.SMTP_SSL('smtp.qq.com') #建立连接
buildlink.login(sender,passwaord)#身份验证
buildlink.sendmail(sender,aim,msg.as_string())#发送邮件
print("电子邮件发送成功")
