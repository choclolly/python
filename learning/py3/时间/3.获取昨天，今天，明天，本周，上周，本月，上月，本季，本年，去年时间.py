import datetime
from datetime import timedelta
import calendar
import time

'''
参考：https://zhuanlan.zhihu.com/p/95919866

如果要获取到date的格式，在最后加上".date"

now不设置默认为取当前时间
'''
def get_datetime():
    # 当前时间
    # 返回datetime格式 : 2020-12-15 14:45:41.249300
    now = datetime.datetime.now()
    print(type(now))
    print('当前时间:{}'.format(now))
    # 返回datetime格式 : 2020-12-15
    date = datetime.datetime.now().date()
    print('当前时间:{}'.format(date))
    date_today = datetime.date.today()
    print('当前时间:{}'.format(date_today))
    # 当前时间戳
    mktime = time.mktime(now.timetuple())
    print('当前时间戳1:{}'.format(mktime))       # 当前时间戳1:1608085912.0
    time_time = time.time()
    print('当前时间戳2:{}'.format(time_time))    # 当前时间戳2:1608085912.5727699

    # 自定义时间戳 1639277075000 = 2021-12-12 10:44:35
    mktime = 1639277075000 / 1000
    # 格式化时间戳为本地的时间，年月日，时分秒等信息,时间戳转<class 'datetime.datetime'>类型
    now = datetime.datetime.fromtimestamp(mktime)
    print(type(now))

    # 今天
    today = now
    print('今天:{}'.format(today))

    # 昨天
    yesterday = now - timedelta(days=1)
    print('昨天:{}'.format(yesterday))

    # 明天
    tomorrow = now + timedelta(days=1)
    print('明天:{}'.format(tomorrow))

    # 当前季度
    now_quarter = now.month / 3 if now.month % 3 == 0 else now.month / 3 + 1
    print('当前季度:{}'.format(int(now_quarter)))

    # 本周第一天和最后一天
    this_week_start = now - timedelta(days=now.weekday())
    this_week_end = now + timedelta(days=6 - now.weekday())
    print('本周第一天:{}'.format(this_week_start))
    print('本周最后一天:{}'.format(this_week_end))

    # 上周第一天和最后一天
    last_week_start = now - timedelta(days=now.weekday() + 7)
    last_week_end = now - timedelta(days=now.weekday() + 1)
    print('上周第一天:{}'.format(last_week_start))
    print('上周最后一天:{}'.format(last_week_end))

    # 本月第一天和最后一天
    this_month_start = datetime.datetime(now.year, now.month, 1)
    this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
    print('本月第一天:{}'.format(this_month_start))
    print('本月最后一天:{}'.format(this_month_end))

    # 上月第一天和最后一天
    last_month_end = this_month_start - timedelta(days=1)
    last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)
    print('上月第一天:{}'.format(last_month_start))
    print('上月最后一天:{}'.format(last_month_end))

    # 本季第一天和最后一天
    month = (now.month - 1) - (now.month - 1) % 3 + 1
    this_quarter_start = datetime.datetime(now.year, month, 1)
    this_quarter_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
    print('本季第一天:{}'.format(this_quarter_start))
    print('本季最后一天:{}'.format(this_quarter_end))

    # 上季第一天和最后一天
    last_quarter_end = this_quarter_start - timedelta(days=1)
    last_quarter_start = datetime.datetime(last_quarter_end.year, last_quarter_end.month - 2, 1)
    print('上季第一天:{}'.format(last_quarter_start))
    print('上季最后一天:{}'.format(last_quarter_end))

    # 本年第一天和最后一天
    this_year_start = datetime.datetime(now.year, 1, 1)
    this_year_end = datetime.datetime(now.year + 1, 1, 1) - timedelta(days=1)
    print('本年第一天:{}'.format(this_year_start))
    print('本年最后一天:{}'.format(this_year_end))

    # 去年第一天和最后一天
    last_year_end = this_year_start - timedelta(days=1)
    last_year_start = datetime.datetime(last_year_end.year, 1, 1)
    print('去年第一天:{}'.format(last_year_start))
    print('去年最后一天:{}'.format(last_year_end))


    


get_datetime()
