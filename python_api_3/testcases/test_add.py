#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 作者：Fillico
# 日期：2019/4/20

import unittest
from python_api_3.common.http_request import HttpSessionRequest
from python_api_3.common import do_excel
from ddt import ddt, data
from python_api_3.common import do_mysql
from python_api_3.common.config import *
from python_api_3.common import context
from python_api_3.common import do_log

logs = do_log.DoLogs(do_log.log_file,'add')

@ddt
class AddTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'add')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logs.info("准备测试前置")
        cls.http_request = HttpSessionRequest()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_add(self, case):
        logs.info("开始执行测试：{}".format(case.title))
        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_request.session_request(case.method, case.url, case.data)
        print(type(eval(case.data)))

        print(case.title)
        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')

            # 加标成功之后，查询数据库，取到loan_id

            # 保存到类属性中
            # setattr(Context,"loan_id",loan_id)
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            logs.error('case:{},请求的数据:{},测试报错：{}'.format(case.title, case.data, e))
            raise e
        logs.info("结束测试：{}".format(case.title))

    @classmethod
    def tearDownClass(cls):
        cls.http_request.session_close()
        cls.mysql.close()
