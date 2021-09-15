# coding: gbk

'''
内容不变，将类型转换——区别于：字节 转 16进制字符串

先转 字符串 再转字节
'''
a = 521
print(type(a))	# <class 'int'>
print(str(a))	# 521
print(type(str(a)))	# <class 'str'>
print(str(a).encode())	# b'521'