"""
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