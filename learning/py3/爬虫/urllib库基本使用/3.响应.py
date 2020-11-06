import urllib.request

# 1.响应类型
response = urllib.request.urlopen('http://www.baidu.com')
print(type(response))  # <class 'http.client.HTTPResponse'>

# 2.状态码、响应头
print(response.status)
print(response.getheaders())
print(response.getheader('Content-Type'))

# 3.响应体:响应体是字节流，需要解码decode('utf-8'),否则输出的中文是进制形式
response = response.read().decode('utf-8')
# print(response)
