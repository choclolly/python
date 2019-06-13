"""
传递表单
通常，你想要发送一些编码为表单形式的数据—非常像一个HTML表单。 要实现这个，只需简单地传递一个字典给 data 参数。
你的数据字典 在发出请求时会自动编码为表单形式:
"""
import requests

# 测试域名
# domain_name='https://test-api.yestae.com/api'
# 开发域名
# domain_name='http://hdh.tae-tea.net/yestae-community-api'
domain_name = 'http://localhost/yestae-community-api'
# 获取活动详情
url = domain_name + '/api/TP0001'

# payload = {'activityId': '5ce384680b76d7812af1bab4', 'sign': '955e2772300ca1f8d614e13d8438538d',
#            'location': '{"lon":116.353408,"lat":40.083555}', 'uid': '', 'sid': '', }
payload = {'activityId': '5ce3b39222ec00c3f8b779c2', 'sign': '5482ca4ab93ae7299d684ac8abe8aec0',
           'location': '{"lon":116.353408,"lat":40.083555}', 'uid': '', 'sid': '', }
r = requests.post(url, data=payload)
print(r.status_code)
print(r.json())
# 活动报名
# url = domain_name+'/api/TP0002'
#
# payload = {'uid': '1123058830953328642', 'activityId': '5ce384680b76d7812af1bab4', 'num': 1,
#            'sign': 'ca436df0f9bbb4a11fda587c88ee1c66', }
# r = requests.post(url, data=payload)
# print(r.status_code)
# print(r.json())
#
# # 获取活动列表
# url = url = domain_name+'/api/TP0003'
#
# payload = {'uid': '1123058830953328642', 'sign': '83ff323b2efa5b042b876bc524f6175f', }
# r = requests.post(url, data=payload)
# print(r.status_code)
# print(r.json())
#
# # 获取wx权限验证配置属性
# url = url = domain_name+'/api/TP0004'
#
# payload = {'jsurl': 'http://localhost:8080', 'sign': '9fe22d86c2cb4b60a9ad5fcc35b04ca9', 'key3': None}
# r = requests.post(url, data=payload)
# print(r.status_code)
# print(r.json())
