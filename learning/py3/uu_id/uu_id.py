# -*- coding:gbk -*-
'''
UUID介绍
	UUID是128位的全局唯一标识符，通常由32字节的字符串表示。它可以保证时间和空间的唯一性，也称为GUID，全称为：UUID —— Universally Unique IDentifier，Python 中叫 UUID。
	它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
UUID主要有五个算法，也就是五种方法来实现。
	uuid1()——基于时间戳。
		由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
	uuid2()——基于分布式计算环境DCE(Python中没有这个函数)。
		算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。实际中很少用到该方法。
	uuid3()——基于名字的MD5散列值。
		通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
	uuid4()——基于随机数。
		由伪随机数得到，有一定的重复概率，该概率可以计算出来。
	uuid5()——基于名字的SHA-1散列值。
		算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法。
'''

import uuid

def uuid_all():
    print('uuid1() 生成基于计算机主机ID和当前时间的UUID:{}'.format(uuid.uuid1()))
    print('uuid3() 基于命名空间和一个字符的MD5加密的UUID:{}'.format(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')))
    print('uuid4() 随机生成一个UUID:{}'.format(uuid.uuid4()))
    print('uuid5() 基于命名空间和一个字符的SHA-1加密的UUID:{}'.format(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')))
    print('other   根据十六进制字符生成UUID,转换成十六进制的UUID表现字符:{}'.format(str(uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}'))))

uuid_all()

'''
UUID中间的'-'是个比较奇怪的字符，那么应该去掉它
'''

def uuid_format():
    uid = uuid.uuid1()
    print(uid)	# cd67334e-3dd8-11eb-8386-54e1ad2e3c5a
    # 方式一
    print(str(uid).replace('-', ''))	# cd67334e3dd811eb838654e1ad2e3c5a
    # 方式二
    print(''.join(str(uid).split('-'))) # cd67334e3dd811eb838654e1ad2e3c5a


uuid_format()