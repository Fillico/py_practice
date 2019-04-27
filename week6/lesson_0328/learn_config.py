# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/3/18 9:15

from configparser import ConfigParser

class MyConfig:
    '''
    定义一个配置文件的类，根据不同类型(int/float/bool/str)获取不同类型的配置文件
    '''
    def __init__(self,conf_filepath,encoding='utf-8'):
        '''

        :param conf_filepath: 配置文件的路径
        :param encoding: 文件编码格式
        '''
        self.cf=ConfigParser()
        self.cf.read(conf_filepath,encoding)
    def get_sections(self): #获取配置文件所有的区
        return self.cf.sections()
    def get_options(self,section):#获取指定分区的所有项
        return self.cf.options(section)
    def get_intValue(self,section,option):#获取int类型的数据
        return self.cf.getint(section,option)
    def get_floatValue(self,section,option):#获取float类型的数据
        return self.cf.getfloat(section,option)
    def get_boolValue(self,section,option):#获取bool类型的数据
        return self.cf.getboolean(section,option)
    def get_strValue(self,section,option):#获取str类型的数据
        return self.cf.get(section,option)
if __name__ == '__main__':  #测试代码
    # my_conf=MyConfig('demo.conf')
    # print(my_conf.get_sections())
    # print(my_conf.get_options('db'))
    # print(my_conf.get_intValue('db','db_port'))
    # print(my_conf.get_floatValue('db','db_port'))
    # print(my_conf.get_strValue('user_info','sex'))
    my_conf = MyConfig('les_0319.conf')
    print(my_conf.get_strValue('LOG','level_2'))
    # print(my_conf.get_sections())

