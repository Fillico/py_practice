# -*- coding:utf-8 -*-
# @author:Fillico
# @date:2019/4/26 11:09

import HTMLTestRunnerNew
import os
import unittest
from python_api_3.common import contants
from python_api_3.testcases import test_login, test_recharge, test_add, test_bidLoan

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_register_2))
# suite.addTest(loader.loadTestsFromModule(test_login))
# suite.addTest(loader.loadTestsFromModule(test_recharge))
# suite.addTest(loader.loadTestsFromModule(test_add))
# suite.addTest(loader.loadTestsFromModule(test_bidLoan))

discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")

# 执行测试用例，并把结果输出到html文件中

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_file = os.path.join(base_dir, 'reports', 'test_future.html')

with open(html_file, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='20190426-前程贷测试报告',
        description='前程贷测试报告',
        tester='Fillico')
    runner.run(discover)
