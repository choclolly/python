'''
Python 解释器内置了很多函数和类型，您可以在任何时候使用它们。以下按字母表顺序列出它们。
    https://www.runoob.com/python/python-built-in-functions.html
    abs()	divmod()	input()	open()	staticmethod()
    all()	enumerate()	int()	ord()	str()
    any()	eval()	isinstance()	pow()	sum()
    basestring()	execfile()	issubclass()	print()	super()
    bin()	file()	iter()	property()	tuple()
    bool()	filter()	len()	range()	type()
    bytearray()	float()	list()	raw_input()	unichr()
    callable()	format()	locals()	reduce()	unicode()
    chr()	frozenset()	long()	reload()	vars()
    classmethod()	getattr()	map()	repr()	xrange()
    cmp()	globals()	max()	reverse()	zip()
    compile()	hasattr()	memoryview()	round()	__import__()
    complex()	hash()	min()	set()
    delattr()	help()	next()	setattr()
    dict()	hex()	object()	slice()
    dir()	id()	oct()	sorted()	exec 内置表达式
'''
'''
    描述
        abs() 函数返回数字的绝对值。
    语法
        以下是 abs() 方法的语法:
            abs( x )
        参数
            x -- 数值表达式。
    返回值
        函数返回x（数字）的绝对值。
'''


def f_abs():
    print('abs(-10): %s' % abs(-10))  # 10


# f_abs()

#  id() 函数用于获取对象内存地址
def f_id():
    a = 20
    b = 20
    if id(a) == id(b):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")

    # 重新赋值,修改变量 b 的值
    a = 20
    b = 30
    if id(a) == id(b):
        print("2 - a 和 b 有相同的标识")
    else:
        print("2 - a 和 b 没有相同的标识")
f_id()