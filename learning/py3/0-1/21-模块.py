import p

p.prt(1, '模块')
'''
模块
    用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了.
    为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块
    比如:p.py
    模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
'''
# 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
import sys


def print_sys_argv():
    # 命令行参数如下:
    # 2、sys.argv 是一个包含命令行参数的列表。
    for x in sys.argv:
        print(x)

    # 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
    print('\nPython 路径为：', sys.path, '\n')


# print_sys_argv()


p.prt(2, 'import 语句')
'''
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下
    import module1[, module2[,... moduleN]
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 p，需要把命令放在脚本的顶端：
    import p
一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行
'''

p.prt(3, 'from … import 语句')
'''
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下
    from modname import name1[, name2[, ... nameN]]

这个声明不会把整个p模块导入到当前的命名空间中，它只会将p里的prt2函数引入进来
'''

from p import prt2

print(prt2())

p.prt(4, 'from … import * 语句')
'''
from … import * 语句
    把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
        from modname import *
这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
'''

p.prt(5, '深入模块')
'''
模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行
每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用

1、当你确实知道你在做什么的话，你也可以通过 modname.itemname 这样的表示法来访问模块内的函数
    p.prt2()
2、还有一种导入的方法，可以使用 import 直接把模块内（函数，变量的）名称导入到当前操作模块
    from p import prt2
        这种导入的方法不会把被导入的模块的名称放在当前的字符表中（所以在这个例子里面，p 这个名称是没有定义的）
3、这还有一种方法，可以一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表
    from p import *
        这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。大多数情况， 
        Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义
'''

p.prt(5, '__name__属性')
'''
__name__属性
    一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
    我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
    
    D:\python\learning\py3\0-1>python p.py
    程序自身在运行
    
    D:\python\learning\py3\0-1>python
    Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import p
    我来自另一模块
    >>>
    
    说明： 
        每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
    说明：
        __name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
'''

p.prt(6, 'dir() 函数')
'''
dir() 函数
    内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
    如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
'''


def func_dir():
    # 得到一个当前模块中定义的属性列表
    print(dir())
    a = 5
    print(a)
    print(dir())  # ['a']

    print(dir(p))
    # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'prt', 'prt2']


func_dir()

p.prt(7, '标准模块')
'''
标准模块
    Python 本身带着一些标准的模块库，
    这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串
        >>> import sys
        >>> sys.ps1
        '>>> '
        >>> sys.ps2
        '... '
        >>> sys.ps1='C>'
        C>print('h')
        h

'''

p.prt(8, '包')

from package1 import p

# 使用的是package1下模块p的函数prt
print(p.prt(0000, '测试包'))

# 再次导入p
import p

# 这时候使用的是p模块的函数prt
print(p.prt(0000, '测试包'))
