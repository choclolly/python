import p
import sys

p.prt(1, '迭代器是Python最强大的功能之一，是访问集合元素的一种方式')
'''
迭代器
    迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    字符串，列表或元组对象都可用于创建迭代器
迭代器对象可以使用常规for语句进行遍历
可以使用 next() 函数
'''


# 实例
def iter_instance():
    list = [1, 2, 3, 4, 5, 6]
    it = iter(list)
    print(it)

    print(next(it), end=",")  # 1
    print(next(it))  # 2

    '''迭代器对象可以使用常规for语句进行遍历：'''
    for x in it:
        print(x, end=",")  # 3,4,5,6,

    '''可以使用 next() 函数'''
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()


# iter_instance()


p.prt(2, '创建一个迭代器')
'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
    如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
    更多内容查阅：Python3 面向对象:https://www.runoob.com/python3/python3-class.html
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
'''


class Num:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


x = Num()
it = iter(x)
# print(next(it))
# print(next(it))
# print(next(it))

p.prt(3, 'StopIteration,触发 StopIteration 异常来结束迭代:raise StopIteration')
'''
StopIteration
    StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后
    触发 StopIteration 异常来结束迭代。
'''


class Num_1:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


x = Num_1()
it = iter(x)
# for y in it:
#     print(y)

p.prt(4, '生成器')
'''
生成器
    在 Python 中，使用了 yield 的函数被称为生成器（generator）。
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
    调用一个生成器函数，返回的是一个迭代器对象。
'''


# 生成器函数 - 斐波那契
def yield_instance(x):
    a, b, counter = 0, 1, 0
    while True:
        if counter > x:
            return
        yield a
        a, b = b, a + b
        # 计数器
        counter += 1


x = yield_instance(20)  # x 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(x), end=",")
    except StopIteration:
        sys.exit()
