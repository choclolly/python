#!/usr/bin/env python
# coding: utf-8

import uuid

# ���
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
		# ����
		begin_index = x * 4	# <class 'int'>
		end_index =  x * 4 + 4	# <class 'int'>
		# ��ȡ
		s = id[begin_index:end_index]
		# print(s)
		# 16�����ַ���ת����
		num = int(s,16)
		# print(num)
		# ȡģ62(ʮ�����Ʊ�ʾΪ314(14��E))�������Ϊ���������ȡ���ַ�
		c = list_code[num % 0x3E]
		# print(c)
		# ����8λ�ַ�
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