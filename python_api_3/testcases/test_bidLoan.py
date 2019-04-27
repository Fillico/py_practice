# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/4/25 17:06

import unittest
from python_api_3.common.http_request import HttpSessionRequest
from python_api_3.common import do_excel
from python_api_3.common import do_mysql
from ddt import ddt,data
from python_api_3.common import context
from python_api_3.common.config import *
from python_api_3.common import do_log

logs = do_log.DoLogs(do_log.log_file, 'bidLoan')

@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'bidLoan')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logs.info("准备测试前置")
        cls.http_request = HttpSessionRequest()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_recharge(self,case):
        logs.info("开始执行测试：{}".format(case.title))

        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)

        resp = self.http_request.session_request(case.method,case.url,case.data)
        if resp.json()['msg'] =='登录成功':
            setattr(context.Context,'mobilephone',eval(case.data)['mobilephone'])
            sql = "SELECT * FROM future.member WHERE mobilephone='{}';".format(eval(case.data)['mobilephone'])
            print(sql)
            member = self.mysql.fetch_one(sql)
            if member is not None:
                print(member['leaveamount'])
                print(member['id'])
                # before = member['leaveamount']
                setattr(context.Context,'before',member['leaveamount'])
                setattr(context.Context,'member_id',member['id'])
                config.set('data','member_id',str(member['id']))
        if resp.json()['msg'] == '加标成功':
            sql = "SELECT * FROM future.loan WHERE memberid= (SELECT id FROM future.member WHERE mobilephone='{}') ORDER BY id DESC LIMIT 1".format(
                getattr(context.Context,'mobilephone'))
            loan_id = self.mysql.fetch_one(sql)['id']
            print("标的id:", loan_id)
            setattr(context.Context,'loan_id',loan_id)
            config.set('data','loan_id',str(loan_id))

        # actual_code = resp.json()['code']   #判断code时，从excel表里面读取的期望值要加个str.因为读取的是int类型。str(case.expected)

        try:
            self.assertEqual(case.expected,resp.json()['msg'])
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
            logs.info('case:{},请求的数据:{},测试通过'.format(case.title, case.data))
            if resp.json()['msg'] == '竞标成功':
                sql = "SELECT * FROM future.loan WHERE id={}".format(getattr(context.Context,'loan_id'))
                after = self.mysql.fetch_one(sql)['amount']

            if resp.json()['msg'] == '充值成功':
                sql = "SELECT * FROM future.member WHERE mobilephone='{}';".format(eval(case.data)['mobilephone'])
                print(sql)
                member = self.mysql.fetch_one(sql)
                print(member['leaveamount'])
                after = member['leaveamount']
                self.assertEqual(float(getattr(context.Context,'before')) + float(eval(case.data)['amount']), float(after))
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            logs.error('case:{},请求的数据:{},测试报错：{}'.format(case.title, case.data, e))
            raise e
        logs.info("结束测试：{}".format(case.title))
    @classmethod
    def tearDownClass(cls):
        cls.http_request.session_close()


