import time
import datetime

millis_time = int(round(time.time() * 1000))
print(millis_time)

print(round(time.time() * 1000))
print(type(round(time.time() * 1000)))

start_time = round(time.time() * 1000)

end_time = round(time.time() * 1000)
print("耗时:{}".format(end_time - start_time))

start = datetime.datetime.now()
# long running (运行代码区）
end = datetime.datetime.now()
# 直接输出end-start格式为'HH:mm:SS'
print((end - start).total_seconds())


# 闭包 私以为最好用
def foo3():
    count = 0

    def f(n):
        nonlocal count
        count += n
        return count

    return f


a = foo3()
print(a(1), a(1), a(1), a(1))
print(a(1))
