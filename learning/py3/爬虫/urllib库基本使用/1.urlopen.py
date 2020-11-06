# 1,不加data是以GET方式发送，加data是以POST发送
import urllib.request

response = urllib.request.urlopen('http://www.cnblogs.com/0bug')
# .decode('utf-8') 解码
response = response.read().decode('utf-8')
# print(response)

# 2,加data发送POST请求
import urllib.parse
import urllib.request

# 2.1,无参数
data = bytes(urllib.parse.urlencode({}), encoding='utf-8')
response = urllib.request.urlopen('https://kill-rest-test.yestae.com/yestae-kill/K0003?ruleId=d21146012d26fc7e50b7119b9c6fff4f&'
                                  'goodsId=0c13ec10579a113e69cc2450d313faba&sign=b0b9e11b406254c4177546b1d0bdfaa8', data=data)
print(response.read().decode('utf-8'))

# 2.2,有参数
data = bytes(
    urllib.parse.urlencode({'ruleId': 'd21146012d26fc7e50b7119b9c6fff4f', 'goodsId': '0c13ec10579a113e69cc2450d313faba',
                            'sign': 'b0b9e11b406254c4177546b1d0bdfaa8'}), encoding='utf-8')
response = urllib.request.urlopen('https://kill-rest-test.yestae.com/yestae-kill/K0003', data=data)
print(response.read().decode('utf-8'))
