# 参考： https://www.cnblogs.com/ding2016/p/14281923.html
'''
添加元素/添加键值对
'''
# 1. 使用中括号 [ ]  说明：中括号指定key名，等于一个value，如果key不存在，那么添加该键值对；如果key存在，那么覆盖修改其对应的value。
aaa = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
aaa['E'] = 5
print(aaa)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

#  2. 使用update()方法  说明：关键字参数形式，key对象只能是字符串对象
aaa.update({'F': 7})
print(aaa)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7}
aaa.update({'G': 8, 'H': 9})
print(aaa)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9}
# aaa.update({I: 8, J: 9})    # # NameError: name 'I' is not defined
aaa.update({'I': 8, 'J': 9})
print(aaa)  # NameError: name 'I' is not defined {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9}

'''
删除元素/删除键值对
'''
# 1. del 函数
aaa = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9}
del [aaa['A']]
print(aaa)  # {'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9, 'I': 8, 'J': 9}
del [aaa['B']]
print(aaa)  # {'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9, 'I': 8, 'J': 9}
del [aaa['C'], aaa['D']]
print(aaa)  # {'E': 5, 'F': 7, 'G': 8, 'H': 9, 'I': 8, 'J': 9}

# 2. pop()方法        注意：使用pop方法会返回要删除key的value，可以接收一下，用作他用，一些场景也会使用到
aaa = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9}
bbb = aaa.pop('G')
print(bbb)  # 8
print(aaa)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'H': 9}

# 3. popitem()方法    注意：popitem() 方法返回并删除字典中的最后一对键和值
aaa = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9}
bbb = aaa.popitem()
print(bbb)  # ('H', 9)

# 4. clear()方法, 清空字典内所有键值对
aaa = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 7, 'G': 8, 'H': 9}
aaa.clear()
print(aaa)  # {}