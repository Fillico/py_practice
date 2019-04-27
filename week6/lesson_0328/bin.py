#!/usr/bin/python3
#-*- coding:utf-8 -*-
#作者：Fillico
#日期：2019/3/30

#这是函数入口，主要功能是发送邮件，通过DDT和配置文件，读取excel中的用例，测试之前写的http_request请求

from week6.lesson_0328.send_email_class import *

if __name__ == '__main__':
    from week6.lesson_0328 import learn_config

    sender = learn_config.MyConfig('les_0319.conf').get_strValue("EMAIL", 'email_name')
    pwd = learn_config.MyConfig('les_0319.conf').get_strValue('EMAIL', 'email_pwd')
    my_email = SendEmail(sender, pwd, '13260032957@163.com')  # 创建SendEmail对象
    # 对象调用send_email方法，send_email方法调用email_content的返回值，并添加两个附件
    my_email.send_email(my_email.email_content('测试报告', """<p style="color:red"> 你好:</p>
       <p style="color:red"> 附件为测试说明和测试报告 </p>
       """, 'test_demo.txt', 'test_Fillico.html'))