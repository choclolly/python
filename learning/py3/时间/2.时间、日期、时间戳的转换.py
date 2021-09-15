# coding: gbk

# 参考 https://www.cnblogs.com/jfl-xx/p/8024596.html

import time
import datetime

'''
1,str类型时间转为时间戳
'''
def one():
	# 字符类型的时间
	date_1 = '2020-12-14 15:22:22'
	# 转为时间数组
	time_array = time.strptime(date_1,'%Y-%m-%d %H:%M:%S')
	# time.struct_time(tm_year=2020, tm_mon=12, tm_mday=14, tm_hour=15, tm_min=22, tm_sec=22, tm_wday=0, tm_yday=349,tm_isdst=-1)
	print(time_array)	
	# timeArray可以调用tm_year等
	print(time_array.tm_year)   # 2020
	# 转为时间戳, 十位数时间戳
	time_stamp = int(time.mktime(time_array))
	print(time_stamp)	# 1607930542

#one()


'''
2,更改str类型日期的显示格式
'''
def two():
	date_2 = '2020-12-14 15:22:22'
	# 转为时间数组
	time_array = time.strptime(date_2,'%Y-%m-%d %H:%M:%S')
	# 转为其它显示格式
	other_style_time = time.strftime("%Y/%m/%d %H:%M:%S", time_array)
	# print(type(other_style_time)) # <class 'str'>
	print(other_style_time)	# 2020/12/14 15:22:22


	# 转为时间数组
	time_array = time.strptime(other_style_time,'%Y/%m/%d %H:%M:%S')
	# 转为其它显示格式
	other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
	print(other_style_time)	# 2020-12-14 15:22:22

#two()


'''
3,时间戳转换为指定格式的日期
'''
# 3.1 使用time
def three_1():
	time_stamp = time.time()
	# 格式化时间戳为本地的时间，年月日，时分秒等信息
	f_time = time.localtime(time_stamp)
	# 格式化时间
	style = time.strftime("%Y--%m--%d %H:%M:%S", f_time)
	print(style)   # 2020--12--14 16:27:43

#three_1()

# 3.2 使用datetime
def three_2():
	time_stamp = time.time()
	# 格式化时间戳为本地的时间，年月日，时分秒等信息
	date_array = datetime.datetime.fromtimestamp(time_stamp)
	# 格式化时间
	style = date_array.strftime("%Y--%m--%d %H:%M:%S")
	print(style)   # 2020--12--14 16:27:43
	# 使用datetime，指定utc时间，相差8小时
	date_array = datetime.datetime.utcfromtimestamp(time_stamp)
	style = date_array.strftime("%Y--%m--%d %H:%M:%S")
	print(style)   # 2020--12--14 08:27:43

#three_2()

'''
4,获取当前时间并且用指定格式显示
'''
# 4.1 # time获取当前时间戳,十位
def current_time_by_time():
	# time获取当前时间戳,十位
	now = int(time.time())     # 1533952277
	# 格式化时间戳为本地的时间，年月日，时分秒等信息
	time_array = time.localtime(now)
	print(time_array)	# time.struct_time(tm_year=2020, tm_mon=12, tm_mday=14, tm_hour=16, tm_min=32, tm_sec=19, tm_wday=0, tm_yday=349, tm_isdst=0)
	# 格式化时间
	style = time.strftime("%Y--%m--%d %H:%M:%S", time_array)
	print(style)	# 2020--12--14 16:32:19

current_time_by_time()

# 4.2 datetime获取当前时间，数组格式
def current_time_by_datetime():
	# datetime获取当前时间，数组格式
	now = datetime.datetime.now()
	print(now)	# 2020-12-14 16:32:19.676008
	style = now.strftime("%Y--%m--%d %H:%M:%S")
	print(style)	# 2020--12--14 16:32:19

current_time_by_datetime()


