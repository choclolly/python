import p

p.prt(1, '元组')
'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
'''


def c_tuple():
    tup1 = ('Google', 'Runoob', 1997, 2000)
    print(tup1)
    tup2 = (1, 2, 3, 4, 5)
    print(tup2)
    tup3 = "a", "b", "c", "d"  # 不需要括号也可以
    print(tup3)
    type(tup3)

    # 创建空元组
    tup_null = ()
    print(tup_null)  # ()

    # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
    tup1 = 50
    print(type(tup1))  # 不加逗号，类型为整型    <class 'int'>
    tup2 = 50,
    print(type(tup2))  # 加上逗号，类型为元组 <class 'tuple'>
    tup3 = (50,)
    print(type(tup3))  # 加上逗号，类型为元组 <class 'tuple'>


c_tuple()

p.prt(2, '访问元组')
'''
元组与字符串类似，下标索引从 0 开始，可以进行截取，组合等。
'''


def visit_tuple():
    tup1 = ('Google', 'Runoob', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5, 6, 7)

    print("tup1[:]: ", tup1[:])
    print("tup1[0]: ", tup1[0])
    print("tup1[-1]: ", tup1[-1])
    print("tup2[1:5]: ", tup2[1:5])


# visit_tuple()

p.prt(3, '修改元组')
'''
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
'''


def splicint_tuple():
    tup1 = (12, 34.56)
    tup2 = ('abc', 'xyz')

    # 以下修改元组元素操作是非法的。
    # tup1[0] = 100

    # 创建一个新的元组
    tup3 = tup1 + tup2
    print(tup3)


# splicint_tuple()


p.prt(4, '删除元组')
'''
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
'''


def del_tuple():
    tup = ('Google', 'Runoob', 1997, 2000)

    print(tup)
    del tup
    print("删除后的元组 tup : ")
    print(tup)


# del_tuple()

p.prt(5, '元组运算符')
'''
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
    Python 表达式	            结果	                            描述
    len((1, 2, 3))	            3	                            计算元素个数
    (1, 2, 3) + (4, 5, 6)	    (1, 2, 3, 4, 5, 6)	            连接
    ('Hi!',) * 4	            ('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
    3 in (1, 2, 3)	            True	                        元素是否存在
    for x in (1, 2, 3): 
        print (x,)	            1 2 3	                        迭代
'''

p.prt(6, '元组索引，截取')
'''
元组索引，截取
tup = ('Google', 'Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
    Python 表达式	        结果	                                                描述
    tup[1]	            'Runoob'	                                        读取第二个元素
    tup[-2]	            'Weibo'	                                            反向读取，读取倒数第二个元素
    tup[1:]	            ('Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')	    截取元素，从第二个开始后的所有元素。
    tup[1:4]	        ('Runoob', 'Taobao', 'Wiki')	                    截取元素，从第二个开始到第四个元素（索引为 3）。
'''


def sub_tuple():
    tup = ('Google', 'Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
    print(tup[1])  # Runoob
    print(tup[-2])  # Weibo
    print(tup[1:])  # ('Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
    print(tup[1:4])  # ('Runoob', 'Taobao', 'Wiki')


# sub_tuple()


p.prt(7, '元组内置函数')
'''
元组内置函数
    序号	方法及描述	实例
    1	len(tuple)  计算元组元素个数。	
        >>> tuple1 = ('Google', 'Runoob', 'Taobao')
        >>> len(tuple1)
        3
        >>> 
    2	max(tuple)  返回元组中元素最大值。	
        >>> tuple2 = ('5', '4', '8')
        >>> max(tuple2)
        '8'
        >>> 
    3	min(tuple)  返回元组中元素最小值。	
        >>> tuple2 = ('5', '4', '8')
        >>> min(tuple2)
        '4'
        >>> 
    4	tuple(iterable) 将可迭代系列转换为元组。	
        >>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
        >>> tuple1=tuple(list1)
        >>> tuple1
        ('Google', 'Taobao', 'Runoob', 'Baidu')
'''

p.prt(8, '关于元组是不可变的')
'''
所谓元组的不可变指的是元组所指向的内存中的内容不可变。
'''


def immutable_tuple():
    tup = ('r', 'u', 'n', 'o', 'o', 'b')
    # tup[0] = 'g'  # 不支持修改元素
    '''
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: 'tuple' object does not support item assignment
    '''

    i = id(tup)  # 查看内存地址
    print(i)  # 9224120

    tup = (1, 2, 3)
    i = id(tup)  # 内存地址不一样了
    print(i)  # 9335304


# immutable_tuple()
