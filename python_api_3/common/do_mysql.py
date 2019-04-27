#!/usr/bin/python3
#-*- coding:utf-8 -*-
#作者：Fillico
#日期：2019/4/19

import pymysql
from python_api_3.common.config import *

class DoMysql:
    def __init__(self):
        '''
        # 完成与MySQL数据库的交互，从配置文件读取数据库信息
        # :param host: 连接的数据库
        # :param user: 用户名
        # :param password: 密码
        # :param port: 端口号
        # '''
        host = config.get('db','host')
        user = config.get('db','user')
        password = config.get('db','password')
        port = config.get('db','port')

        #1.创建连接
        #mysql,实例化的时候还可以加一个参数，指定返回字典格式cursorclass = pymysql.cursors.DictCursor
        self.mysql = pymysql.connect(host=host, user=user, password=password,port=int(port))
        #设置返回字典
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)# 2.新建一个查询页面，以字典格式返回

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    # def commit(self):
    #     self.mysql.commit()

    def close(self):
        self.cursor.close()
        self.mysql.close()

# mysql = DoMysql(host=config.get('db','host'),user=config.get('db','user'),password=config.get('db','password'),port=int(config.get('db','port')))
# # sql = 'SELECT * FROM test.tdb_goods'
# sql = 'SELECT max(mobilephone) from future.member'
# res=mysql.fetch_one(sql)
# print(res)