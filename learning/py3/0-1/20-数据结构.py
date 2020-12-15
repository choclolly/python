import p

p.prt(1, '数据结构')
'''
数据结构
    结合前面所学的知识点来介绍Python数据结构
'''

p.prt(2, '列表')
'''
列表是可变的，这是它区别于字符串和元组的最重要的特点,一句话概括即：列表可以修改，而字符串和元组不能
'''
p.prt(3, '下是 Python 中列表的方法')
'''
方法	                        描述
list.append(x)	    把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	    通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，
                        而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	    删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	    从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
                        （方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	    移除列表中的所有项，等于del a[:]。
list.index(x)	    返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	    返回 x 在列表中出现的次数。
list.sort()	        对列表中的元素进行排序。
list.reverse()	    倒排列表中的元素。
list.copy()	        返回列表的浅复制，等于a[:]。
'''


def m_list():
    l = [66.25, 333, 333, 1, 1234.5]
    # 返回 x 在列表中出现的次数
    print(l.count(333), l.count(1234.5), l.count(66.25))

    l.insert(0, 1)
    l.insert(-1, 2)
    print(l)

    l.append(4)
    print(l)

    index = l.index(1)
    print(index)

    l.remove(1)
    print(l)

    l.reverse()
    print(l)

    l.sort()
    print(l)


# m_list()


p.prt(4, '将列表当做堆栈使用')
'''
将列表当做堆栈使用
    列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
    用 append() 方法可以把一个元素添加到堆栈顶。
    用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
'''


def stack():
    l = [1, 2, 3]
    print(l)

    # 用 append() 方法可以把一个元素添加到堆栈顶
    l.append(4)
    l.append(5)
    print(l)

    # 用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
    pop = l.pop()
    print(pop)
    pop = l.pop()
    print(pop)
    pop = l.pop()
    print(pop)


# stack()

p.prt(5, '将列表当作队列使用')
'''
将列表当作队列使用
    Python3 collections模块使用详解:https://www.jianshu.com/p/47f66ff4ab7b
        collections包含了一些特殊的容器，针对Python内置的容器，例如list、dict、set和tuple，提供了另一种选择；
            namedtuple，可以创建包含名称的tuple
            deque，类似于list的容器，可以快速的在队列头部和尾部添加、删除元素
            Counter，dict的子类，计算可hash的对象
            OrderedDict，dict的子类，可以记住元素的添加顺序
            defaultdict，dict的子类，可以调用提供默认值的函数
'''
from collections import deque


def queue():
    queue = deque([1, 2, 3, 4])
    print(queue)

    queue.append(5)
    print(queue)

    queue.append(6)
    print(queue)

    popleft = queue.popleft()
    print(popleft)

    print(queue)


queue()


p.prt(6, '列表推导式')

'''
列表推导式
    列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，
    或者根据确定的判定条件创建子序列。

    每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
    如果希望表达式推导出一个元组，就必须使用括号
Python3学习9 列表、元组、集合、字典的推导式'
    https://blog.csdn.net/weixin_42560429/article/details/86773050
'''


def deriverd_list():
    '''list列表推导式'''
    # for…
    l = [1, 2, 3]
    # 不使用推导式
    l2 = []
    for x in l:
        l2.append(5 * x)
    print(f'for…不使用推导式:{l2}')
    # 使用推导式
    l_new = [5 * x for x in l]
    print(f'for…使用推导式:{l_new}')

    p.prt2()
    # for… if… ,if 子句作为过滤器
    # 不使用推导式
    l2 = []
    for x in l:
        if x > 1:
            l2.append(5 * x)
    print(f'for… if…不使用推导式:{l2}')
    # 使用推导式
    l_new = [5 * x for x in l if x > 1]
    print('for… if…使用推导式:% s' % l_new)

    p.prt2()
    # for… if…else…
    # 不使用推导式
    l2 = []
    for x in l:
        if x > 1:
            l2.append(x)
        else:
            l2.append(8)
    print(f'for… if…else…不使用推导式:{l2}')
    # 使用推导式
    l_new = [x if x > 1 else 8 for x in l]
    print('for… if…else…使用推导式:% s' % l_new)


# deriverd_list()

def deriverd_list_1():
    l = [1, 2, 3]
    y = [[x, x * 2] for x in l]
    print(y)  # [[1, 2], [2, 4], [3, 6]]


# deriverd_list_1()

# 对序列里每一个元素逐个调用某方法
def deriverd_list_2():
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    x = [x.strip() for x in freshfruit]
    print(x)  # ['banana', 'loganberry', 'passion fruit']


# deriverd_list_2()

# 关于循环和其它技巧
def devrierd_list3():
    vec1, vec2 = [2, 4, 6], [4, 3, -9]
    x = [x * y for x in vec1 for y in vec2]
    print(x)  # [8, 6, -18, 16, 12, -36, 24, 18, -54]

    x = [x + y for x in vec1 for y in vec2]
    print(x)  # [6, 5, -7, 8, 7, -5, 10, 9, -3]

    x = [vec1[i] * vec2[i] for i in range(len(vec1))]
    print(x)  # [8, 12, -54]


# devrierd_list3()

p.prt(7, '元组推导式')


def deriverd_tuple():
    x = (x for x in range(10))
    print(x)  # <generator object deriverd_tuple.<locals>.<genexpr> at 0x00F2D098>
    print(tuple(x))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    # tuple
    tup = (5 * x for x in range(10))
    print(tup)
    print(tuple(tup))


# deriverd_tuple()

p.prt(8, '集合推导式')


def deriverd_set():
    x = {x for x in range(10)}
    print(x)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# deriverd_set()

p.prt(9, '字典推导式')


def deriverd_dict():
    x = {x: x * x for x in range(10)}
    print(x)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# deriverd_dict()

p.prt(10, '4&8 媳妇出题 2020年10月30日 13点34分')


# 位运算
def count():
    # 转二进制
    binary_1 = int('{0:b}'.format(4))
    binary_2 = int('{0:b}'.format(8))
    print(binary_1)
    print(binary_2)
    print(4 & 8)


# count()

p.prt(11, '嵌套列表解析')
'''
嵌套列表解析
    Python的列表还可以嵌套
'''


# 3X4的矩阵列表
def nesting_list():
    l = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print(l)

    # 嵌套列表
    l4 = [12]
    l5 = []
    print(l5)
    l5.append(l4)  # 等价 l5[l4]
    print(l5)


# nesting_list()

# 将3X4的矩阵列表转换为4X3列表
def nesting_list_1():
    l = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # 将3X4的矩阵列表转换为4X3列表
    x = [[y[x] for y in l] for x in range(4)]
    print(x)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# nesting_list_1()

# 将3X4的矩阵列表转换为4X3列表
def nesting_list_2():
    l = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    l2 = []
    for x in range(4):
        l2.append([y[x] for y in l])
    print(l2)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# nesting_list_2()

# 将3X4的矩阵列表转换为4X3列表
def nesting_list_3():
    l = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    l3 = []
    for x in range(4):
        l2 = []
        for y in l:
            l2.append(y[x])
        l3.append(l2)
    print(l3)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# nesting_list_3()


p.prt(12, 'del语句')
'''
del 语句
    使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。
        可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）
    
    也可以用 del 删除实体变量：
'''


def example_del():
    l = [-1, 1, 66.25, 333, 333, 1234.5]

    del l[0]
    print(l)

    del l[1:2]
    print(l)

    # 清空整个列表
    del l[:]
    print(l)

    #  删除实体变量
    del l
    print(l)


# example_del()


p.prt(13, '元组和序列')
'''
元组和序列
    元组由若干逗号分隔的值组成
    元组可以嵌套
    
    元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。
'''


def example_tuple():
    t = 12345, 54321, 'hello!'
    print(t)
    print(t[0])

    # Tuples may be nested:
    x = t, (1, 2, 3)
    print(x)  # 12345, 54321, 'hello!'), (1, 2, 3))


# example_tuple()


p.prt(14, '集合')
'''
集合
    集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
    可以用大括号({})创建集合。注意：
        如果要创建一个空集合，你必须用 set() 而不是 {} ；
        后者 {} 创建一个空的字典。
    支持推导式
'''


def example_set():
    # 空集合
    x = set()
    print(x)

    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

    # 去重
    print(basket)

    # 成员
    if 'apple' in basket:
        print(True)
    else:
        print(False)

    a = set('abracadabra')
    b = set('alacazam')

    print(a & b)  # 交集 在 a 和 b 中都有的字母
    print(a | b)  # 并集 在 a 或 b 中的字母
    print(a ^ b)  # 在 a 或 b 中的字母，但不同时在 a 和 b 中
    print(a - b)  # 差集 在 a 中的字母，但不在 b 中

    # 支持推导式
    x = {x for x in basket if x not in 'banana'}
    print(x)


# example_set()


p.prt(15, '字典')
'''
字典
    另一个非常有用的 Python 内建数据类型是字典。
    序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
    理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
    一对大括号创建一个空的字典：{}。
'''

import time


def example_dict():
    dict = {'name': 'h', 'age': 32, 'sex': 1}
    dict['birthday'] = time.time()
    print(dict)

    print(dict['name'])

    del dict['name']
    print(dict)

    keys = dict.keys()
    print(keys)
    print(list.sort(list(keys)))

    values = dict.values()
    print(values)

    if 'h' in values:
        print(True)
    else:
        print(False)


# example_dict()


def example_dict_1():
    # 构造函数 dict() 直接从键值对元组列表中构建字典
    d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(d)

    # 典推导可以用来创建任意键和值的表达式词典
    d = {x: x ** 2 for x in (2, 4, 6)}
    print(d)

    # 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
    d = dict(sape=4139, guido=4127, jack=4098)
    print(d)


# example_dict_1()


p.prt(16, '遍历技巧')
'''
遍历技巧
    在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
    序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
    同时遍历两个或更多的序列，可以使用 zip() 组合
    要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
    要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
'''


def iter_m():
    # 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
    d = {'sape': 4139, 'guido': 4127, 'jack': 4098}
    for k, v in d.items():
        print(k, v, end=' |')
    print('\n')

    # 序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
    l = [x for x in range(10,20)]
    print(l)
    for i, v in enumerate(l):
        print(f'索引:{i},值:{v}')
    print('\n')

    #要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
    x = [x for x in reversed(l)]
    print(x)
    print('\n')

    # 同时遍历两个或更多的序列，可以使用 zip() 组合
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q,a in zip(questions,answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
    print('\n')

    # 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for x in  sorted(basket):
        print(x,end=",")
# iter_m()
