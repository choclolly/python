def prt(num=0, str=''):
    print('---------')
    # print('%s、%s' % (num, str))
    print(f'{num}、{str}')


def prt2():
    print('---------')


if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
