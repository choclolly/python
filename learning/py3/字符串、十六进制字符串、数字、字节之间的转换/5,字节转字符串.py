# coding: gbk

'''
���ݲ��䣬������ת�����������ڣ��ֽ� ת 16�����ַ���
	
'''
a = b'hello world'
print(type(a))	# <class 'bytes'>
print(a.decode('utf-8'))	# hello world
print(type(a.decode('utf-8')))	# <class 'str'>