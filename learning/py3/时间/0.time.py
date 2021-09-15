# coding: gbk

# 参考 https://blog.csdn.net/qq_36512295/article/details/99694528

'''
符号	意义
	%y	两位数的年份（00-99）
	%Y	四位数的年份（000-9999）
	%m	月份（01-12）
	%d	日（0-31）
	%H	24小时制（0-23）
	%I	12小时制（01-12）
	%M	分（00-59）
	%S	秒（00-59）
	%a	简化星期名称（示例：Sat）
	%A	完整星期名称（示例：Saturday）
	%b	简化月份名称（示例：Aug）
	%B	完整月份名称（示例：August）
	%c	日期和时间（示例：Sat Aug 17 15:55:44 2019）
	%x	日期（示例：08/17/19）
	%X	时间（示例：15:59:31）
	%j	年内第几天（001-366）
	%p	A.M.或P.M.
	%U	年内第几个星期，星期天为星期的开始（00-53）
	%W	年内第几个星期，星期一为星期的开始（00-53）
	%w	星期，星期天为星期的开始（0-6）
	%z	GMT时区信息（示例：+0800，表示中国标准时间，正8时区）
	%Z	失去名称（Python3，Windows下乱码，未解决）
	%%	%
'''

import time

'''
0. 获取当前系统时间13位时间戳
'''
def thirteen_byte():
	t = time.time()
	print(t)			# 1607932987.1427777
	print(type(t))		# <class 'float'>
	print(int(t * 1000)) # 1607932987142

# thirteen_byte()

'''
1. time.time()
	返回当前时间戳，值为按秒计算的浮点数
	表示从1970年1月1日0点0分开始，到当前时间，一共经历了多少秒
'''
def time_time():
	print(time.time()) # 1607931541.6668549

#time_time()

'''
2. time.localtime()
	格式化时间戳为本地的时间，年月日，时分秒等信息
	若未输入参数，默认当前时间
'''
def time_localtime():
	# time.struct_time(tm_year=2020, tm_mon=12, tm_mday=14, tm_hour=15, tm_min=42, tm_sec=28, tm_wday=0, tm_yday=349, tm_isdst=0)
	t = time.localtime()
	print(t)
	print(type(t))	# <class 'time.struct_time'>
	# 年, 月, 日
	print(t.tm_year, t.tm_mon, t.tm_mday) # 2020 12 14
	# 时, 分, 秒
	print(t.tm_hour, t.tm_min, t.tm_sec)
	# 本周的第几天， 本年的第几天
	print(t.tm_wday,  t.tm_yday)
	# 夏时令（夏天时将时间快调一小时，中国于1992年暂停实行）
	print(t.tm_isdst)

#time_localtime()

'''
3. time.asctime()
	格式化时间
	若未输入参数，默认当前时间
'''
def time_asctime():
	print(time.asctime())	# Mon Dec 14 15:48:52 2020
	t = time.localtime(time.time())
	print(time.asctime(t))	# Mon Dec 14 15:48:52 2020
	print(time.asctime(time.localtime()))	# Mon Dec 14 15:48:52 2020

#time_asctime()

'''
4. time.strftime()
		格式化时间
'''
def time_strftime():
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))	# 2020-12-14 15:50:57
	print(time.strftime('%a %b %d %H:%M:%S %Y', time.time()))	# Mon Dec 14 15:50:57 2020

#time_strftime()

'''
5. time.mktime()
	将格式字符串转换为时间戳（按秒计算的浮点数）
'''
def time_mktime():
	print(time.mktime(time.localtime()))  # 1607932401.0

#time_mktime()

'''
6. time.ctime()
	把时间戳（按秒计算的浮点数）转化为 time.asctime() 形式。
	若未输入参数或参数为 None，默认 time.time()，即当前时间，相当于 time.asctime(time.localtime())
'''

def time_ctime():
	print(time.ctime())						# Mon Dec 14 15:55:59 2020
	print(time.ctime(None))					# Mon Dec 14 15:55:59 2020
	print(time.ctime(time.time()))			# Mon Dec 14 15:55:59 2020
	print(time.asctime(time.localtime()))	# Mon Dec 14 15:55:59 2020

#time_ctime()