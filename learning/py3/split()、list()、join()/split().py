'''
将句子分成单词
'''

A = 'Mary had a little rabbit'
print(A.split())  # ['Mary', 'had', 'a', 'little', 'rabbit']

'''
空白字符包括空格’ ‘，换行符’\ n’和制表符’\ t’等。.split()分隔这些字符的任何组合序列：

    color    green 
	idea


'''
B = 'color    green \n\tidea\n'
print(B)

print(B.split())  # ['color', 'green', 'idea']


'''
.split（‘x’）可用于在特定子字符串’x’上拆分字符串。如果没有指定’x’，split ()只是在所有空白符上分割
'''
print(A.split('a')) # ['M', 'ry h', 'd ', ' little r', 'bbit']


D= 'Hello mother,\nHello father.'
print(D)    # Hello mother,
            # Hello father.

print(D.split())    # ['Hello', 'mother,', 'Hello', 'father.']
print(D.split('\n')) # ['Hello mother,', 'Hello father.']

