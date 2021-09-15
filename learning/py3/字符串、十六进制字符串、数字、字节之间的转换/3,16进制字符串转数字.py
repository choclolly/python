#!/usr/bin/env python
# coding: utf-8

import uuid

# 码池
list_code = ["a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z"]




def get_code():
	id = ''.join(str(uuid.uuid1()).split('-')) # <class 'str'>
	eight_c = ''
	for x in range(8):
		# 索引
		begin_index = x * 4	# <class 'int'>
		end_index =  x * 4 + 4	# <class 'int'>
		# 截取
		s = id[begin_index:end_index]
		# print(s)
		# 16进制字符串转数字
		num = int(s,16)
		# print(num)
		# 取模62(十六进制表示为314(14即E))，结果作为索引从码池取出字符
		c = list_code[num % 0x3E]
		# print(c)
		# 生成8位字符
		eight_c = eight_c + c
	return eight_c

# c = get_code()
# print(c)

def eight_c_1000w():
	s = set()
	for x in range(1):
		c = get_code()
		s.add(c)
	print(len(s))

for x in range(10):
	eight_c_1000w()