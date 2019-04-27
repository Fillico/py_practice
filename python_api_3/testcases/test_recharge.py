# -*- coding:utf-8 -*-
# @author:Fillico
# @date:2019/4/18 11:15

import unittest
from python_api_3.common.http_request import HttpSessionRequest
from python_api_3.common import do_excel
from python_api_3.common import do_mysql
from python_api_3.common import contants
from ddt import ddt, data
from python_api_3.common import context
from python_api_3.common import do_log

logs = do_log.DoLogs(do_log.log_file, 'recharge')

@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'recharge')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logs.info("准备测试前置")
        cls.http_request = HttpSessionRequest()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_recharge(self, case):
        logs.info("开始执行测试：{}".format(case.title))
        # 执行用例前判断是否需要执行sql
        # if case.sql is not None:
        #     sql = eval(case.sql)['sql1']
        #     member = self.mysql.fetch_one(sql)
        #     print(member['leaveamount'])
        #     before = member['leaveamount']

        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)
        print(case.data)
        sql = "SELECT * FROM future.member WHERE mobilephone = '{}';".format(eval(case.data)['mobilephone'])
        print(sql)
        member = self.mysql.fetch_one(sql)
        if member is not None:
            print(member['leaveamount'])
            before = member['leaveamount']

        resp = self.http_request.session_request(case.method, case.url, case.data)

        # actual_code = resp.json()['code']   #判断code时，从excel表里面读取的期望值要加个str.因为读取的是int类型。str(case.expected)
        actual_msg = resp.json()['msg']

        try:
            self.assertEqual(case.expected, actual_msg)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
            # 成功之后，判断是否需要执行sql
            # if case.sql is not None:
            #     sql = eval(case.sql)['sql1']
            #     member = self.mysql.fetch_one(sql)
            #     print(member['leaveamount'])
            #     after = member['leaveamount']
            #     self.assertEqual(before+int(eval(case.data)['amount']),after)
            if actual_msg == '充值成功':
                sql = "SELECT * FROM future.member WHERE mobilephone='{}';".format(eval(case.data)['mobilephone'])
                print(sql)
                member = self.mysql.fetch_one(sql)
                print(member['leaveamount'])
                after = member['leaveamount']
                self.assertEqual(float(before) + float(eval(case.data)['amount']), float(after))
                logs.debug('case:{},请求的数据:{},测试通过'.format(case.title, case.data))
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            logs.error('case:{},请求的数据:{},测试报错：{}'.format(case.title, case.data, e))
            raise e
        logs.info("结束测试：{}".format(case.title))

    @classmethod
    def tearDownClass(cls):
        cls.http_request.session_close()
