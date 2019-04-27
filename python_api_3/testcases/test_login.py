# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/4/18 9:50

import unittest
from python_api_3.common.http_request import HttpSessionRequest
from python_api_3.common import do_excel
from python_api_3.common import contants
from ddt import ddt,data
from python_api_3.common import context
from python_api_3.common import do_log

logs = do_log.DoLogs(do_log.log_file,'login')

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logs.info("准备测试前置")
        cls.http_request = HttpSessionRequest()

    @data(*cases)
    def test_login(self,case):
        logs.info("开始执行测试：{}".format(case.title))
        case.data = context.replace(case.data)
        resp = self.http_request.session_request(case.method,case.url,case.data)
        print(case.data)
        logs.debug('输出debug级别日志')
        logs.info('输出info级别日志')
        logs.warning('输出warning级别日志')
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            logs.error('case:{},请求的数据:{},测试报错：{}'.format(case.title, case.data, e))
            raise e
        logs.info("结束测试：{}".format(case.title))
    @classmethod
    def tearDownClass(cls):
        cls.http_request.session_close()
