# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/3/22 14:08

import unittest
import HTMLTestRunnerNew
from week6.lesson_0328 import login_testcases

suite=unittest.TestSuite()

#loader通过模块来加载
from week6.lesson_0328 import login_testcases
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(login_testcases))

#执行用例
# runner=unittest.TextTestRunner()
# runner.run(suite)

#执行测试用例，并把结果输出到html文件中
with open('test_Fillico.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='20190325-测试报告',
        description='测试http_request请求',
        tester='Fillico')
    runner.run(suite)
