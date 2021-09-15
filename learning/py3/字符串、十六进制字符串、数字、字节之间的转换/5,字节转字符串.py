# coding: gbk

'''
内容不变，将类型转换——区别于：字节 转 16进制字符串
	
'''
a = b'hello world'
print(type(a))	# <class 'bytes'>
print(a.decode('utf-8'))	# hello world
print(type(a.decode('utf-8')))	# <class 'str'>