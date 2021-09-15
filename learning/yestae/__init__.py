import re

'''
       去除特殊字符
              参考：https://www.jb51.net/article/180132.htm
'''

'''
去除数字，特殊字符，只保留汉字
'''
line = '    1123*#$ 中abc    国()   ' \
       '   啊打发   士大夫'
filter_content = "[a-zA-Z0-9'!#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘'！[\\]^_`{|}~\s]+"
sub = re.sub(filter_content, "", line)
print(sub)  # 中国啊打发士大夫

'''
去除特殊字符，只保留汉子，字母、数字
'''

filter_content = u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])"
sub = re.sub(filter_content, "", line)
print(sub)  # 1123中abc国啊打发士大夫

'''
去除不可见字符
'''
filter_content = '[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a]+'
sub = re.sub(filter_content, "", line)
print(sub)  # 1123*#$ 中abc国()   啊打发   士大夫
