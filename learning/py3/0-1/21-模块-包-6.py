from package2 import p
from package2 import p2
# 在执行 from...import 前，包 package2 中的 p 和 p2 模块都被导入到当前的命名空间中了，并且他【不会破坏】掉我们在这句话之前导入的所有明确指定的模块
from package2 import *

# p.prt(4, '从一个包中导入*')

'''
5、
    如果 __all__ 真的没有定义，那么使用from package1 import *这种语法的时候，就不会导入包 package1 里的任何子模块。
    他只是把包package1和它里面定义的所有内容导入进来（可运行__init__.py里定义的初始化代码）。
    
    这会把 __init__.py 里面定义的所有名字导入进来。并且他【不会破坏】掉我们在这句话之前导入的所有明确指定的模块
    这个例子中,在执行 from...import 前，包 package2 中的 p 和 p2 模块都被导入到当前的命名空间中了。（当然如果定义了 __all__ 就更没问题了）
    
    通常我们并不主张使用 * 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。
    不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。
    
    记住，使用 from Package import specific_submodule 这种方法永远不会有错。事实上，这也是推荐的方法。
    除非是你要导入的子模块有可能和其他包的子模块重名。
    
     
'''


def package_example():
    # __all__ 真的没有定义 的时候    from package2 import *  就不会导入包 package1 里的任何子模块，所以下面会报错
    p.prt(4, 'from package2 import p 导入了 package2 包下的 p 模块')
    print('\n')
    p2.prt(4, 'from package2 import p2 导入了 package2 包下的 p2 模块')
    print('\n')
    # 可运行__init__.py里定义的初始化代码
    prt()  # 我是__init__.py


package_example()
