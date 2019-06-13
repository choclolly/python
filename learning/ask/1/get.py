import requests

url = 'http://hdh.tae-tea.net/yestae-community-api/teaPatry/wxConfig/'
payload = {'jsurl': 'http://localhost:8080', 'sign': '96e79218965eb72c92a549dd5a330112', 'key3': None}
r = requests.get(url, params=payload, stream=True)
'''
r.text 返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
r.content返回二进制结果
r.json()返回JSON格式，可能抛出异常
r.status_code
r.raw返回原始socket respons，需要加参数stream=True
    response = requests.get(url, params=payload, stream=True)
    经测试python3 加不加无所谓
'''
print(r.text)
print(r.content)
print(r.json())
print(r.status_code)
print(r.raw)

'''
输出：
{"datas":{"signature":"eac164a95cfcf60dd862835027c983dc3a08f76f","appid":"wx4d92796730d1c47b","noncestr":"GhBei0iCZijVfpd2wGPS","timestamp":"1558080622108"},"returnCode":"system.success","returnMsg":"操作成功","succeed":1}
b'{"datas":{"signature":"eac164a95cfcf60dd862835027c983dc3a08f76f","appid":"wx4d92796730d1c47b","noncestr":"GhBei0iCZijVfpd2wGPS","timestamp":"1558080622108"},"returnCode":"system.success","returnMsg":"\xe6\x93\x8d\xe4\xbd\x9c\xe6\x88\x90\xe5\x8a\x9f","succeed":1}'
{'datas': {'signature': 'eac164a95cfcf60dd862835027c983dc3a08f76f', 'appid': 'wx4d92796730d1c47b', 'noncestr': 'GhBei0iCZijVfpd2wGPS', 'timestamp': '1558080622108'}, 'returnCode': 'system.success', 'returnMsg': '操作成功', 'succeed': 1}
200
<urllib3.response.HTTPResponse object at 0x000002A2CB897A20>
'''