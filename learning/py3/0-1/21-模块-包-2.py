from package1 import p

p.prt(2, '包2')
'''
2、还有一种导入子模块的方法是:
    from package1 import p
        同样会导入子模块: p，并且他不需要那些冗长的前缀，所以他可以这样使用
'''


def package_example():
    # 访问的是 当前包下的模块p
    p.prt(10000, '测试点模块名称')
    '''
    输出
        =========
        10000、测试点模块名称
    '''

    # 访问子模块:package1.p。 他必须使用全名去访问
    p.prt(20000, '测试点模块名称')
    '''
    输出
        =========
        20000、测试点模块名称
    '''


package_example()
