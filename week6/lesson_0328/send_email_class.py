#!/usr/bin/python3
#-*- coding:utf-8 -*-
#作者：Fillico
#日期：2019/3/30

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class SendEmail:
    '''
    创建一个类，发送邮件，并可以上传多个附件，通过for遍历附件，分别加入到邮件中
    '''
    def __init__(self,sender,pwd,receiver):
        '''
        :param sender: 邮件发送者
        :param pwd: 邮件密码
        :param receiver: 邮件接收者
        '''
        self.sender=sender
        self.pwd=pwd
        self.receiver=receiver

    def email_content(self,subject,msg_content,*filename):
        '''
        这是一个添加邮件主题、正文、附件的函数，可以添加多个附件
        :param subject: 邮件主题
        :param msg_content: 邮件正文
        :param *filename:邮件的附件
        :return: 邮件的主题、正文和附件
        '''
        msg_total=MIMEMultipart()
        msg_total['Subject']=subject
        msg = MIMEText(msg_content,'html')
        msg_total.attach(msg) #将测试正文添加到邮件中
        if len(filename)>=1:   #如果测试附件等于或多于1个，通过for遍历文件，分别添加到正文中
            for i in range(1,len(filename)+1):
                file = MIMEApplication(open(filename[i-1],'rb').read())
                file.add_header('content-disposition','attachment',filename=filename[i-1])
                msg_total.attach(file)
        return msg_total

    def send_email(self,msg):
        server=smtplib.SMTP_SSL('smtp.163.com',465)
        server.login(self.sender,self.pwd)
        server.sendmail(self.sender,self.receiver,msg.as_string())
        server.quit()

if __name__ == '__main__':
    from week6.lesson_0328 import learn_config
    sender=learn_config.MyConfig('les_0319.conf').get_strValue("EMAIL",'email_name')
    pwd =learn_config.MyConfig('les_0319.conf').get_strValue('EMAIL', 'email_pwd')
    my_email=SendEmail(sender,pwd,'13260032957@163.com') #创建SendEmail对象
    #对象调用send_email方法，send_email方法调用email_content的返回值，并添加两个附件
    my_email.send_email(my_email.email_content('测试报告',"""<p style="color:red"> 你好:</p>
    <p style="color:red"> 附件为测试说明和测试报告 </p>
    """,'test_demo.txt','test_Fillico.html'))
