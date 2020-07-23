# https://www.cnblogs.com/ShawSpring/p/10555063.html


# 要实现累加，关键在于数据存在哪儿，怎么使每次累加的都是同一个变量 行为像静态变量

# 前两种都是数据存到类的成员变量，
# 类利用__call__
class foo:
    def __init__(self, n=0):
        self.n = n

    def __call__(self, i):
        self.n += i
        return self.n


a = foo()
print(a(1), a(2), a(3), a(4))  # 1 3 6 10


# 函数中定义类，返回一个实例的成员函数
def foo2(n=0):
    class acc:
        def __init__(self, s):
            self.s = s

        def inc(self, i):
            self.s += i
            return self.s

    return acc(n).inc


a = foo2()
print(a(1), a(2), a(3), a(4))


# 闭包 私以为最好用
def foo3():
    count = 0

    def f(n):
        nonlocal count
        count += n
        return count

    return f


a = foo3()
print(a(1), a(2), a(3), a(4))


# 奇淫技巧吧，又不是c，没必要管什么堆内存
def foo4(i, L=[]):
    if len(L) == 0:
        L.append(0)
    L[0] += i
    return L[0]


print(foo4(1), foo4(4), foo4(5))
