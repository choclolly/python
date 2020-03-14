"""
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
字符串的截取的语法格式如下：
    变量[头下标:尾下标]
加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数
"""

s = 'Runoob'

print(s)  # 输出字符串
print(s[0:-1])  # 输出第一个到倒数第二个的所有字符
print(s[0])  # 输出字符串第一个字符
print(s[2:5])  # 输出从第三个开始到第五个的字符
print(s[2:])  # 输出从第三个开始的后的所有字符
print(s * 2)  # 输出字符串两次，也可以写成 print (2 * s) 
print(s + "TEST")  # 连接字符串

'''
Runoob
Runoo
R
noo
noob
RunoobRunoob
RunoobTEST
'''


