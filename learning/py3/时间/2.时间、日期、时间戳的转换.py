# coding: gbk

# �ο� https://www.cnblogs.com/jfl-xx/p/8024596.html

import time
import datetime

'''
1,str����ʱ��תΪʱ���
'''
def one():
	# �ַ����͵�ʱ��
	date_1 = '2020-12-14 15:22:22'
	# תΪʱ������
	time_array = time.strptime(date_1,'%Y-%m-%d %H:%M:%S')
	# time.struct_time(tm_year=2020, tm_mon=12, tm_mday=14, tm_hour=15, tm_min=22, tm_sec=22, tm_wday=0, tm_yday=349,tm_isdst=-1)
	print(time_array)	
	# timeArray���Ե���tm_year��
	print(time_array.tm_year)   # 2020
	# תΪʱ���, ʮλ��ʱ���
	time_stamp = int(time.mktime(time_array))
	print(time_stamp)	# 1607930542

#one()


'''
2,����str�������ڵ���ʾ��ʽ
'''
def two():
	date_2 = '2020-12-14 15:22:22'
	# תΪʱ������
	time_array = time.strptime(date_2,'%Y-%m-%d %H:%M:%S')
	# תΪ������ʾ��ʽ
	other_style_time = time.strftime("%Y/%m/%d %H:%M:%S", time_array)
	# print(type(other_style_time)) # <class 'str'>
	print(other_style_time)	# 2020/12/14 15:22:22


	# תΪʱ������
	time_array = time.strptime(other_style_time,'%Y/%m/%d %H:%M:%S')
	# תΪ������ʾ��ʽ
	other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
	print(other_style_time)	# 2020-12-14 15:22:22

#two()


'''
3,ʱ���ת��Ϊָ����ʽ������
'''
# 3.1 ʹ��time
def three_1():
	time_stamp = time.time()
	# ��ʽ��ʱ���Ϊ���ص�ʱ�䣬�����գ�ʱ�������Ϣ
	f_time = time.localtime(time_stamp)
	# ��ʽ��ʱ��
	style = time.strftime("%Y--%m--%d %H:%M:%S", f_time)
	print(style)   # 2020--12--14 16:27:43

#three_1()

# 3.2 ʹ��datetime
def three_2():
	time_stamp = time.time()
	# ��ʽ��ʱ���Ϊ���ص�ʱ�䣬�����գ�ʱ�������Ϣ
	date_array = datetime.datetime.fromtimestamp(time_stamp)
	# ��ʽ��ʱ��
	style = date_array.strftime("%Y--%m--%d %H:%M:%S")
	print(style)   # 2020--12--14 16:27:43
	# ʹ��datetime��ָ��utcʱ�䣬���8Сʱ
	date_array = datetime.datetime.utcfromtimestamp(time_stamp)
	style = date_array.strftime("%Y--%m--%d %H:%M:%S")
	print(style)   # 2020--12--14 08:27:43

#three_2()

'''
4,��ȡ��ǰʱ�䲢����ָ����ʽ��ʾ
'''
# 4.1 # time��ȡ��ǰʱ���,ʮλ
def current_time_by_time():
	# time��ȡ��ǰʱ���,ʮλ
	now = int(time.time())     # 1533952277
	# ��ʽ��ʱ���Ϊ���ص�ʱ�䣬�����գ�ʱ�������Ϣ
	time_array = time.localtime(now)
	print(time_array)	# time.struct_time(tm_year=2020, tm_mon=12, tm_mday=14, tm_hour=16, tm_min=32, tm_sec=19, tm_wday=0, tm_yday=349, tm_isdst=0)
	# ��ʽ��ʱ��
	style = time.strftime("%Y--%m--%d %H:%M:%S", time_array)
	print(style)	# 2020--12--14 16:32:19

current_time_by_time()

# 4.2 datetime��ȡ��ǰʱ�䣬�����ʽ
def current_time_by_datetime():
	# datetime��ȡ��ǰʱ�䣬�����ʽ
	now = datetime.datetime.now()
	print(now)	# 2020-12-14 16:32:19.676008
	style = now.strftime("%Y--%m--%d %H:%M:%S")
	print(style)	# 2020--12--14 16:32:19

current_time_by_datetime()


