# coding: gbk

a = b's'
print(type(a))	# <class 'bytes'>
print(a.hex())	# 73, s 对应的16进制数是 0X73
print(type(a.hex()))	# <class 'str'>

'''
少括号的错误
	SyntaxError: unexpected EOF while parsing
'''