import p
'''
什么是运算符？
    举个简单的例子:
        4 + 5 = 9
        例子中，4 和 5 被称为操作数，+ 称为运算符
'''

'''
    Python 语言支持以下类型的运算符:
        算术运算符               +,-,*,/,%,**,//
        比较/关系运算符           ==,!=,>,<,>=,<=                                                          
        赋值运算符             =,+=,-=,*=,/=,%=,**=,//=,:=
        逻辑运算符               and,or,not
        位运算符                &,|,^,~,<<,>>
        成员运算符              in,not in
        身份运算符               is,is not
        运算符优先级             高到低:**,~+-:按位翻转,*/%//,+-:加减,>> <<,&,^|,<= < > >=,== !=,= %= /= //= -= += *= **=,
                                        is is not,in not in,not and or
'''

p.prt(1, '算术运算符               +,-,*,/,%,**,//')
'''
以下假设变量a为10，变量b为21：
    +	加 - 两个对象相加	                                a + b 输出结果 31
    -	减 - 得到负数或是一个数减去另一个数	                a - b 输出结果 -11
    *	乘 - 两个数相乘或是返回一个被重复若干次的字符串	    a * b 输出结果 210
    /	除 - x 除以 y	                                b / a 输出结果 2.1
    %	取模 - 返回除法的余数	                            b % a 输出结果 1
    **	幂 - 返回x的y次幂	                                a**b 为10的21次方
    //	取整除 - 向下取接近商的整数	                    >>> 9//2
                                                        4
                                                        >>> -9//2
                                                        -5
'''


def count_operator():
    a = 21
    b = 10
    c = 0
    print("初始 - c 的值为：", c)  # 0

    c = a + b
    print("加 - c 的值为：", c)  # 31

    c = a - b
    print("减 - c 的值为：", c)  # 11

    c = a * b
    print("乘 - c 的值为：", c)  # 210

    c = a / b
    print("除 - c 的值为：", c)  # 2.1

    c = a % b
    print("取余 - c 的值为：", c)  # 1

    # 修改变量 a 、b 、c
    a = 2
    b = 3
    c = a ** b
    print("幂 - c 的值为：", c)  # 8

    a = 10
    b = 5
    c = a // b
    print("取整除 - c 的值为：", c)  # 2

    a = -10.6
    b = 5
    c = a // b
    print("取整除 - c 的值为：", c)  # -3.0


# count_operator()

print('---------')
print('2,比较/关系运算符           ==,!=,>,<,>=,<= ')
'''
以下假设变量a为10，变量b为20：
所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。
    ==	等于 - 比较对象是否相等	            a == b 返回 False。
    !=	不等于 - 比较两个对象是否不相等	        a != b 返回 True。
    >	大于 - 返回x是否大于y	                a > b 返回 False。
    <	小于 - 返回x是否小于y                 a < b 返回 True。
    >=	大于等于 - 返回x是否大于等于y。	        a >= b 返回 False。
    <=	小于等于 - 返回x是否小于等于y。         a <= b 返回 True。
'''


def compare_operator():
    a = 21
    b = 10

    print(a == b)  # False

    if a == b:
        print("1 - a 等于 b")
    else:
        print("1 - a 不等于 b")

    if a != b:
        print("2 - a 不等于 b")
    else:
        print("2 - a 等于 b")

    if a < b:
        print("3 - a 小于 b")
    else:
        print("3 - a 大于等于 b")

    if a > b:
        print("4 - a 大于 b")
    else:
        print("4 - a 小于等于 b")

    # 修改变量 a 和 b 的值
    a = 5
    b = 20
    if a <= b:
        print("5 - a 小于等于 b")
    else:
        print("5 - a 大于  b")

    if b >= a:
        print("6 - b 大于等于 a")
    else:
        print("6 - b 小于 a")


# compare_operator()

print('---------')
print('3,赋值运算符             =,+=,-=,*=,/=,%=,**=,//=,:=')
'''
以下假设变量a为10，变量b为20：
    =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
    +=	加法赋值运算符	c += a 等效于 c = c + a
    -=	减法赋值运算符	c -= a 等效于 c = c - a
    *=	乘法赋值运算符	c *= a 等效于 c = c * a
    /=	除法赋值运算符	c /= a 等效于 c = c / a
    %=	取模赋值运算符	c %= a 等效于 c = c % a
    **=	幂赋值运算符	    c **= a 等效于 c = c ** a
    //=	取整除赋值运算符	c //= a 等效于 c = c // a
    :=	海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。	在这个示例中，赋值表达式可以避免调用 len() 两次:
        if (n := len(a)) > 10:
            print(f"List is too long ({n} elements, expected <= 10)")
'''


def voluation_operator():
    a = 21
    b = 10
    c = 0

    print("初始 - c 的值为：", c)  # 0

    c = a + b
    print("1 - c 的值为：", c)

    c += a
    print("2 - c 的值为：", c)

    c *= a
    print("3 - c 的值为：", c)

    c /= a
    print("4 - c 的值为：", c)

    c = 2
    c %= a
    print("5 - c 的值为：", c)

    c **= a
    print("6 - c 的值为：", c)

    c //= a
    print("7 - c 的值为：", c)


# voluation_operator()


print('---------')
print('4,逻辑运算符               and,or,not')
'''
以下假设变量 a 为 10, b为 20:
    and	    x and y	    布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	    a and b 返回 20。
    or	    x or y	    布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	            a or b 返回 10。
    not	    not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	    not(a and b) 返回 False
'''


def logic_operator():
    a = 10
    b = 20

    if a and b:
        print("1 - 变量 a 和 b 都为 true")
    else:
        print("1 - 变量 a 和 b 有一个不为 true")

    if a or b:
        print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("2 - 变量 a 和 b 都不为 true")

    # 修改变量 a 的值
    a = 0
    if a and b:
        print("3 - 变量 a 和 b 都为 true")
    else:
        print("3 - 变量 a 和 b 有一个不为 true")

    if a or b:
        print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
    else:
        print("4 - 变量 a 和 b 都不为 true")

    if not (a and b):
        print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
    else:
        print("5 - 变量 a 和 b 都为 true")


logic_operator()

print('---------')
print('5,位运算符                &,|,^,~,<<,>>')
'''
以下假设 a 为 60，b 为 13二进制格式如下:   a = 0011 1100,b = 0000 1101
按位运算符是把数字看作二进制来进行计算的
    &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	    a & b 输出结果 12 ，二进制解释： 0000 1100
    |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	                a | b 输出结果 61 ，二进制解释： 0011 1101
    ^	按位异或运算符：当两对应的二进位相异时，结果为1	                            a ^ b 输出结果 49 ，二进制解释： 0011 0001
    ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	    ~a  输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
    <<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，
        高位丢弃，低位补0。	                                                    a << 2 输出结果 240 ，二进制解释： 1111 0000
    >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，
        ">>"右边的数指定移动的位数	                                                a >> 2 输出结果 15 ，二进制解释： 0000 1111
'''


def bitwise_operator():
    a = 60
    b = 13
    '''将整数转化成二进制字符串'''
    # https://blog.csdn.net/qq_37701443/article/details/84493931
    # 1、采用字符串的 format 方法来获取二进制
    binary_m1_a = '{0:b}'.format(a)
    binary_m1_b = '{0:b}'.format(b)
    print('方法一', binary_m1_a, binary_m1_b)  # 方法一 111100 1101
    print('方法二', binary_m2_a, binary_m2_b)
    # 2、采用 python 自带了方法 bin 函数：
    binary_m3_a = str(bin(a))[2:]
    binary_m3_b = bin(b)[2:]
    print(type(bin(a)))
    print('方法三', binary_m3_a, binary_m3_b)

    c = a & b  # 12 = 0000 1100
    print("1 - c 的值为：", c)

    c = a | b  # 61 = 0011 1101
    print("2 - c 的值为：", c)

    c = a ^ b  # 49 = 0011 0001
    print("3 - c 的值为：", c)

    c = ~a  # -61 = 1100 0011
    print("4 - c 的值为：", c)

    c = a << 2  # 240 = 1111 0000
    print("5 - c 的值为：", c)

    c = a >> 2  # 15 = 0000 1111
    print("6 - c 的值为：", c)


# bitwise_operator()

print('---------')
print('6,成员运算符              in,not in')
'''
in	        如果在指定的序列中找到值返回 True，否则返回 False。	        x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	    如果在指定的序列中没有找到值返回 True，否则返回 False。	    x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
'''


def member_operator():
    a = 10
    b = 20
    list = [1, 2, 3, 4, 5]

    if a in list:
        print("1 - 变量 a 在给定的列表中 list 中")
    else:
        print("1 - 变量 a 不在给定的列表中 list 中")

    if b not in list:
        print("2 - 变量 b 不在给定的列表中 list 中")
    else:
        print("2 - 变量 b 在给定的列表中 list 中")

    # 修改变量 a 的值
    a = 2
    if a in list:
        print("3 - 变量 a 在给定的列表中 list 中")
    else:
        print("3 - 变量 a 不在给定的列表中 list 中")


member_operator()

print('---------')
print('7,身份运算符               is,is not')
'''
身份运算符用于比较两个对象的存储单元
    is	is      是判断两个标识符是不是引用自一个对象	            x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
    is not	    is not 是判断两个标识符是不是引用自不同对象	    x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，
                                                            否则返回 False。
'''


def identity_operator():
    a = 20
    b = 20

    if a is b:
        print("1 - a 和 b 有相同的标识")
    else:
        print("1 - a 和 b 没有相同的标识")

    if id(a) == id(b):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    # 修改变量 b 的值
    b = 30
    if a is b:
        print("3 - a 和 b 有相同的标识")
    else:
        print("3 - a 和 b 没有相同的标识")

    if a is not b:
        print("4 - a 和 b 没有相同的标识")
    else:
        print("4 - a 和 b 有相同的标识")


# identity_operator()

'''
    is 与 == 区别：
    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''


def is_diff_equal():
    a = [1, 2, 3]
    b = a
    print(b is a)  # True
    print(b == a)  # True
    b = a[:]
    print(b is a)  # False
    print(b == a)  # True


# is_diff_equal()

print('---------')
print('8,运算符优先级 ')
'''
从最高到最低优先级的所有运算符：
    **	                        指数 (最高优先级)
    ~ + -	                    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
    * / % //	                乘，除，求余数和取整除
    + -	                        加法减法
    >> <<	                    右移，左移运算符
    &	                        位 'AND'
    ^ |	                        位运算符
    <= < > >=	                比较运算符
    == !=	                    等于运算符
    = %= /= //= -= += *= **=	赋值运算符
    is is not	                身份运算符
    in not in	                成员运算符
    not and or	                逻辑运算符
'''


def operator_priority():
    a = 20
    b = 10
    c = 15
    d = 5
    e = 0
    print('初始化:e{}'.format(e))

    e = (a + b) * c / d  # ( 30 * 15 ) / 5
    print("(a + b) * c / d 运算结果为：", e)

    e = ((a + b) * c) / d  # (30 * 15 ) / 5
    print("((a + b) * c) / d 运算结果为：", e)

    e = (a + b) * (c / d)  # (30) * (15/5)
    print("(a + b) * (c / d) 运算结果为：", e)

    e = a + (b * c) / d  # 20 + (150/5)
    print("a + (b * c) / d 运算结果为：", e)


operator_priority()
