import p

p.prt(1, '列表')
'''
序列是 Python 中最基本的数据结构。
序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。
Python 有 6 个序列的内置类型，但最常见的是列表和元组。
'''


# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
def c_list():
    list1 = ['Google', 'Runoob', 1997, 2000]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]
    list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    print(list1, list2, list3, list4)


# c_list()


p.prt(2, '访问列表中的值')
'''
与字符串的索引一样，列表索引从 0 开始，第二个索引是 1，依此类推。
通过索引列表可以进行截取、组合等操作
索引也可以从尾部开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推
使用下标索引来访问列表中的值，同样你也可以使用方括号 [] 的形式截取字符
'''


def visit_list():
    list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    print(list[0])
    print(list[1])
    print(list[2])

    print(list[-1])
    print(list[-2])
    print(list[-3])

    # 读取第二位
    print("list[1]: ", list[1])
    # 从第二位开始（包含）截取到倒数第二位（不包含）
    print("list[1:-2]: ", list[1:-2])


# visit_list()


p.prt(3, '更新列表')
'''
你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项
'''


def update_list():
    list = ['Google', 'Runoob', 1997, 2000]

    print("第三个元素为 : ", list[2])
    list[2] = 2001
    print("更新后的第三个元素为 : ", list[2])


# update_list()

p.prt(4, '删除列表元素')
'''可以使用 del 语句来删除列表的的元素'''


def del_list():
    list = ['Google', 'Runoob', 1997, 2000]

    print("原始列表 : ", list)
    del list[2]
    print("删除第三个元素 : ", list)


# del_list()


p.prt(5, '列表脚本操作符')
'''
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表
    Python 表达式	        结果	                                描述
    len([1, 2, 3])	        3	                                长度
    [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	                组合
    ['Hi!'] * 4	            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	    重复
    3 in [1, 2, 3]	        True	                        元素是否存在于列表中
    for x in [1, 2, 3]: 
        print(x, end=" ")	1 2 3	                            迭代
'''

p.prt(6, '列表截取与拼接')
'''
列表截取与字符串操作类型
L=['Google', 'Runoob', 'Taobao']
    Python 表达式	结果	                    描述
    L[2]	        'Taobao'	            读取第三个元素
    L[-2]	        'Runoob'	            从右侧开始读取倒数第二个元素: count from the right
    L[1:]	        ['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素
'''


def sub_and_splicing():
    # 截取
    L = ['Google', 'Runoob', 'Taobao']
    print(L[2])
    print(L[-2])
    print(L[1:])

    # 拼接
    squares = [1, 4, 9, 16, 25]
    squares += [36, 49, 64, 81, 100]
    print(squares)


# sub_and_splicing()

p.prt(7, '嵌套列表')
'''
使用嵌套列表即在列表里创建其它列表
'''


def nesting_list():
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
    print(x[0])  # ['a', 'b', 'c']
    print(x[0][1])  # b


# nesting_list()


p.prt(8,'列表函数&方法')
'''
包含以下函数:
    序号	函数
    1	len(list)   列表元素个数
    2	max(list)   返回列表元素最大值
    3	min(list)   返回列表元素最小值
    4	list(seq)   将元组转换为列表

包含以下方法
    序号	    方法
    1	list.append(obj)        在列表末尾添加新的对象
    2	list.count(obj)         统计某个元素在列表中出现的次数
    3	list.extend(seq)        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    4	list.index(obj)         从列表中找出某个值第一个匹配项的索引位置
    5	list.insert(index, obj) 将对象插入列表
    6	list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    7	list.remove(obj)        移除列表中某个值的第一个匹配项
    8	list.reverse()          反向列表中元素
    9	list.sort( key=None, reverse=False) 对原列表进行排序
    10	list.clear()            清空列表
    11	list.copy()             复制列表
'''