# https://blog.csdn.net/h836384379/article/details/105731991/

import datetime
import time

# 1,datetime.datetime.now()
start = datetime.datetime.now()
# long running (运行代码区）
end = datetime.datetime.now()
# 直接输出end-start格式为'HH:mm:SS'
print((end - start).total_seconds())

# 2,time.time()
start = time.time()
# long running (运行代码区）
end = time.time()
print(end - start)

# 3,me.process_time()
start = time.process_time()
# long running (运行代码区）
end = time.process_time()
print(end - start)
