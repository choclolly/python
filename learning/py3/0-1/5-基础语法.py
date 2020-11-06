#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
编码
    第一行是指定python解释器，
    第二行是指定python文件编码方式
    默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
        # -*- coding: cp-1252 -*-
'''


def code():
    s = '中文'  # 注意这里的 str 是 str 类型的，而不是 unicode
    print('1.默认中文编码     :{}'.format(s))
    print('2.重新编码        :%s' % s.encode('gb18030'))


# code()

'''
标识符
    第一个字符必须是字母表中字母或下划线 _ 。
    标识符的其他的部分由字母、数字和下划线组成。
    标识符对大小写敏感。
'''


def identifier():
    s = '中文'
    哈哈 = '中文——哈哈'  # 在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。
    print(s)
    print(哈哈)


# identifier()

'''
python保留字
'''
import keyword


def key_word():
    print(keyword.kwlist)


# key_word()

'''
注释
    Python中单行注释以 # 开头，实例如下：
    多行注释可以用多个 # 号，还有 \'\'\':三单引号 和 """:三双引号
'''


def notes():
    # 第一个注释
    print("Hello, Python!")  # 第二个注释


# notes()
'''
行与缩进
    python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
    缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数,缩进不一致，会导致运行错误。实例如下：
'''


def lines_and_indents():
    i = 1
    if i == 1:
        print('True')
    else:
        print("False")
        # print('缩进不一致，会导致运行错误')


# linesandindents()

'''
多行语句
    Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：sql.
    在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
'''


def multiline_statement():
    sql = 'insert into uc_user (id,name,age,birthday,create_time) values ' \
          '(1,haodonghui,31,\'19880520\',int(round(time.time() * 1000)))'
    list_num = [1, 2, 3, 4,
                5, 6,
                7]
    print(sql)
    print(list_num)


# multiline_statement()

'''
数字(Number)类型
    python中数字有四种类型：整数、布尔型、浮点数和复数。
        int (整数), 
            如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
        bool (布尔), 
            如 True。
        float (浮点数), 
            如 1.23、3E-2
        complex (复数), 
            如 1 + 2j、 1.1 + 2.2j
'''


def num():
    i = 1
    b = True
    f = 1.2
    c = 1 + 2j
    print(i)
    print(b)
    print(f)
    print(c)


# num()

'''
字符串(String)
    python中单引号和双引号使用完全相同。
    使用三引号(\'\'\'或""")可以指定一个多行字符串。
    转义符 '\'
    反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
    按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
    字符串可以用 + 运算符连接在一起，用 * 运算符重复。
    Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    Python中的字符串不能改变。
    Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
    字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''


def st_r():
    word = '字符串'
    sentence = "这是一个句子。"
    paragraph = """这是一个段落，
    可以由多行组成"""
    print(word)
    print(sentence)
    print(paragraph)

    s = 'haodonghui'
    print(s)  # 输出字符串
    print(s[-1])    # 输出字符串最后一个字符
    print(s[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(s[0])  # 输出字符串第一个字符
    print(s[3:5])  # 输出从第三个开始到第五个的字符,不包含第五个字符
    print(s[2:])  # 输出从第二个开始后的所有字符
    print(s * 2)  # 输出字符串两次
    print(s + '你好')  # 连接字符串
    print('------------------------------')
    print('hao\ndonghui')  # \n 换行, 使用反斜杠(\)+n转义特殊字符
    print(r'hao\ndonghui')  # \n 换行, 在字符串前面添加一个 r，表示原始字符串，不会发生转义


st_r()

'''
空行
    函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
    空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
    记住：空行也是程序代码的一部分。
'''


def empty_line():
    print('记住：空行也是程序代码的一部分。')


# empty_line()

'''
等待用户输入
    执行下面的程序在按回车键后就会等待用户输入：
        \n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出
'''


def input_something():
    input('\n\n按下enter键后推出')


# input_something()

'''
同一行显示多条语句
    Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
        import sys;x = 'haodonghui1';sys.stdout.write(x + '\n')
    不过一般不这么用
    
'''
import sys


def one_line_with_many_sentences():
    x = 'haodonghui'
    sys.stdout.write(x + '\n')


# one_line_with_many_sentences()

'''
多个语句构成代码组
    缩进相同的一组语句构成一个代码块，我们称之代码组。
    像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
    我们将首行及后面的代码组称为一个子句(clause)。
'''


def code_group():
    i = 2
    if i > 1:
        print("i:{}大于1".format(i))
    elif i < 1:
        print("i:{}小于1".format(i))
    else:
        print("i:{}等于1".format(i))


# code_group()

'''
Print 输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
'''


def print_():
    x = 'a'
    y = 'b'
    # 换行输出
    print(x)
    print(y)
    print('---------')
    # 不换行输出
    print(x, end="")
    print(y, end="")


# print_()

'''
import 与 from...import
    在 python 用 import 或者 from...import 来导入相应的模块。
        将整个模块(somemodule)导入，格式为： import somemodule
        从某个模块中导入某个函数,格式为： from somemodule import somefunction
        从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
        将某个模块中的全部函数导入，格式为： from somemodule import *
'''

# 导入 sys 模块
import sys
# 导入 sys 模块的 argv,path 成员
from sys import argv, path


def command_line_parameters():
    print('命令行参数为:')
    for i in sys.argv:
        print(i)
    print('\n python 路径为', sys.path)
    print('================python from import===================================')
    print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path


# command_line_parameters()


'''
命令行参数
    很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息：
    windows cmd命令:
        python -h
'''