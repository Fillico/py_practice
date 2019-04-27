# -*- coding:utf-8 -*-
# @author:Fillico
# @date:2019/4/15 9:51

import requests
from python_api_3.common.config import config
from python_api_3.common import do_log

logs = do_log.DoLogs(do_log.log_file, 'http_request')


class HttpRequest:
    def http_request(self, method, url, data=None, json=None):
        try:
            if method.upper() == "GET":
                resp = requests.get(url, params=data)
            elif method.upper() == "POST":
                if json:
                    resp = requests.post(url, json=json)
                else:
                    resp = requests.post(url, data=data)
            else:
                print("不支持的请求方式")
            print("请求的response:", resp.text)
            return resp
        except Exception as e:
            raise e


class HttpSessionRequest:
    '''定义一个类，通过session直接传递cookie,不用再单独传递cookie'''

    def __init__(self):
        self.session = requests.sessions.session()

    def session_request(self, method, url, data=None, json=None):

        if type(data) == str:
            data = eval(data)

        # 拼接请求的url
        url = config.get('api', 'pre_url') + url
        logs.debug("请求的data：{}".format(data))
        try:
            if method.upper() == 'GET':
                resp = self.session.request(method=method, url=url, params=data)
            elif method.upper() == 'POST':
                if json:
                    resp = self.session.request(method=method, url=url, json=json)
                else:
                    resp = self.session.request(method=method, url=url, data=data)
            else:
                logs.error("不支持的请求方式")
        except Exception as e:
            logs.error("请求出错:{}".format(e))
            raise e

        return resp

    def session_close(self):
        self.session.close()


if __name__ == '__main__':
    http_re = HttpRequest()
    params = {"mobilephone": "13660000111", "pwd": "12345678"}
    resp = http_re.http_request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/register', data=params)
    # params2 = {"mobilephone": "13660000110", "amount": "5000"}
    # resp2 = http_re.session_request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params2)
    print(resp.text)
