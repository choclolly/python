"""
以下表格列出了从最高到最低优先级的所有运算符：

运算符	                        描述
**	                        指数 (最高优先级)
~ + -	                    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	                乘，除，求余数和取整除
+ -	                        加法减法
>> <<	                    右移，左移运算符
&	                        位 'AND'
^ |	                        位运算符
<= < > >=	                比较运算符
== !=	                    等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	                身份运算符
in not in	                成员运算符
not and or	                逻辑运算符
"""

# !/usr/bin/python3

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)

e = (a + b) * (c / d);  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)

e = a + (b * c) / d;  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)

'''
and 拥有更高优先级:
'''

x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")

''''
注意：Pyhton3 已不支持 <> 运算符，可以使用 != 代替，如果你一定要使用这种比较运算符，可以使用以下的方式：
>>> from __future__ import barry_as_FLUFL
>>> 1 <> 2
True
'''
