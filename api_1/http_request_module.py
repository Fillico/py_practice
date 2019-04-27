# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/3/13 13:32

#-------题目：
# 1：作业安排：
# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码

import requests
class HttpRequest:  #定义一个http请求的类，使用get和post请求时，返回响应数据
    def http_request(self,url,method="post",**kwargs):
        if method.upper()=='GET':
            resp = requests.get(url,params=None, **kwargs)
        elif method.upper()=='POST':
            resp = requests.post(url,data=None, json=None, **kwargs)
        return resp   #返回响应数据
if __name__=='__main__':
    url='http://test.lemonban.com//futureloan/mvc/api/member/register'
    params={'mobilephone':'18688773467','pwd':'123456'}
    login=HttpRequest()  #创建对象
    resu=login.http_request(url,params=params).json()  #对象调用类里面的http_request方法
    # print("状态码为：{}\n响应头为：{}\n响应报文为：{}".format(resu.status_code,resu.headers,resu.text))
    # print(type(resu))
    print(resu)
    print(resu['msg'])



