"""
Python 没有单独的字符类型，一个字符就是长度为1的字符串。
"""
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])

'''
P n
n P
'''

'''
与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
'''
word[0] = 'm'