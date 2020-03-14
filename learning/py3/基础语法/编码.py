# -*- coding: utf-8 -*-
"""
1,
默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串，也就是：
# -*- coding: utf-8 -*-
并且这一行必须放在#！行的下面，如果没有#！行，则必须放在第一行。

2,
当然你也可以为源码文件指定不同的编码,写在python文件开头：方式如下
# -*- coding: cp-1252 -*-
上述定义允许在源文件中使用 Windows-1252 字符集中的字符编码，对应适合语言为保加利亚语、白罗斯语、马其顿语、俄语、塞尔维亚语。
"""

A = "哈哈" + " hello word"
print(A)
print(type(A))  # <class 'str'>  所有字符串都是 unicode 字符串，所以带u和不带u是一样的
print(type(A.encode("utf-8")))  # <class 'bytes'>
B = 3
print(type(B))  # <class 'int'>
"""
1,
    python中 r'', b'', u'', f'' 的含义
        u/U:表示unicode字符串
            不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。
            一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；
            但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。
                建议所有编码方式采用utf8
2,
    在python中unicode中的type为str,gbk/utf-8的类型为byte
3,  
    python之中utf-8,unicode,gbk之间转换
        unicode与GBK没有相对应的算法可以直接转换
            unicode，utf-8，gbk之间的转换,需要先转为unicode
4,
    utf-8一个中文占3个字节，gbk两个字节
5,
    字符和字节是两个不同的术语，
        在unicode中一个字符就是两个字节，如’人’一个字符占两个字节。
        对于python中len()函数,len(u’中国’)和len(‘hi’)一样长度值都为2，这里长度是指字符长度
6,
    ASCII码跟Unicode没有本质的区别。只不过Unicode表示范围比ASCII大
7,
    在简体中文Windows操作系统中，ANSI 编码代表 GBK 编码
8,
    unicode和utf-8的区别
        unicode是charset(字符集)，
            包括GBK,GBK2312也是字符集
        utf-8是encoding(编码)：
            多字节编码，对英文使用8位(1个字节)，对中文使用24位(3个字节)编码
        unicode是一个字符集，utf-8是在这个字符集基础上的一种具体的编码方案，为了更好的存储和传输，还有utf-16，utf-32等
"""
# 所有字符串都是 unicode 字符串，所以带u和不带u是一样的
s = u'小明'
s1 = '小明'
print(s)
# 在python中unicode中的type为str
print(type(s))      # <class 'str'>
print(type(s1))     # <class 'str'>
# 编码为utf-8
# 在python中gbk/utf-8的类型为byte
s_utf = s.encode('utf-8')
print(type(s_utf))  # <class 'bytes'>
print(s_utf)        # b'\xe5\xb0\x8f\xe6\x98\x8e'
# 变为为gbk,先解码为unicode，再编码
s_gbk = s_utf.decode('utf-8').encode('gbk')
print(type(s_gbk))  # <class 'bytes'>
print(s_gbk)        # b'\xd0\xa1\xc3\xf7'
