"""
getopt模块
    getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。命令行选项使得程序的参数更加灵活。
    支持短选项模式（-）和长选项模式（--）。

该模块提供了两个方法及一个异常处理来解析命令行参数。
    方法
        getopt.getopt 方法
            getopt.getopt 方法用于解析命令行参数列表，语法格式如下：
                getopt.getopt(args, options[, long_options])
                    方法参数说明：
                        args: 要解析的命令行参数列表。
                        options: 以字符串的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
                        long_options: 以列表的格式定义，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
            该方法返回值由两个元素组成:
                第一个是 (option, value) 元组的列表。
                第二个是参数列表，包含那些没有'-'或'--'的参数。
        getopt.gnu_getopt 方法
            这里不多做介绍。
    异常
        Exception getopt.GetoptError
            在没有找到参数列表，或选项的需要的参数为空时会触发该异常。
            异常的参数是一个字符串，表示错误的原因。属性 msg 和 opt 为相关选项的错误信息。
"""
import sys
import getopt


def main(argv):
    # print('参数个数为:', len(argv), '个参数。')
    # print('参数列表:', str(argv))
    i = ''
    o = ''
    try:
        # opts 元组列表(option, value)；
        # args 参数列表
        opts, args = getopt.getopt(argv, "ha:b:c:", ["g", "d=", "e=", "f="])
        print(type(opts))  # <class 'list'>
        print(type(args))  # # <class 'list'>
    except getopt.GetoptError as err:
        print(str(err))
        print('在没有找到参数列表，或选项的需要的参数为空时会触发该异常。')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('表示该选项无须有附加的参数,因为h后面没有冒号(:)')
            sys.exit()
        elif opt == '--g':
            print('表示该选项无须有附加的参数,因为g后面没有等号(=)')
        elif opt in ("-a", "--d"):  # 如果选项串都有那么后边的会覆盖前面的:选项串d的附加参数，会覆盖掉选项串a的附加参数
            i = arg
        elif opt in ("-b", "-c", "--e", "--f"):  # 如果选项串都有那么后边的会覆盖前面的:选项串d的附加参数，会覆盖掉选项串a的附加参数
            o = arg
    print('输入为：', i)
    print('输出为：', o)


if __name__ == "__main__":
    # sys.argv[0] 表示脚本名;sys.argv[1:] 表示输出从第三个开始后的所有字符
    main(sys.argv[1:])

'''
开始测试

D:\python\learning\py3\基础语法\命令行参数>py test2.py -t
option -t not recognized
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

D:\python\learning\py3\基础语法\命令行参数>py test2.py -a
option -a requires argument
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

D:\python\learning\py3\基础语法\命令行参数>py test2.py -h
<class 'list'>
<class 'list'>
连接mysql-connector.py -i <inputfile> -o <outputfile> 2

D:\python\learning\py3\基础语法\命令行参数>py test2.py -g
option -g not recognized
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

D:\python\learning\py3\基础语法\命令行参数>py test2.py --g
<class 'list'>
<class 'list'>
输入为：
输出为：

D:\python\learning\py3\基础语法\命令行参数>py test2.py --g
<class 'list'>
<class 'list'>
表示该选项无须有附加的参数,因为g后面没有等号(=)
输入为：
输出为：

D:\python\learning\py3\基础语法\命令行参数>py test2.py -t
option -t not recognized
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

D:\python\learning\py3\基础语法\命令行参数>py test2.py -h 1
<class 'list'>
<class 'list'>
表示该选项无须有附加的参数,因为h后面没有冒号(:)

D:\python\learning\py3\基础语法\命令行参数>py test2.py -h
<class 'list'>
<class 'list'>
表示该选项无须有附加的参数,因为h后面没有冒号(:)

D:\python\learning\py3\基础语法\命令行参数>py test2.py -a
option -a requires argument
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

D:\python\learning\py3\基础语法\命令行参数>py test2.py -a 1
<class 'list'>
<class 'list'>
输入为： 1
输出为：

D:\python\learning\py3\基础语法\命令行参数>py test2.py -a 1 --d 2
<class 'list'>
<class 'list'>
输入为： 1
输出为：

注：这个比较特殊 因为         
    elif opt in ("-a", "--d"):
        i = arg
    选项串d的附加参数，会覆盖掉选项串a的附加参数

'''
