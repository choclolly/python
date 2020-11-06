import p

p.prt(1, '循环语句')
'''
Python 中的循环语句有 for 和 while。
'''

p.prt(2, 'for 语句')
'''
for 语句
    Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for循环的一般格式如下：
    for <variable> in <sequence>:
        <statements>
    else:
        <statements>
'''


def for_instance():
    languages = ["C", "C++", "Perl", "Python"]
    for x in languages:
        print(f'{x}', end=",")


# for_instance()

p.prt(3, 'while 循环语句')
'''
Python 中 while 语句的一般形式：
    while 判断条件(condition)：
        执行语句(statements)……
    同样需要注意冒号和缩进。
    另外，在 Python 中没有 do..while 循环。
'''


# 计算 1 到 100 的总和
def while_instance():
    n = 100
    sum = 0
    counter = 0
    while counter <= n:
        sum = sum + counter
        counter += 1
    print(f'1 到 100 之和为:{sum}')


# while_instance()

p.prt(4, 'break 语句，break 语句用于跳出当前循环体 for 和 while')


# for 中使用 break
def break_for_instance():
    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        # 在循环到 "Runoob"时会跳出循环体
        if site == 'Runoob':
            print('site is Runoob')
            break
        print(f'循环数据:{site}')
    else:
        print('site is not Runoob')
    print('循环完成')


# break_for_instance()


# for 中使用 continue
def continue_for_instance():
    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        # 在循环到 "Runoob"时会跳出循环体
        if site == 'Runoob':
            print('site is Runoob')
            continue
        print(f'循环数据:{site}')
    else:
        print('site is not Runoob')
    print('循环完成')


# continue_for_instance()

p.prt(5, 'continue 语句，continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环')


# while 中使用 break
def continue_while_instance():
    x = 5
    while x > 0:
        # 相当于 x = x - 1
        x -= 1
        if x == 3:
            continue
        print(x, end=",")
    print('while over')


# continue_while_instance()


# while 中使用 break
def break_while_instance():
    x = 5
    while x > 0:
        # 相当于 x = x - 1
        x -= 1
        if x == 3:
            break
        print(x, end=",")
    print('while over')


# break_while_instance()

def break_another_instance():
    for x in "haodonghui":
        # 碰到字母 o 跳出循环
        if x == 'o':
            break
        print('当前字母为 :', x, end=" |")  # 当前字母为 : h |当前字母为 : a |


# break_other_instance()

def break_another_instance_1():
    var = 10
    while var > 0:
        print('当期变量值为 :', var)
        var -= 1
        # var 等于 5 的时候跳出循环
        if var == 5:
            break
    print('Good Bye')


# break_another_instance_1()

def continue_another_instance():
    for x in "haodonghui":
        # 碰到字母 o 跳过出书
        if x == 'o':
            continue
        print('当前字母为 :', x,
              end=" |")  # 当前字母为 : h |当前字母为 : a |当前字母为 : d |当前字母为 : n |当前字母为 : g |当前字母为 : h |当前字母为 : u |当前字母为 : i |


# continue_another_instance()


def continue_another_instance_1():
    var = 10
    while var > 0:
        var -= 1
        # var 变量为 5 时跳过输出
        if var == 5:
            continue
        print('当期变量值为 :', var)
    print('Good Bye')


# continue_another_instance_1()

p.prt(6, '循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。')


# 查询质数
# 质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数（规定1既不是质数也不是合数）
def for_of_else():
    for n in range(2, 10):
        for x in range(2, n):
            if n % 2 == 0:
                print(n, '等于', x, '*', n // x)
                break
        else:
            print(n, ' 是质数')


# for_of_else()

p.prt(7, 'while 循环使用 else 语句')
'''
while 循环使用 else 语句
    在 while … else 在条件语句为 false 时执行 else 的语句块。
    语法格式如下：
        while <expr>:
            <statement(s)>
        else:
            <additional_statement(s)>
'''


def while_of_else():
    x = 0
    while x < 5:
        print(x, " 小于 5")
        x = x + 1
    else:
        print(x, " 大于或等于 5")


while_of_else()

p.prt(8, 'pass 语句')
'''
pass 语句
    Python pass是空语句，是为了保持程序结构的完整性。
    pass 不做任何事情，一般用做占位语句
        D:\python\learning\py3\0-1>py
        Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> while True:
        ...     pass

'''


def pass_statement():
    for x in "haodonghui":
        # 碰到字母 o 跳出循环
        if x == 'o':
            pass
            break
        print('当前字母为 :', x, end=" |")  # 当前字母为 : h |当前字母为 : a |


# pass_statement()


p.prt(9, '无限循环')
'''
无限循环
    我们可以通过设置条件表达式永远不为 false 来实现无限循环
    
    D:\python\learning\py3\0-1>python
    Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> while True:
    ...     print('------------------')
    ------------------
    ------------------
    ------------------
    ....
    
    限循环你可以使用 CTRL+C 来中断循环

'''


def infinite_loop():
    i = 0
    # 表达式永远为 true
    while i == 0:
        num = str(input('输入一个数字  :'))
        print("你输入的数字是: ", num)
        if int(num) == 9:
            i += 1
    print('Good bye!')


# infinite_loop()

p.prt(10, '简单语句组')
'''
简单语句组
    类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
'''


def simple_statement():
    flag = 1
    counter = 0
    while flag: counter += 1;print('hello', counter)


# simple_statement()
