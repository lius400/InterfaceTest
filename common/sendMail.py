#! /usr/bin/env python
# coding=utf-8

import os
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication

'''
先来想下发送邮件需要填写什么，还需要有什么条件
1.与邮件服务器建立连接,用户名和密码
2.发邮件:发件人\收件人\主题\内容\附件
3.发送
'''

class Mail_entity:
    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, value):
        self._host = value

    @property
    def adress(self):
        return self._adress
    @adress.setter
    def adress(self, value):
        self._adress = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, value):
        self._port = value

    @property
    def sender(self):
        return self._sender
    @sender.setter
    def sender(self, value):
        self._sender = value

    @property
    def receiver(self):
        return self._receiver
    @receiver.setter
    def receiver(self, value):
        self._receiver = value


class SendMail:
    # def send_mail(self, sender, receiver, title):
    def send_mail(self,host,port,adress,password,sender, receiver, title, attach_xlsx, attach_jpg):
        msg = email.mime.multipart.MIMEMultipart()  # 生成包含多个邮件体的对象
        msg['from'] = sender
        msg['to'] = receiver
        msg['subject'] = title
        content = '''
        Hi all，
        这是一封LIUCHAO自动化测试发送的邮件
        微信号:            
        带附件
        '''
        print('成功1')
        # 邮件正文,将文件正文当成附件发送,当正文内容很多时,提高效率
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        print('成功2')

        # excel附件--固定格式
        xlsxpart = MIMEApplication(open(attach_xlsx, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\result"+"\ResultData.xlsx")
        msg.attach(xlsxpart)

        # # jpg图片附件
        # jpgpart = MIMEApplication(open(attach_jpg, 'rb').read())
        # jpgpart.add_header('Content-Disposition', 'attachment', filename='接口测试框架.jpg')
        # msg.attach(jpgpart)

        # 发送邮件
        smtp = smtplib
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)  # 设置为调试模式，console中显示
        print('成功3')
        smtp.connect(host, port)  # 链接服务器，smtp地址+端口
        print('成功4')
        smtp.login(adress, password)  # 登录，用户名+密码
        print('成功5')
        smtp.sendmail(sender, receiver, str(msg))  # 发送，from+to+内容
        smtp.quit()
        print('发送邮件成功')



# sender = 'lius400@163.com'
# receiver = 'lius400@hotmail.com'
# title = '测试文件'
# # attach_xlsx = 'C:/Users/Administrator/Desktop/liuchao-testcase1.xlsx'
# # attach_jpg = 'C:/Users/Administrator/Desktop/接口测试框架.jpg'
#
# mail = SendMail()
# mail.send_mail(sender,receiver,title)
# # mail.send_mail(sender,receiver,title,attach_xlsx,attach_jpg)
