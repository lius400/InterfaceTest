#! /usr/bin/env python
# coding=utf-8

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

class SendMail:
    # def send_mail(self, sender, receiver, title):
    def send_mail(self, sender, receiver, title, attach_xlsx, attach_jpg):
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

        # # excel附件--固定格式
        # xlsxpart = MIMEApplication(open(attach_xlsx, 'rb').read())
        # xlsxpart.add_header('Content-Disposition', 'attachment', filename='liuch-testcase1.xlsx')
        # msg.attach(xlsxpart)
        #
        # # jpg图片附件
        # jpgpart = MIMEApplication(open(attach_jpg, 'rb').read())
        # jpgpart.add_header('Content-Disposition', 'attachment', filename='接口测试框架.jpg')
        # msg.attach(jpgpart)

        # 发送邮件
        smtp = smtplib
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)  # 设置为调试模式，console中显示
        print('成功3')
        smtp.connect('smtp.163.com', '25')  # 链接服务器，smtp地址+端口
        print('成功4')
        smtp.login('lius400@163.com', 'jRThjytr546783$')  # 登录，用户名+密码
        print('成功5')
        smtp.sendmail(sender, receiver, str(msg))  # 发送，from+to+内容
        smtp.quit()
        print('发送邮件成功')



# sender = 'lius400@163.com'
# receiver = 'lius400@hotmail.com'
# title = '测试文件'
# # attach_xlsx = 'C:/Users/Administrator/Desktop/laohuangli-testcase1.xlsx'
# # attach_jpg = 'C:/Users/Administrator/Desktop/接口测试框架.jpg'
#
# mail = SendMail()
# mail.send_mail(sender,receiver,title)
# # mail.send_mail(sender,receiver,title,attach_xlsx,attach_jpg)
