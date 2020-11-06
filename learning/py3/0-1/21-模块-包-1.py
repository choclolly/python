import p
import package1.p

p.prt(1, '包1')
'''
包
    包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
    比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
    就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
    这样不同的作者都可以提供 NumPy 模块，或者是 Python 图形库。


    在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
    目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
    最简单的情况，放一个空的 :file:__init__.py就可以了。当然这个文件中也可以包含一些初始化代码

    这里给出了一种可能的包结构（在分层的文件系统中）
        sound/                          顶层包
            __init__.py               初始化 sound 包
        formats/                  文件格式转换子包
            __init__.py
            wavread.py
            wavwrite.py
            aiffread.py
            aiffwrite.py
            auread.py
            auwrite.py
            ...
        effects/                  声音效果子包
            __init__.py
            echo.py
            surround.py
            reverse.py
            ...
        filters/                  filters 子包
            __init__.py
            equalizer.py
            vocoder.py
            karaoke.py
            ...

    导入子模块的方式
        1、导入子模块:package1.p。 他必须使用全名去访问
            import package1.p
        2、还有一种导入子模块的方法是:
            from package1 import p
                同样会导入子模块: p，并且他不需要那些冗长的前缀，所以他可以这样使用
        3、还有一种变化就是直接导入一个函数或者变量:
            from package1.p import prt
                同样的，这种方法会导入子模块: p，并且可以直接使用他的 prt() 函数


    注意
        当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
        import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，抛出一个 :exc:ImportError 异常。
        反之，如果使用形如 import item.subitem.subsubitem 这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，
        但是不可以是类，函数或者变量的名字。
    总结
        learning/py3/0-1/21-模块-包-5.py
'''

'''
1、导入子模块:package1.p。 他必须使用全名去访问
        import package1.p
'''
def package_example():
    # 访问的是 当前包下的模块p
    p.prt(10000, '测试点模块名称')
    '''
    输出
        ---------
        10000、测试点模块名称
    '''

    # 访问子模块:package1.p。 他必须使用全名去访问
    package1.p.prt(20000, '测试点模块名称')
    '''
    输出
        =========
        20000、测试点模块名称
    '''


package_example()
