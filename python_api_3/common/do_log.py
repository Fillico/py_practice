# -*- coding:utf-8 -*-
# @author:Fillico
# @date:2019/4/26 13:08

import logging
import os
from python_api_3.common.contants import *
from python_api_3.common.config import *


class DoLogs:
    def __init__(self, file_path, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(config.get('LOG', 'level_1'))
        formatter = logging.Formatter(config.get('LOG', 'formatter'))

        # 日志输出到文件
        fh = logging.FileHandler(filename=file_path, encoding='utf-8')
        fh.setLevel(config.get('LOG', 'level_2'))
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

log_file = os.path.join(contants.log_dir, 'test_future.log')
# logs = DoLogs(log_file)

if __name__ == '__main__':
    print(log_file)
    # logs = DoLogs('os.path','register')
    # DoLogs(log_file,'log').debug('输出debug级别日志')
    # logs.info('输出info级别日志')
    # logs.warning('输出warning级别日志')
    # logs.error('输出error级别日志')
    # logs.critical('输出critical级别日志')
