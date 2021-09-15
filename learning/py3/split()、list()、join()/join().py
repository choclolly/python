'''
‘x’.join(y)连接列表y中由’x’分隔的每个元素。
'''
A = 'Mary had a little rabbit'
split = A.split()
print(split)    # ['Mary', 'had', 'a', 'little', 'rabbit']
print(''.join(A))   # Mary had a little rabbit


'''
可以对任何分隔符字符串进行连接。下面，使用’ – ‘和制表符’\ t’。
'''
print('--'.join(split)) # Mary--had--a--little--rabbit

print('\t'.join(split)) # Mary	had	a	little	rabbit


'''
将一个字符列表放回到原始字符串中：
'''
hi = 'hello world'
l = list(hi)
print(l)    # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(''.join(l))   # hello world

'''
题目：将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
'''
print(' '.join('I am a boy'.split()[::-1]))