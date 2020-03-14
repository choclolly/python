"""
is 与 == 区别：
    is 用于判断两个变量引用对象是否为同一个，
    is运算符比较判断的是对象间的唯一身份标识，也就是id是否相同
    == 用于判断引用变量的值是否相等。
"""
# == 用于判断引用变量的值是否相等
# 数字类型
a = 1
b = 1
print('数字类型')
print(a == b)  # True
print(a is b)  # True
print(id(a))  # 140730412137536
print(id(b))  # 140730412137536

# 字符串类型
print()
a = 'china'
b = 'china'
print('字符串类型')
print(a == b)  # True
print(a is b)  # True
print(id(a))  # 1970844570736
print(id(b))  # 1970844570736

# 列表类型
print()
print('列表类型')
x = y = [4, 5, 6]
z = [4, 5, 6]
print(x == y)  # True
print(x == z)  # True
print(x is y)  # True
print(x is z)  # False
print(id(x))  # 2026665497096
print(id(y))  # 2026665497096
print(id(z))  # 2026665497608

# 元组类型
print()
print("元组类型")
a = (1, 2, 3)
b = (1, 2, 3)
print(a == b)  # True
print(a is b)  # True
print(id(a))  # 2640199698056
print(id(b))  # 2640199698056

# 集合类型类型
print()
print("集合类型类型")
a = {1, 2, 3}
b = {1, 2, 3}
print(a == b)  # True
print(a is b)  # False
print(id(a))  # 2255406589096
print(id(b))  # 2255406588200

# 字典类型
print()
print("字典类型")
a = {'a': 1, 'b': 2}
b = {'a': 1, 'b': 2}
print(a == b)  # True
print(a is b)  # False
print(id(a))  # 2640171387544
print(id(b))  # 2640171387624


'''
观察结果发现
    不可变数据   a is b 为True
        Number（数字）、String（字符串）、Tuple（元组）
    可变数据    a is b为False
        List（列表）、Dictionary（字典）、Set（集合）。
    
    不可变数据（3 个）：
        Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：
            List（列表）、Dictionary（字典）、Set（集合）。
'''
