import sys

print('参数个数为:', len(sys.argv), '个参数。')
print('参数列表:', str(sys.argv))

'''
Python3 命令行参数
执行Python3 命令行参数.py
    D:\python\learning\py3\基础语法>py "连接mysql-connector.py"
    参数个数为: 1 个参数。
    参数列表: ['连接mysql-connector.py']
    
    D:\python\learning\py3\基础语法>py "连接mysql-connector.py" arg1 arg2 arg3
    参数个数为: 4 个参数。
    参数列表: ['连接mysql-connector.py', 'arg1', 'arg2', 'arg3']
    
    D:\python\learning\py3\基础语法>

'''

'''
exit()
    退出py命令行
Python 提供了 getopt 模块来获取命令行参数。
Python 中也可以所用 sys 的 sys.argv 来获取命令行参数：
    sys.argv 是命令行参数列表。
    len(sys.argv) 是命令行参数个数。
    注：sys.argv[0] 表示脚本名。
'''
