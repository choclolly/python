from package1 import *

p.prt(4, '从一个包中导入*')

'''
4、
    设想一下，如果我们使用 from sound.effects import *会发生什么
        Python 会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。
    Windows是一个大小写不区分的系统。
        在这类平台上，没有人敢担保一个叫做 ECHO.py 的文件导入为模块 echo 还是 Echo 甚至 ECHO。
    为了解决这个问题，只能烦劳包作者提供一个精确的包的索引了。
    导入语句遵循如下规则：
        如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
        那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
    作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊。你说我就不这么做，我就不使用导入*这种用法，好吧，没问题，谁让你是老板呢
'''


def package_example():
    p.prt(4,
          'learning/py3/0-1/package1/__init__.py存在 __all__ = [\'p\'],顶部使用from package1 import * ,只导入了 package1包下的p模块')
    p2.prt(4,
           'learning/py3/0-1/package1/__init__.py存在 __all__ = [\'p\',\'p2\'],顶部使用from package1 import * ,只导入了 package1包下的p模块')


package_example()
