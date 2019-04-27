# -*- coding:utf-8 -*-
#@author:Fillico
#@date:2019/4/10 14:29

from api_1.http_request_module import *

# #前程贷-注册接口
# register_params={"mobilephone":"13260032957","pwd":"123456","regname":"Fillico"}
# futureloan_register = HttpRequest("http://test.lemonban.com/futureloan/mvc/api/member/register",
#                                   register_params)
# resp=futureloan_register.http_request()
# print(resp.text)

#前程贷-登录接口
login_params = {"mobilephone":"13260032957","pwd":"123456"}
futureloan_login = HttpRequest()
resp_login = futureloan_login.http_request("http://test.lemonban.com/futureloan/mvc/api/member/login",
                                            data = login_params)
print(resp_login.cookies)

#前程贷-充值接口
recharge_params = {"mobilephone":"13260032957","amount":"2000"}
futureloan_recharge = HttpRequest()
resp_recharge = futureloan_recharge.http_request("http://test.lemonban.com/futureloan/mvc/api/member/recharge",
                                  data=recharge_params,
                                  cookies=resp_login.cookies)
print(resp_recharge.text)
