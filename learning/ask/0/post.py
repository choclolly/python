"""
Python调用http请求--post
url
    https://blog.csdn.net/jiulanhao/article/details/88388304
"""
# 导入请求包
import requests
# 导入json包
import json

# 设置要访问的地址
url = 'http://hdh.tae-tea.net/yestae-community-api/api/TP0004'

# 定一个字典类型
mapA = {"jsurl": "http://localhost:8080", "sign": "9fe22d86c2cb4b60a9ad5fcc35b04ca9"}

# 把字典转成字符串
strMapA = json.dumps(mapA)

# 这里得给设置一个请求格式，不然会返回415
# header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
header_dict = {"Content-Type": "application/json; charset=utf8"}

print(strMapA)

# 直接请求
r = requests.post(url, data=strMapA, headers=header_dict)
# 这里是输出了一个字符串
print(r.text)
