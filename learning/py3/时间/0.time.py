# coding: gbk

# �ο� https://blog.csdn.net/qq_36512295/article/details/99694528

'''
����	����
	%y	��λ������ݣ�00-99��
	%Y	��λ������ݣ�000-9999��
	%m	�·ݣ�01-12��
	%d	�գ�0-31��
	%H	24Сʱ�ƣ�0-23��
	%I	12Сʱ�ƣ�01-12��
	%M	�֣�00-59��
	%S	�루00-59��
	%a	���������ƣ�ʾ����Sat��
	%A	�����������ƣ�ʾ����Saturday��
	%b	���·����ƣ�ʾ����Aug��
	%B	�����·����ƣ�ʾ����August��
	%c	���ں�ʱ�䣨ʾ����Sat Aug 17 15:55:44 2019��
	%x	���ڣ�ʾ����08/17/19��
	%X	ʱ�䣨ʾ����15:59:31��
	%j	���ڵڼ��죨001-366��
	%p	A.M.��P.M.
	%U	���ڵڼ������ڣ�������Ϊ���ڵĿ�ʼ��00-53��
	%W	���ڵڼ������ڣ�����һΪ���ڵĿ�ʼ��00-53��
	%w	���ڣ�������Ϊ���ڵĿ�ʼ��0-6��
	%z	GMTʱ����Ϣ��ʾ����+0800����ʾ�й���׼ʱ�䣬��8ʱ����
	%Z	ʧȥ���ƣ�Python3��Windows�����룬δ�����
	%%	%
'''

import time

'''
0. ��ȡ��ǰϵͳʱ��13λʱ���
'''
def thirteen_byte():
	t = time.time()
	print(t)			# 1607932987.1427777
	print(type(t))		# <class 'float'>
	print(int(t * 1000)) # 1607932987142

# thirteen_byte()

'''
1. time.time()
	���ص�ǰʱ�����ֵΪ�������ĸ�����
	��ʾ��1970��1��1��0��0�ֿ�ʼ������ǰʱ�䣬һ�������˶�����
'''
def time_time():
	print(time.time()) # 1607931541.6668549

#time_time()

'''
2. time.localtime()
	��ʽ��ʱ���Ϊ���ص�ʱ�䣬�����գ�ʱ�������Ϣ
	��δ���������Ĭ�ϵ�ǰʱ��
'''
def time_localtime():
	# time.struct_time(tm_year=2020, tm_mon=12, tm_mday=14, tm_hour=15, tm_min=42, tm_sec=28, tm_wday=0, tm_yday=349, tm_isdst=0)
	t = time.localtime()
	print(t)
	print(type(t))	# <class 'time.struct_time'>
	# ��, ��, ��
	print(t.tm_year, t.tm_mon, t.tm_mday) # 2020 12 14
	# ʱ, ��, ��
	print(t.tm_hour, t.tm_min, t.tm_sec)
	# ���ܵĵڼ��죬 ����ĵڼ���
	print(t.tm_wday,  t.tm_yday)
	# ��ʱ�����ʱ��ʱ����һСʱ���й���1992����ͣʵ�У�
	print(t.tm_isdst)

#time_localtime()

'''
3. time.asctime()
	��ʽ��ʱ��
	��δ���������Ĭ�ϵ�ǰʱ��
'''
def time_asctime():
	print(time.asctime())	# Mon Dec 14 15:48:52 2020
	t = time.localtime(time.time())
	print(time.asctime(t))	# Mon Dec 14 15:48:52 2020
	print(time.asctime(time.localtime()))	# Mon Dec 14 15:48:52 2020

#time_asctime()

'''
4. time.strftime()
		��ʽ��ʱ��
'''
def time_strftime():
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))	# 2020-12-14 15:50:57
	print(time.strftime('%a %b %d %H:%M:%S %Y', time.time()))	# Mon Dec 14 15:50:57 2020

#time_strftime()

'''
5. time.mktime()
	����ʽ�ַ���ת��Ϊʱ������������ĸ�������
'''
def time_mktime():
	print(time.mktime(time.localtime()))  # 1607932401.0

#time_mktime()

'''
6. time.ctime()
	��ʱ������������ĸ�������ת��Ϊ time.asctime() ��ʽ��
	��δ������������Ϊ None��Ĭ�� time.time()������ǰʱ�䣬�൱�� time.asctime(time.localtime())
'''

def time_ctime():
	print(time.ctime())						# Mon Dec 14 15:55:59 2020
	print(time.ctime(None))					# Mon Dec 14 15:55:59 2020
	print(time.ctime(time.time()))			# Mon Dec 14 15:55:59 2020
	print(time.asctime(time.localtime()))	# Mon Dec 14 15:55:59 2020

#time_ctime()