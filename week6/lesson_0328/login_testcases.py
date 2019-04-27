# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/3/22 10:43

import requests
from week6.lesson_0328.http_request_0312 import *
import unittest
from ddt import ddt,data,unpack
from week6.lesson_0328.read_write_excel import ReadWriteExcel

@ddt
class TestHttpRequest(unittest.TestCase):
    '''
    定义一个类，每条用例作为一个列表，其中的params参数用一个字典存储
    '''
    test_data=ReadWriteExcel('login_cases.xlsx','Sheet1').read_excel()
    @data(*test_data)
    @unpack
    def test_001(self,url,params,expected,method='get'):
        res = HttpRequest(url,eval(params),method).http_request().json()  #将响应数据转换为字典格式
        print(res) #打印实际结果，在生成的测试报告详情中可以看到
        # print("expected:",expected)
        # print("url:",url)
        # print('params:',params)
        # print('method:',method)
        self.assertEqual(expected, res["msg"])

