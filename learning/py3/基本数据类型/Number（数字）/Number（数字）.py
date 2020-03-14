"""
Python3 支持
    int、float、bool、complex（复数）。
在Python 3里，
    只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
    到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
像大多数语言一样，数值类型的赋值和计算都是很直观的。
查询变量所指的对象类型
    内置的 type() 函数可以用来查询变量所指的对象类型。
    此外还可以用 isinstance 来判断

    isinstance 和 type 的区别在于：
        type()不会认为子类是一种父类类型。
        isinstance()会认为子类是一种父类类型。
"""
print('======type')
# type()
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))  # <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

print('======isinstance')
# isinstance
a = 1
print(isinstance(a, int))  # True

print('======区别')


# 区别
class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # True
print(type(A()) == A)  # True

print(isinstance(B(), A))  # True
print(type(B) == A)  # False






