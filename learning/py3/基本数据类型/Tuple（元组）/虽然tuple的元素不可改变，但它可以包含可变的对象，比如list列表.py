# list
# tuple不可变
b = ('abcd', 786, 2.23, 'runoob', [123, 'runoob'])
# 包含a为list，list可变
a = b[-1]
print(a)  # list列表 [123, 'runoob']
print(type(a))  # <class 'list'>
a[0] = 456
print(a)
a[0:] = [789, 101112]  # 将对应的元素值设置为 []
print(a)

'''
观察结果可发现 元组包含的可变对象，比如list 改变了
    [123, 'runoob']
    <class 'list'>
    [456, 'runoob']
    [789, 101112]
'''
