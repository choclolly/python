# coding: gbk
import datetime, time

'''
��ǰʱ�䲢����ָ����ʽ��ʾ
'''


def one():
    t = datetime.datetime.now()
    print(t)  # 2020-12-14 16:36:54.046271
    print(type(t))  # <class 'datetime.datetime'>

    style = t.strftime("%Y-%m-%d %H:%M:%S")
    print(style)  # 2020-12-14 16:38:07


# one()

def two():
    # ��ȡ��ǰʱ��
    t = datetime.datetime.now()
    # תʱ���
    mktime = time.mktime(t.timetuple())
    # ��ʽ��ʱ���Ϊ���ص�ʱ�䣬�����գ�ʱ�������Ϣ
    date_array = datetime.datetime.fromtimestamp(mktime)
    # ��ʽ��ʱ��
    style = date_array.strftime("%Y-%m-%d %H:%M:%S")
    print(style)  # 2020-12-14 16:43:21
    # ʹ��datetime��ָ��utcʱ�䣬���8Сʱ
    date_array = datetime.datetime.utcfromtimestamp(mktime)
    style = date_array.strftime("%Y-%m-%d %H:%M:%S")
    print(style)  # 2020-12-14 08:43:21


# two()

'''
��ȡ��������
'''


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# ���
# print(getYesterday())

'''
��ȡ��ǰ���ڵ�ʱ������Լ�n��������ʱ���
'''


def get_current_time():
    # ��ǰʱ��
    now = datetime.datetime.now()
    # ��ʽ������ָ����ʽ��ʾ
    strftime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(strftime)
    # ��ʽ��ʱ���Ϊ���ص�ʱ�䣬�����գ�ʱ�������Ϣ
    time_strptime = time.strptime(strftime, '%Y-%m-%d %H:%M:%S')
    # תʱ���
    mktime = time.mktime(time_strptime)
    print(mktime)
    # ת���뼶ʱ���
    time_strptime_mill = str(mktime * 1000).split(".")[0]
    print(time_strptime_mill)


# get_current_time()

''' 
��ȡ30��ǰ/���ʱ��
    days=30
    days=-30
'''


def get_x_days_time():
    now = datetime.datetime.now()
    # ��ȡ30����ʱ��
    timedelta = datetime.timedelta(days=-30)
    now_timedelta = now + timedelta
    # ��ʽ������ָ����ʽ��ʾ
    timedelta_strftime = now_timedelta.strftime("%Y-%m-%d %H:%M:%S")
    print(timedelta_strftime)
    # ��ʽ��ʱ���Ϊ���ص�ʱ�䣬�����գ�ʱ�������Ϣ
    time_strftime = time.strptime(timedelta_strftime, '%Y-%m-%d %H:%M:%S')
    print(time_strftime)
    # תʱ���
    time_mktime = time.mktime(time_strftime)
    print(time_mktime)
    # ת���뼶ʱ���
    time_mktime__split___ = str((time_mktime * 1000)).split(".")[0]
    print(time_mktime__split___)


# get_x_days_time()
