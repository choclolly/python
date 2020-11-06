import random
import datetime

from dateutil.relativedelta import relativedelta

# uuid study
import uuid

ID = str(uuid.uuid1()).replace('-', '')
print(ID)

# time study
import time

f = time.time()
current_time = int(f * 1000)  # 当前时间
# query_user_vas_sql = 'SELECT user_id FROM uc_vas_record WHERE end_time > %d AND STOP = 0 AND invalid = 0 AND added_service_id = %s' % current_time% 'e0316f1b70784d26924e09bc18a92fb8'
query_user_vas_sql = 'SELECT user_id FROM uc_vas_record WHERE end_time > %d AND STOP = 0 AND invalid = 0 AND added_service_id = \'%s\'' % (
    current_time, "e0316f1b70784d26924e09bc18a92fb8")
print(query_user_vas_sql)

print(f)
print("f类型:", type(f))  # f类型: <class 'float'>
print("--------------------------------------------------------------------------------------")
print("time.time(): %f " % time.time())  # 1601354006.944756
localtime = time.localtime(time.time())
print("localtime:{}".format(localtime))
print("年:", localtime.tm_year)
print("月:", localtime.tm_mon)
print("日:", localtime.tm_mday)
asctime = time.asctime(localtime)
print("asctime:{}".format(asctime))

print("--------------------------------------------------------------------------------------")
# 10位时间戳
time = round(f)
time = round(f)
print(time)
print("time类型:", type(time))  # time类型: <class 'int'>
print("--------------------------------------------------------------------------------------")
# 13位时间戳
time = round(f * 1000)  # round() 方法返回浮点数 x 的四舍五入值
print(time)
time = int(f * 1000)
print(time)
