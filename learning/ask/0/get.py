"""
Python调用http请求--get
url
    https://blog.csdn.net/jiulanhao/article/details/88388304
"""
# 导入请求包
import requests
# 导入json包
import json

# 设置要访问的地址（这里是get请求）
url = 'http://hdh.tae-tea.net/yestae-community-api/teaPatry/wxConfig/?jsurl=http://localhost:8080&sign=9fe22d86c2cb4b60a9ad5fcc35b04ca9'
# 直接请求
r = requests.get(url)
# 这里是输出了一个字符串
print(r.text)
# 用自带的json工具把字符串转成字典
dictinfo = json.loads(r.text)

# 输出字典
print(dictinfo)
print(type(dictinfo))
# 用字典的方法获取值
print(dictinfo['datas'])
print(dictinfo['datas']['appid'])
