# coding: gbk
import datetime, time

'''
当前时间并且用指定格式显示
'''


def one():
    t = datetime.datetime.now()
    print(t)  # 2020-12-14 16:36:54.046271
    print(type(t))  # <class 'datetime.datetime'>

    style = t.strftime("%Y-%m-%d %H:%M:%S")
    print(style)  # 2020-12-14 16:38:07


# one()

def two():
    # 获取当前时间
    t = datetime.datetime.now()
    # 转时间戳
    mktime = time.mktime(t.timetuple())
    # 格式化时间戳为本地的时间，年月日，时分秒等信息
    date_array = datetime.datetime.fromtimestamp(mktime)
    # 格式化时间
    style = date_array.strftime("%Y-%m-%d %H:%M:%S")
    print(style)  # 2020-12-14 16:43:21
    # 使用datetime，指定utc时间，相差8小时
    date_array = datetime.datetime.utcfromtimestamp(mktime)
    style = date_array.strftime("%Y-%m-%d %H:%M:%S")
    print(style)  # 2020-12-14 08:43:21


# two()

'''
获取昨天日期
'''


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# 输出
# print(getYesterday())

'''
获取当前日期的时间戳，以及n天后的日期时间戳
'''


def get_current_time():
    # 当前时间
    now = datetime.datetime.now()
    # 格式化：用指定格式显示
    strftime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(strftime)
    # 格式化时间戳为本地的时间，年月日，时分秒等信息
    time_strptime = time.strptime(strftime, '%Y-%m-%d %H:%M:%S')
    # 转时间戳
    mktime = time.mktime(time_strptime)
    print(mktime)
    # 转毫秒级时间戳
    time_strptime_mill = str(mktime * 1000).split(".")[0]
    print(time_strptime_mill)


# get_current_time()

''' 
获取30天前/后的时间
    days=30
    days=-30
'''


def get_x_days_time():
    now = datetime.datetime.now()
    # 获取30天后的时间
    timedelta = datetime.timedelta(days=-30)
    now_timedelta = now + timedelta
    # 格式化：用指定格式显示
    timedelta_strftime = now_timedelta.strftime("%Y-%m-%d %H:%M:%S")
    print(timedelta_strftime)
    # 格式化时间戳为本地的时间，年月日，时分秒等信息
    time_strftime = time.strptime(timedelta_strftime, '%Y-%m-%d %H:%M:%S')
    print(time_strftime)
    # 转时间戳
    time_mktime = time.mktime(time_strftime)
    print(time_mktime)
    # 转毫秒级时间戳
    time_mktime__split___ = str((time_mktime * 1000)).split(".")[0]
    print(time_mktime__split___)


# get_x_days_time()
