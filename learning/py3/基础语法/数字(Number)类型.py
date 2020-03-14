"""
python中数字有四种类型：整数、布尔型、浮点数和复数。

    int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    bool (布尔), 如 True。
    float (浮点数), 如 1.23、3E-2
    complex (复数), 如 1 + 2j、 1.1 + 2.2j
"""

A = 1
b = True
c, d = 1.23, 3E-2
e, f = 1 + 2j, 1.1 + 2.2j

print(A)
print(type(A))
print(b)
print(type(b))
print(c, d)
print(type(c), type(d))
print(e, f)
print(type(e), type(f))

"""
输出
    1
    <class 'int'>
    True
    <class 'bool'>
    1.23 0.03
    <class 'float'> <class 'float'>
    (1+2j) (1.1+2.2j)
    <class 'complex'> <class 'complex'>
"""