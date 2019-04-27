# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/4/18 14:09

import configparser
from python_api_3.common import contants


class ReadConfig:
    '''
    完成配置文件的读取
    '''
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file)  #先加载global
        switch = self.config.getboolean('switch','on')
        if switch:  #
            self.config.read(contants.online_file,encoding='utf-8')
        else:
            self.config.read(contants.test_file,encoding='utf-8')

    def get(self,section,option):
        return self.config.get(section,option)

    def set(self, section, option, value=None):
        self.config.set(section,option,value)

config = ReadConfig()

# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api','pre_url'))

