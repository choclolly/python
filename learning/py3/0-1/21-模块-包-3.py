from package1.p import prt

p.prt(3, '包3')
'''
3、还有一种变化就是直接导入一个函数或者变量:
        from package1.p import prt
    这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:
'''


def package_example():
    # 访问的是 当前包下的模块p
    prt(10000, '测试点模块名称')
    '''
    输出
        =========
        10000、测试点模块名称
    '''

    # 访问子模块:package1.p。 他必须使用全名去访问
    prt(20000, '测试点模块名称')
    '''
    输出
        =========
        20000、测试点模块名称
    '''


package_example()
