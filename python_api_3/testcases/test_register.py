#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 作者：Fillico
# 日期：2019/4/20
import json
import unittest
from python_api_3.common.http_request import HttpSessionRequest
from python_api_3.common import do_excel
from ddt import ddt, data
from python_api_3.common import do_mysql
import random
from python_api_3.common.context import Context
from python_api_3.common import do_log
from python_api_3.common import contants

logs = do_log.DoLogs(do_log.log_file, 'register')


@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'register')
    cases = excel.get_cases()

    def setUp(self):
        logs.info("准备测试前置")
        self.http_request = HttpSessionRequest()
        self.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_register(self, case):
        logs.info("开始执行测试：{}".format(case.title))

        if case.data.find('register_mobile') > -1:
            # 查询最大手机号码,fetch_one()返回的是一个元组
            if case.sql is not None:
                max_phone = self.mysql.fetch_one(case.sql)['MAX(mobilephone)']
                print(max_phone)
                # max_phone = int(max_phone) + 1
                random_num = random.randint(1000, 9999)
                phone = int(max_phone) - random_num  # 用最大手机号减去一个随机数，生成一个新的手机号

                sql_phone = 'SELECT mobilephone FROM future.member where mobilephone={}'.format(phone)
                # #查询数据库中已注册的手机号，如果phone在数据库中已经存在 ，则phone+1
                res = do_mysql.DoMysql().fetch_one(sql_phone)
                if res is not None:
                    phone += 1
                setattr(Context, 'register_mobile', phone)
                case.data = case.data.replace('register_mobile', str(phone))
                print(case.data)

        resp = self.http_request.session_request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
            # 执行用例后，判断是否需要执行sql
            if case.sql is not None:
                self.assertEqual(getattr(Context, 'register_mobile'), int(json.loads(case.data)['mobilephone']))
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            logs.error('case:{},请求的数据:{},测试报错：{}'.format(case.title, case.data, e))
            raise e
        logs.info("结束测试：{}".format(case.title))

    def tearDown(self):
        self.http_request.session_close()
        self.mysql.close()
