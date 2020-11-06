
'''
基本数据类型
'''

print('---------')
print('1,变量赋值')


def basic_data_type():
    counter = 100  # 整形变量 int
    miles = 1000.0  # 浮点型变量 float
    name = 'haodonghui'  # 字符串变量 str
    print(counter)
    print(miles)
    print(name)


# basic_data_type()

'''
多个变量赋值
    Python允许你同时为多个变量赋值
        a = b = c = 100
    您也可以为多个对象指定多个变量
        a, b, c = 1, 2, "haodonghui"
'''


def multiple_variable_assignment():
    a = b = c = 100
    print(a)
    print(c)
    print(b)

    a, b, c = 1, 2, "haodonghui"
    print(a, end=",")
    print(c, end=",")
    print(b)


# multiple_variable_assignment()

'''
标准数据类型  
    Python3 中有六个标准的数据类型：
        Number（数字）
        String（字符串）
        List（列表）
        Tuple（元组）
        Set（集合）
        Dictionary（字典）
        Python3 的六个标准数据类型中：
        
        不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
        可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''

'''
Number（数字）
    Python3 支持 int、float、bool、complex（复数）。
    在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    像大多数语言一样，数值类型的赋值和计算都是很直观的。
        内置的 type() 函数可以用来查询变量所指的对象类型。
        此外还可以用 isinstance 来判断：
    数值运算
        +       # 加法
        -       # 减法
        *       # 乘法
        /       # 除法，得到一个浮点数
        //      # 除法，得到一个整数
        %       # 取余
        **      # 乘方
    注意：
        1、Python可以同时为多个变量赋值，如a, b = 1, 2。
        2、一个变量可以通过赋值指向不同类型的对象。
        3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
        4、在混合计算时，Python会把整型转换成为浮点数
'''

'''type()'''

print('---------')
print('2,Number（数字）')


def type_():
    a, b, c, d = 1, 1.1, False, 1 + 2j
    print(type(a), type(b), type(c), type(d))  # <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

    '''
        当你指定一个值时，Number 对象就会被创建：
        您也可以使用del语句删除一些对象引用:
            del var1[,var2[,var3[....,varN]]]
            
    '''
    # del 删除多个对象引用
    del a, c
    print(type(b), type(d))  # <class 'float'> <class 'complex'>
    # del 删除单个对象引用
    del d
    print(type(b))


# type_()

'''isinstance'''


def isinstance_():
    i = 1
    instance = isinstance(i, int)
    print(instance)


# _isinstance()

'''
isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
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

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        super().__init__(n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %s 年级" % (self.name, self.age, self.grade))


s = Student('nannan', 3.5, 14.8, '小1班')
# s.speak()  # nannan 说: 我 3 岁了，我在读 小1班 年级

'''isinstance()会认为子类是一种父类类型。'''


def isinstance_(arg1, arg2):
    print(isinstance(arg1, arg2))


# isinstance_(People('nn', 3.5, 96), People)  # True
# isinstance_(Student('nn', 3.5, 96, 1), People)  # True

'''type()不会认为子类是一种父类类型。'''


def type_(arg1, arg2):
    print(type(arg1) == type(arg2))


# type_(People('nn', 3.5, 96), People)    # False
# type_(Student('nn', 3.5, 96, 1), Student)   # False

print('---------')
print('3,String（字符串）')
'''
String（字符串）
    Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
    字符串的截取的语法格式如下：
        变量[头下标:尾下标]
        索引值以 0 为开始值，-1 为从末尾的开始位置。
            从后面索引           -4      -3      -2      -1                      
            从前面索引           0       1       2       3
            
                                h       a       o       d
                                
            从前面截取           1       2       3       4
            从后面截取           -4      -3      -2      -1
    注意：
        1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
        2、字符串可以用+运算符连接在一起，用*运算符重复。
        3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
        4、Python中的字符串不能改变。

'''


def str_():
    s = 'haodonghui'
    print(s[:])  # 输出字符串                                  haodonghui
    print(s)  # 输出字符串                                     haodonghui
    print(s[0:-1])  # 输出第一个到倒数第二个的所有字符            haodonghu
    print(s[0])  # 输出字符串第一个字符                         h
    print(s[-1])  # 输出字符串倒数第一个字符                     i
    print(s[2:5])  # 输出从第三个开始到第五个的字符               odo
    print(s[2:])  # 输出从第三个开始的后的所有字符                odonghui
    print(s * 2)  # 输出字符串两次，也可以写成 print (2 * str)   haodonghuihaodonghui
    print(s + ",TEST")  # 连接字符串                           haodonghui,TEST


# str_()

'''
\n:特殊字符,换行
    Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 ""..."" 跨越多行。
注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
'''


def 反斜杠():
    print('hao\ndonghui')  # hao
    # donghui
    print(r'hao\ndonghui')  # hao\ndonghui

    s = '反斜杠(\)可以作为续行符，' \
        '表示下一行是上一行的延续。也可以使用'
    print(s)
    s1 = """反斜杠(\)可以作为续行符，表示下一行是上一行的延续。' ...
        也可以使用"""
    print(s1)

    s2 = '''反斜杠(\)可以作为续行符，表示下一行是上一行的延续。' ...
            也可以使用'''
    print(s2)


# 反斜杠()

print('---------')
print('4,List（列表）')
'''
List（列表）
    List（列表） 是 Python 中使用最频繁的数据类型。
    列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
    列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
    和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
    列表截取的语法格式如下：
        变量[头下标:尾下标]
            索引值以 0 为开始值，-1 为从末尾的开始位置
            t = ['a','b','c','d','e']
            索引  0    1   2   3   4
                -5   -4  -3  -2   -1
    加号 + 是列表连接运算符，
    星号 * 是重复操作
    Python 列表截取可以接收第三个参数，参数作用是截取的步长
        t = ['a','b','c','d','e']
        t[1:4:2]
        
        如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
'''


def list_():
    list = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinylist = [123, 'runoob']

    print(list)  # 输出完整列表                      ['abcd', 786, 2.23, 'runoob', 70.2]
    print(list[0])  # 输出列表第一个元素                 abcd
    print(list[1:3])  # 从第二个开始输出到第三个元素         [786, 2.23]
    print(list[2:])  # 输出从第三个元素开始的所有元素       [2.23, 'runoob', 70.2]
    print(tinylist * 2)  # 输出两次列表                       [123, 'runoob', 123, 'runoob']
    print(list + tinylist)  # 连接列表                          ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']


# list_()

# 与Python字符串不一样的是，列表中的元素是可以改变的：
def list_2():
    list = [1, 2, 3, 4, 5, 6]
    list[0] = 9
    list[2:5] = [13, 14, 15]
    print(list)  # [9, 2, 13, 14, 15, 6]

    list[2:5] = []
    print(list)  # [9, 2, 6]


# list_2()

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
def list_3():
    t = ['a', 'b', 'c', 'd', 'e']
    t_ = t[1:4:2]
    print(t_)  # ['b', 'd']


# list_3()

'''如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：'''


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


words = reverseWords('I like this')
# print(words)    # this like I

print('---------')
print('5,List（列表）')
'''
Tuple（元组）
    元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
    元组中的元素类型也可以不相同：
    
    加号 + 是列表连接运算符，
    星号 * 是重复操作
    
    元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取。
    其实，可以把字符串看作一种特殊的元组。
    
    注意：
        1、与字符串一样，元组的元素不能修改。
        2、元组也可以被索引和切片，方法一样。
        3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
            tup = ()
            tup = (20,)
        4、元组也可以使用+操作符进行拼接。

'''


def tuple_0():
    tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
    tinytuple = (123, 'runoob')

    print(tuple)  # 输出完整元组        ('abcd', 786, 2.23, 'runoob', 70.2)
    print(tuple[0])  # 输出元组的第一个元素    abcd
    print(tuple[1:3])  # 输出从第二个元素开始到第三个元素  (786, 2.23)
    print(tuple[2:])  # 输出从第三个元素开始的所有元素   (2.23, 'runoob', 70.2)
    print(tinytuple * 2)  # 输出两次元组      (123, 'runoob', 123, 'runoob')
    print(tuple + tinytuple)  # 连接元组    ('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')


# tuple_0()

# 修改元组元素的操作是非法的
def tuple_1():
    tup = (1, 2, 3, 4, 5, 6)
    print(tup[0])
    # tup[0] = 11   # 修改元组元素的操作是非法的:TypeError: 'tuple' object does not support item assignment


# tuple_1()

'''
    虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
    构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
'''


def c_tuple():
    tup = ()  # 空元组
    tup2 = (20,)  # 一个元素，需要在元素后添加逗号
    print(tup)
    print(tup2)


# c_tuple()


print('---------')
print('6,Set（集合）')
'''
Set（集合）
    集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
    基本功能是进行成员关系测试和删除重复元素。
    可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
    创建格式：
        parame = {value01,value02,...}
        或者
        set(value)
'''


# 创建set集合
def c_set():
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Baidu'}
    # set是无序的
    print(sites)  # 输出集合，重复的元素被自动去掉 {'Facebook', 'Google', 'Runoob', 'Baidu', 'Zhihu', 'Taobao'}

    # 成员测试
    if 'Runoob' in sites:
        print('Runoob 在集合中')
    else:
        print('Runoob 不在集合中')


# c_set()


# set可以进行集合运算
def set_arithmetic():
    a = set('abracadabra')
    b = set('alacazam')

    print(a)  # 去重    {'r', 'c', 'a', 'b', 'd'}
    print(b)  # 去重    {'c', 'a', 'z', 'm', 'l'}
    print(a - b)  # a 和 b 的差集               {'r', 'b', 'd'}
    print(a | b)  # a 和 b 的并集               {'r', 'c', 'a', 'b', 'd', 'l', 'z', 'm'}
    print(a & b)  # a 和 b 的交集               {'c', 'a'}
    print(a ^ b)  # a 和 b 中不同时存在的元素     {'r', 'b', 'l', 'd', 'z', 'm'}


# set_arithmetic()

print('---------')
print('7,Dictionary（字典）')
'''
Dictionary（字典）
    字典（dictionary）是Python中另一个非常有用的内置数据类型。
    列表和字典
        列表是有序的对象集合，字典是无序的对象集合。
        两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
    字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
    键(key)必须使用不可变类型。
    在同一个字典中，键(key)必须是唯一的。
    
    另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
    注意：
        1、字典是一种映射类型，它的元素是键值对。
        2、字典的关键字必须为不可变类型，且不能重复。
        3、创建空字典使用 { }。
'''


def c_dict_0():
    # dict = {}
    # dict['one'] = "1 - 菜鸟教程"
    # dict[2] = "2 - 菜鸟工具"
    dict = {'one': "1 - 菜鸟教程", 2: "2 - 菜鸟工具"}

    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

    dict_null = {}  # 创建空字典使用 { }

    print(dict['one'])  # 输出键为 'one' 的值     1 - 菜鸟教程
    print(dict[2])  # 输出键为 2 的值         2 - 菜鸟工具
    print(tinydict)  # 输出完整的字典           {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
    print(tinydict.keys())  # 输出所有键             dict_keys(['name', 'code', 'site'])
    print(tinydict.values())  # 输出所有值           dict_values(['runoob', 1, 'www.runoob.com'])


# c_dict_0()

print('---------')
print('8,Python数据类型转换')
'''
Python数据类型转换
    有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
    以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
        
            函数	                                            描述
        int(x [,base])                                  将x转换为一个整数
        float(x)                                        将x转换到一个浮点数
        complex(real [,imag])                           创建一个复数
        str(x)                                          将对象 x 转换为字符串
        repr(x)                                         将对象 x 转换为表达式字符串
        eval(str)                                       用来计算在字符串中的有效Python表达式,并返回一个对象
        tuple(s)                                        将序列 s 转换为一个元组
        list(s)                                         将序列 s 转换为一个列表
        set(s)                                          转换为可变集合
        dict(d)                                         创建一个字典。d 必须是一个 (key, value)元组序列。
        frozenset(s)                                    转换为不可变集合
        chr(x)                                          将一个整数转换为一个字符
        ord(x)                                          将一个字符转换为它的整数值
        hex(x)                                          将一个整数转换为一个十六进制字符串
        oct(x)                                          将一个整数转换为一个八进制字符串
'''

'''
    描述
        int() 函数用于将一个字符串或数字转换为整型。
        语法
            以下是 int() 方法的语法:
                class int(x, base=10)
        参数
            x -- 字符串或数字。
            base -- 进制数，默认十进制。
        返回值
            返回整型数据。
'''


def x_conversion_to_int():
    x = 8
    '''
    将x转换为一个整数
        x -- 字符串或数字。
        base -- 进制数，默认十进制;如果是带参数base的话,x要以字符串的形式进行输入
    '''
    i = int()
    print(i)  # 不传入参数时，得到结果0
    i = int(x)
    print(i)
    i = int(str(x), base=10)  # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
    print(i)


# x_conversion_to_int()

def x_conversion_to_float():
    x = 8
    f = float(x)
    print(f)


# x_conversion_to_float()

'''
    描述
        complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。
    complex 语法
        complex 语法：
            class complex([real[, imag]])
        参数说明：
            real -- int, long, float或字符串；
            imag -- int, long, float；
    返回值
        返回一个复数。
'''


def x_conversion_to_complex():
    c = complex(1, 2)
    print(c)
    c = complex(1)  # 数字
    print(c)
    c = complex("1")  # 当做字符串处理
    print(c)
    # 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
    c = complex("1+2j")
    print(c)


# x_conversion_to_complex()

'''
    描述
        str() 函数将对象转化为适于人阅读的形式。
        
    语法
        以下是 str() 方法的语法:
            class str(object='')
    参数
            object -- 对象。
    返回值
        返回一个对象的string格式。
'''


def x_conversion_to_str():
    s = 'RUNOOB'
    print(str(s))  # RUNOOB
    dict = {'runoob': 'runoob.com', 'google': 'google.com'}
    print(dict)  # {'runoob': 'runoob.com', 'google': 'google.com'}
    print(str(dict))  # {'runoob': 'runoob.com', 'google': 'google.com'}


# x_conversion_to_str()

'''
    描述
        repr() 函数将对象转化为供解释器读取的形式。
    
    语法
        以下是 repr() 方法的语法:
            repr(object)
    参数
        object -- 对象。
    返回值
        返回一个对象的 string 格式。
'''


def x_conversion_to_repr():
    s = 'RUNOOB'
    print(repr(s))  # 'RUNOOB'
    dict = {'runoob': 'runoob.com', 'google': 'google.com'}
    print(dict)  # {'runoob': 'runoob.com', 'google': 'google.com'}
    print(repr(dict))  # {'runoob': 'runoob.com', 'google': 'google.com'}


# x_conversion_to_repr()

'''
    描述
        eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    语法
        以下是 eval() 方法的语法:
            eval(expression[, globals[, locals]])
        参数
            expression -- 表达式。
            globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
            locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
    返回值
        返回表达式计算结果。
'''


def x_conversion_to_eval():
    x = 7
    print(eval('3*x'))  # 21
    print(eval('pow(2,2)'))  # 4
    print(eval('2+2'))  # 4
    n = 81
    print(eval("n+4"))  # 85


# x_conversion_to_eval()

'''
    描述
        tuple 函数将可迭代系列（如列表）转换为元组。
    语法
        以下是 tuple 的语法:
            tuple( iterable )
        参数
            iterable -- 要转换为元组的可迭代序列。
    返回值
        返回元组。
'''


def x_conversion_to_tuple():
    list = ['Google', 'Taobao', 'Runoob', 'Baidu']
    print(tuple(list))  # ('Google', 'Taobao', 'Runoob', 'Baidu')


# x_conversion_to_tuple()

'''
    描述
        list() 方法用于将元组或字符串转换为列表。
        注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
    语法
        list()方法语法：
            list( seq )
        参数
            seq -- 要转换为列表的元组或字符串。
    返回值
        返回列表。
'''


def x_conversion_to_list():
    tuple = (123, 'Google', 'Runoob', 'Taobao')
    list1 = list(tuple)
    print("列表元素 : ", list1)  # 列表元素 :  [123, 'Google', 'Runoob', 'Taobao']

    str = "Hello World"
    list2 = list(str)
    print("列表元素 : ", list2)  # 列表元素 :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']


# x_conversion_to_list()

'''
    转换为可变集合
    描述
        set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    语法
        set 语法：
            class set([iterable])
        参数说明：
            iterable -- 可迭代对象对象；
    返回值
        返回新的集合对象
'''


def x_conversion_to_set():
    x = set('runoob')
    y = set('google')
    print(x)  # {'b', 'u', 'r', 'n', 'o'}
    print(y)  # {'g', 'e', 'l', 'o'}
    print(x, y)  # 去重,重复的被删除 {'b', 'u', 'r', 'n', 'o'} {'g', 'e', 'l', 'o'}

    print(x - y)  # 差集        {'b', 'n', 'r', 'u'}
    print(x & y)  # 交集        {'o'}
    print(x | y)  # 并集        {'o', 'g', 'b', 'n', 'e', 'l', 'r', 'u'}
    print(x ^ y)  # 不同时存在     {'g', 'b', 'n', 'e', 'l', 'r', 'u'}


# x_conversion_to_set()

'''
    创建一个字典。d 必须是一个 (key, value)元组序列。
    描述
        dict() 函数用于创建一个字典。
    语法
        dict 语法：
            class dict(**kwarg)
            class dict(mapping, **kwarg)
            class dict(iterable, **kwarg)
        参数说明：
            **kwargs -- 关键字
            mapping -- 元素的容器。
            iterable -- 可迭代对象。
    返回值
        返回一个字典。
'''


def x_conversion_to_dict():
    print(dict())  # 创建空字典 {}
    print(dict(a='a', b='b', t='t'))  # 传入关键字 {'a': 'a', 'b': 'b', 't': 't'}
    # zip 映射函数
    print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))  # 映射函数方式来构造字典  {'one': 1, 'two': 2, 'three': 3}
    print(dict([('one', 1), ('two', 2), ('three', 3)]))  # 可迭代对象方式来构造字典{'one': 1, 'two': 2, 'three': 3}


# x_conversion_to_dict()


'''
    转换为不可变集合
    描述
        frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
    语法
        frozenset() 函数语法：
            class frozenset([iterable])
        参数
            iterable -- 可迭代的对象，比如列表、字典、元组等等。
    返回值
        返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。
'''


def x_conversion_to_frozenset():
    # range() 函数可创建一个整数列表，一般用在 for 循环中。
    a = frozenset(range(10))  # 生成一个新的不可变集合
    print(a)  # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = frozenset('runoob')
    print(b)  # frozenset({'u', 'n', 'r', 'o', 'b'})
    c = frozenset(['b', 'r', 'u', 'o', 'n'])  # 创建不可变集合
    print(c)  # frozenset({'u', 'n', 'r', 'o', 'b'})


# x_conversion_to_frozenset()

'''
    将一个整数转换为一个字符
    描述
        chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
    
    语法
        以下是 chr() 方法的语法:
            chr(i)
        参数
            i -- 可以是10进制也可以是16进制的形式的数字。
    返回值
        返回值是当前整数对应的 ASCII 字符。
'''


def x_conversion_to_chr():
    print(chr(0x30), chr(0x31), chr(0x61))  # 十六进制  0 1 a
    print(chr(48), chr(49), chr(97))  # 十进制   0 1 a


# x_conversion_to_chr()

'''
    将一个字符转换为它的整数值
    描述
        ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）
        作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
    
    语法
        以下是 ord() 方法的语法:
            ord(c)
        参数
            c -- 字符。
    返回值
        返回值是对应的十进制整数。
'''


def x_conversion_to_ord():
    print(ord('a'))  # 97
    print(ord('b'))  # 98
    print(ord('c'))  # 99


# x_conversion_to_ord()

'''
    将一个整数转换为一个十六进制字符串
    描述
        hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
    语法
        hex 语法：
            hex(x)
        参数说明：
            x -- 10进制整数
    返回值
        返回16进制数，以字符串形式表示
'''


def x_conversion_to_hex():
    print(hex(255))  # 0xff
    print(hex(-42))  # -0x2a
    print(hex(1))  # 0x1
    print(hex(12))  # 0xc
    print(type(hex(12)))  # <class 'str'>


x_conversion_to_hex()

'''
    将一个整数转换为一个八进制字符串
    描述
        oct() 函数将一个整数转换成 8 进制字符串。
        Python2.x 版本的 8 进制以 0 作为前缀表示。
        Python3.x 版本的 8 进制以 0o 作为前缀表示。
    语法
        oct 语法：
            oct(x)
        参数说明：
            x -- 整数。
    返回值
        返回 8 进制字符串。
'''


def x_conversion_to_oct():
    print(oct(10))  # 0o12
    print(oct(20))  # 0o24
    print(oct(15))  # 0o17


# x_conversion_to_oct()
