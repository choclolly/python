'''
将一个字符串拆分成一个字符列表。在Python中，字符只是长度为1的字符串。list()函数将字符串转换为单个字母的列表。
'''
l = list('hello world')
print(l)  # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

'''
思考
    有一个单词列表，你如何将它们重新组合成一个字符串？此时要用.join()。
'''
print(''.join(l))   # hello world