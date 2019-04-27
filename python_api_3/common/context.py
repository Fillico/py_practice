#!/usr/bin/python3
#-*- coding:utf-8 -*-
#author:Fillico
#date:2019/4/20
#function:

import re
from python_api_3.common.config import *

class Context:
    load_id = None
    register_mobile = None
    member_id = None
    before = None
    mobilephone = None

def replace(data):
    pattern = '#(.*?)#'
    while re.search(pattern,data):
        # print(data)
        match_data = re.search(pattern, data)
        match_data_key = match_data.group(1)
        try:
            match_data_value = config.get('data', match_data_key)  #根据key取配置文件里面的值
        except configparser.NoOptionError as e:
            if hasattr(Context,match_data_key):
                getattr(Context,match_data_key)
            else:
                print("找不到参数化的值")
                raise e
        # print(match_data_value)
        # 记得替换后的内容，继续用data接收
        data = re.sub(pattern, match_data_value, data, count=1)
    return data



