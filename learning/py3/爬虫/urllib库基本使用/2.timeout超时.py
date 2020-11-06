import socket
import urllib.error
import urllib.request
import urllib.parse

timeout = 0.01  # 请求超时
# timeout = 0.1  # 正常输出

# try except捕获超时异常
try:
    data = bytes(
        urllib.parse.urlencode(
            {'ruleId': 'd21146012d26fc7e50b7119b9c6fff4f', 'goodsId': '0c13ec10579a113e69cc2450d313faba',
             'sign': 'b0b9e11b406254c4177546b1d0bdfaa8'}), encoding='utf-8')
    response = urllib.request.urlopen('https://kill-rest-test.yestae.com/yestae-kill/K0003', data=data, timeout=timeout)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('请求超时')
