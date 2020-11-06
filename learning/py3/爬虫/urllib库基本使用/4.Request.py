import urllib.request

# 1.request
request = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 2.添加请求头信息
from urllib import request, parse

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Host': 'httpbin.org'
}
dic = {}
data = bytes(parse.urlencode(dic), encoding='utf-8')
req = request.Request(url=url, data=data, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
