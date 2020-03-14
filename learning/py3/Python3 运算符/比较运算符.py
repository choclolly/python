"""
以下假设变量a为10，变量b为20：
运算符	               描述	                                                      实例
==	               等于 - 比较对象是否相等	                                    (a == b) 返回 False。
!=	               不等于 - 比较两个对象是否不相等	                            (a != b) 返回 True。
>	               大于 - 返回x是否大于y	                                    (a > b) 返回 False。
<	               小于 - 返回x是否小于y。所有比较运算符返回1表示真，
                         返回0表示假。这分别与特殊的变量True和False等价。
                         注意，这些变量名的大写。	                            (a < b) 返回 True。
>=	               大于等于 - 返回x是否大于等于y。	                            (a >= b) 返回 False。
<=	               小于等于 - 返回x是否小于等于y。	                            (a <= b) 返回 True。

注意：
    Pyhton3 已不支持 <> 运算符，可以使用 != 代替，如果你一定要使用这种比较运算符，可以使用以下的方式：
        from __future__ import barry_as_FLUFL
        print(1 <> 2)
        True
"""

# !/usr/bin/python3

a = 21
b = 10
c = 0

if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a < b:
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if a > b:
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if b >= a:
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")
