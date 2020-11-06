'''
面向对象
    Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的
面向对象技术简介
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    方法：类中定义的函数。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    局部变量：定义在方法中的变量，只作用于当前实例的类。
    实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
    和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
对象可以包含任意数量和类型的数据。
'''
'''
    类定义
        class ClassName:
        <statement-1>
        .
        .
        .
        <statement-N>
        类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。
    
    类对象
        类对象支持两种操作：
            属性引用
            实例化。
        属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
        类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
'''

''' 类定义:一个简单的类实例'''


class MyClass:
    i = 12345

    def f(self):
        return "hello world" + ',' + str(self.i)


print('---------')
print('1,一个简单的类实例')
# 实例化类
x = MyClass()
# 属性引用:访问类的属性和方法
print("     MyClass 类的属性 i 为：", x.i)  # MyClass 类的属性 i 为： 12345
print("     MyClass 类的方法 f 输出为：", x.f())  # MyClass 类的方法 f 输出为： hello world,12345

'''
__init__()
    类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
        x = MyClass()
    当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
    '''

'''类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用'''


class MyClassTwo:
    i = 12345

    def __init__(self):
        self.i = 54321

    def f(self):
        return "hello world" + ',' + str(self.i)


print('---------')
print('2,类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用:x = MyClassTwo()')
# x = MyClassTwo() 实例化类 MyClassTwo，对应的 __init__() 方法就会被调用
x = MyClassTwo()
print("     MyClassTwo 类的属性 i 为：", x.i)  # MyClass 类的属性 i 为： 54321
print("     MyClassTwo 类的方法 f 输出为：", x.f())  # MyClass 类的方法 f 输出为： hello world,54321

'''当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上'''


class MyClassThree:
    i = 12345

    def __init__(self, name, age):
        self.i = 54321
        self.name = name
        self.age = age

    def f(self):
        return "     hello world" + ',' + str(self.i) + ',' + str(self.name) + ',' + str(self.age)


print('---------')
print('3,__init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上')
# x = MyClassThree() 实例化类 MyClassThree，对应的 __init__() 方法就会被调用
x = MyClassThree(10, 20)
print("     MyClassThree 类的属性 i 为：", x.i)  # MyClass 类的属性 i 为： 54321
print("     MyClassThree 类的方法 f 输出为：", x.f())  # MyClass 类的方法 f 输出为： hello world,54321

'''
self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
'''


class Test:
    def prt(self):
        print('     self 代表的是类的实例:{}'.format(self))  # <__main__.Test object at 0x00D08388>
        print('     self.class 则指向类:{}'.format(self.__class__))  # __main__.Test


print('---------')
print('4,self代表类的实例，而非类 \
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self')
x = Test()
x.prt()

'''从Test类的执行结果:
    可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
    self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的
'''


class TestTwo:
    def prt(runoob):
        print('     runoob 代表的是类的实例:{}'.format(runoob))  # <__main__.Test object at 0x00D08388>
        print('     runoob.class 则指向类:{}'.format(runoob.__class__))  # __main__.Test


print('---------')
print('5,self代表类的实例，而非类 \
代表当前对象的地址，而 self.class 则指向类。\
    self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的,不过我们习惯使用self')
x = Test()
x.prt()

'''
类的方法
    在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
'''


# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    # 定义类的方法
    def speak(self):
        print('     %s 说:我 %s 岁,体重 %s 公斤' % (self.name, self.age, self.__weight))


print('---------')
print('6,类的方法')
x = People("nana", 3.5, 14.5)
x.speak()  # nana 说:我 3.5 岁,体重 14.5 公斤

'''
继承
    Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
        class DerivedClassName(BaseClassName1):
        <statement-1>
        .
        .
        .
        <statement-N>
    BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
'''


# 单继承示例
class Strdent(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        super().__init__(n, a, w)
        self.grade = g

    def speak(self):
        # 调用父类方法
        super().speak()
        # 覆写父类的方法
        print("     %s 说: 我 %s 岁了，我在读 %s 年级" % (self.name, self.age, self.grade))


print('---------')
print('7,单继承示例')
x = Strdent('mumna', 3.5, 14.5, '小1班')
x.speak()

'''
多继承
    Python同样有限的支持多继承形式。多继承的类定义形如下例:
        class DerivedClassName(Base1, Base2, Base3):
        <statement-1>
        .
        .
        .
        <statement-N>
    需要注意圆括号中父类的顺序，
        若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''


# 另一个类，多重继承之前的准备
class Speaker:
    topic = ''
    name = ''

    def __init__(self, t, n):
        self.topic = t
        self.name = n

    def speak(self):
        print("     我叫 %s，我是一个演说家，我演讲的主题是: %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, People):

    def __init__(self, n, a, w, t):
        super().__init__(t, n)

    def speak(self):
        super().speak()


print('---------')
print('8,多继承示例1:方法名同，子类使用时未指定,默认调用的是在括号中排前地父类的方法')
x = Sample('nn', 3.5, 14.5, '观察小蚂蚁')
x.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

'''
方法重写
    如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
'''


class Animal:
    def prt(self):
        print('调用父类方法')


class Cat(Animal):
    def prt(self):
        # '调用父类方法
        super().prt()
        print('调用子类方法')


print('---------')
print('9,方法重写,如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法')
c = Cat()  # 子类实例
c.prt()  # 子类调用重写方法
super(Cat, c).prt()  # 用子类对象调用父类已被覆盖的方法

'''
类属性与方法
    类的私有属性
        __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
    类的方法
        在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
        self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
    类的私有方法
        __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
    类的专有方法：
        __init__ : 构造函数，在生成对象时调用
        __del__ : 析构函数，释放对象时使用
        __repr__ : 打印，转换
        __setitem__ : 按照索引赋值
        __getitem__: 按照索引获取值
        __len__: 获得长度
        __cmp__: 比较运算
        __call__: 函数调用
        __add__: 加运算
        __sub__: 减运算
        __mul__: 乘运算
        __truediv__: 除运算
        __mod__: 求余运算
        __pow__: 乘方
'''

'''类的私有属性实例'''


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


print('---------')
print('10,类的私有属性实例')
counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量,AttributeError: 'JustCounter' object has no attribute '__secretCount'


'''类的私有方法实例'''

print('---------')
print('11,类的私有方法实例')


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    @staticmethod
    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错


'''运算符重载'''


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


print('---------')
print('12,运算符重载')
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
