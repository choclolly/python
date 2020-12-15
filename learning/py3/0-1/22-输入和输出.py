from package2 import p2
import p

p2.prt(1, '输入和输出')
'''
输出格式美化
    Python两种输出值的方式: 
        表达式语句
        print() 函数。
    第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用
    如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值
    如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    
    str()： 函数返回一个用户易读的表达形式。
    repr()： 产生一个解释器易读的表达形式。
'''

a = 0
sum = 0
while a < 5:
    sum += a  # sum = sum+a
    a += 1  # a = a+1
print(sum)

p2.prt(2, "输出格式美化")


def in_and_out():
    s = 'Hello World!'
    print(s)  # Hello World!
    print(str(s))  # Hello World!

    print(repr(s))  # 'Hello World!'

    print(str(1 / 7))  # 0.14285714285714285


# in_and_out()

p2.prt(2.1, "平方立方表")
'''平方立方表
    这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
    还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串
'''


def square_cubic_table():
    #  每列间的空格由 print() 添加
    for x in range(1, 12):
        print(x, x * x, x * x * x)
    p.prt2()
    for x in range(1, 12):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        print(repr(x * x * x).rjust(4))
    p.prt2()
    for x in range(1, 12):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))


# square_cubic_table()

'''另一个方法 zfill(), 它会在数字的左边填充 0
    返回长度为 width 的字符串，原字符串右对齐，前面填充0
'''


def str_zfill():
    print('2'.zfill(3))  # 002
    print('-3.14'.zfill(7))  # -003.14
    print('3.14159265359'.zfill(5))  # 3.14159265359
    print('3.14159265359'.zfill(20))  # 003.14159265359


# str_zfill()

p2.prt(2.2, "str.format() 的基本使用如下:")
'''
括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
    print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))   # 菜鸟教程网址： "www.runoob.com!"
在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
    print('{0} 和 {1}'.format('Google', 'Runoob'))   # Google 和 Runoob
    print('{1} 和 {0}'.format('Google', 'Runoob'))   # Runoob 和 Google
如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。  
    print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
位置及关键字参数可以任意的结合:
    print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
    print('常量 PI 的值近似为： {}。'.format(math.pi))
    print('常量 PI 的值近似为： {!r}。'.format(math.pi))
    print('常量 PI 的值近似为： {!a}。'.format('你好'))
可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后五位：
    print('常量 PI 的值近似为 {0:.5f}。'.format(math.pi))   # 常量 PI 的值近似为 3.14159。
    print('常量 PI 的值近似为 {1:.5f},{0:.3f}。'.format(math.pi, 1.23456789))  # 常量 PI 的值近似为 1.23457,3.142。
在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
    table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
    for name, number in table.items():
        print('{0:10} ==> {1:10d}'.format(name, number))
如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
    最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
        table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
        print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
    也可以通过在 table 变量前使用 ** 来实现相同的功能：
        table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
        print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
'''
import math


def str_format():
    print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))  # 菜鸟教程网址： "www.runoob.com!"

    print('{0} 和 {1}'.format('Google', 'Runoob'))  # Google 和 Runoob
    print('{1} 和 {0}'.format('Google', 'Runoob'))  # Runoob 和 Google

    print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))  # 菜鸟教程网址： www.runoob.com

    print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))  # 站点列表 Google, Runoob, 和 Taobao。

    print('常量 PI 的值近似为： {}。'.format(math.pi))  # 常量 PI 的值近似为： 3.141592653589793。
    print('常量 PI 的值近似为： {!r}。'.format(math.pi))  # 量 PI 的值近似为： 3.141592653589793。
    print('常量 PI 的值近似为： {!a}。'.format('你好'))  # 常量 PI 的值近似为： '\u4f60\u597d'。

    print('常量 PI 的值近似为 {0:.5f}。'.format(math.pi))  # 常量 PI 的值近似为 3.14159。
    print('常量 PI 的值近似为 {1:.5f},{0:.3f}。'.format(math.pi, 1.23456789))  # 常量 PI 的值近似为 1.23457,3.142。

    table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
    for name, number in table.items():
        print('{0:10} ==> {1:10d}'.format(name, number))


# str_format()

p2.prt(3, "旧式字符串格式化")
'''
% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
    import math
    print('常量 PI 的值近似为：%5.3f。' % math.pi)   # 常量 PI 的值近似为：3.142。
因为 str.format() 是比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().
'''

p2.prt(4, "读取键盘输入")
'''
Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
input 可以接收一个Python表达式作为输入，并将运算结果返回。
'''


def read_keyboard_enter():
    str = input("请输入：");
    print("你输入的内容是: ", str)


p2.prt(5, "读和写文件")
'''
open() 将会返回一个 file 对象，基本语法格式如下:
    open(filename, mode)
    
    filename：包含了你要访问的文件名称的字符串值。
    mode：决定了打开文件的模式：只读，写入，追加等。
        所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
            模式	    描述
            r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
            rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
            r+	打开一个文件用于读写。文件指针将会放在文件的开头。
            rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
            w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
            wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
            w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
            wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
            a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
            ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
            a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
            ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
            
            
            模式	        r	r+	w	w+	a	a+
            读	        +	+		+		+
            写		    +	+	+	+	+
            创建			+	+	+	+
            覆盖			+	+		
            指针在开始	+	+	+	+		
            指针在结尾					+	+
'''

def write_to_foo_file():
    # 打开一个文件
    f = open("foo.txt", "w")

    f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

    # 关闭打开的文件
    f.close()

# write_to_foo_file()

p.prt(6,'文件对象的方法')
'''
f.read()
    为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
    size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
f.readline()
    f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
f.readlines() 将返回该文件中包含的所有行。
    如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
    另一种方式是迭代一个文件对象然后读取每行:
f.write()
    f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
    
    如果要写入一些不是字符串的东西, 那么将需要先进行转换:
        # 打开一个文件
        f = open("/tmp/foo1.txt", "w")
        
        value = ('www.runoob.com', 14)
        s = str(value)
        f.write(s)
        
        # 关闭打开的文件
        f.close()
f.tell()
    f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
'''

def file_read():
    f = open("foo.txt", "r")
    str = f.read()
    print(str)

    # 关闭打开的文件
    f.close()

# file_read()

def file_readline():
    f = open("foo.txt", "r")
    str = f.readline()
    print(str)

    # 关闭打开的文件
    f.close()

# file_readline()   # Python 是一个非常好的语言。

def file_readlines():
    f = open("foo.txt", "r")
    str = f.readlines()
    print(str)

    # 关闭打开的文件
    f.close()

# file_readlines()    # ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']


def file_readlines_other_m():
    f = open("foo.txt", "r")
    for line in f:
        print(line,end=" ")
    # 关闭打开的文件
    f.close()

# file_readlines_other_m()

def file_write():
    # 打开一个文件
    f = open("foo_1.txt", "w")

    num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    print(num)
    # 关闭打开的文件
    f.close()

# file_write()

def file_write_1():
    # 打开一个文件
    f = open("foo_2.txt", "w")

    value = ('www.runoob.com', 14)
    s = str(value)
    f.write(s)

    # 关闭打开的文件
    f.close()

# file_write_1()
def file_tell():
    print("1")
