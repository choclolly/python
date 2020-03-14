list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[2:])  # 输出从第三个元素开始的所有元素

list[2:] = []   # 将对应的元素值设置为 []
print(list)
print(list[2:])

'''
['abcd', 786, 2.23, 'runoob', 70.2]
[2.23, 'runoob', 70.2]
['abcd', 786]
[]
'''