# coding: gbk

a = b's'
print(type(a))	# <class 'bytes'>
print(a.hex())	# 73, s ��Ӧ��16�������� 0X73
print(type(a.hex()))	# <class 'str'>

'''
�����ŵĴ���
	SyntaxError: unexpected EOF while parsing
'''