import p

p.prt(1, '斐波纳契数列')
'''
Fibonacci series: 斐波纳契数列
    两个元素的总和确定了下一个数
'''


def fibonacci_series():
    # 复合赋值
    a, b = 0, 1
    while b < 100:
        # end 关键字:可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
        print(b, end=",")
        # 复合赋值
        a, b = b, a + b


fibonacci_series()