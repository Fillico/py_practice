# -*- coding:utf-8 -*-
# @author:Fillico
# @date:2019/4/17 18:12

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

case_file = os.path.join(base_dir, 'data', 'future_cases.xlsx')
print(case_file)

global_file = os.path.join(base_dir, 'config', 'global.conf')
print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')
print(test_file)

log_dir = os.path.join(base_dir, 'log')
print(log_dir)

case_dir = os.path.join(base_dir,'testcases')
