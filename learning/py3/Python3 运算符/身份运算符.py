"""
身份运算符用于比较两个对象的存储单元

运算符	                描述	                                实例
is	        is 是判断两个标识符是不是引用自一个对象	        x is y, 类似 id(x) == id(y) ,
                                                            如果引用的是同一个对象则返回 True，否则返回 False
is not	    is not 是判断两个标识符是不是引用自不同对象	    x is not y ，
                                                            类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

注：
    id() 函数用于获取对象内存地址。
以下实例演示了Python所有身份运算符的操作：
"""
# !/usr/bin/python3

a = 20
b = 20

if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if id(a) == id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
