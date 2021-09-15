# -*- coding:gbk -*-
'''
UUID����
	UUID��128λ��ȫ��Ψһ��ʶ����ͨ����32�ֽڵ��ַ�����ʾ�������Ա�֤ʱ��Ϳռ��Ψһ�ԣ�Ҳ��ΪGUID��ȫ��Ϊ��UUID ���� Universally Unique IDentifier��Python �н� UUID��
	��ͨ��MAC��ַ��ʱ����������ռ䡢�������α���������֤����ID��Ψһ�ԡ�
UUID��Ҫ������㷨��Ҳ�������ַ�����ʵ�֡�
	uuid1()��������ʱ�����
		��MAC��ַ����ǰʱ�������������ɡ����Ա�֤ȫ��Χ�ڵ�Ψһ�ԣ���MAC��ʹ��ͬʱ������ȫ�����⣬�������п���ʹ��IP������MAC��
	uuid2()�������ڷֲ�ʽ���㻷��DCE(Python��û���������)��
		�㷨��uuid1��ͬ����ͬ���ǰ�ʱ�����ǰ4λ�û�ΪPOSIX��UID��ʵ���к����õ��÷�����
	uuid3()�����������ֵ�MD5ɢ��ֵ��
		ͨ���������ֺ������ռ��MD5ɢ��ֵ�õ�����֤��ͬһ�����ռ��в�ͬ���ֵ�Ψһ�ԣ��Ͳ�ͬ�����ռ��Ψһ�ԣ���ͬһ�����ռ��ͬһ����������ͬ��uuid��
	uuid4()���������������
		��α������õ�����һ�����ظ����ʣ��ø��ʿ��Լ��������
	uuid5()�����������ֵ�SHA-1ɢ��ֵ��
		�㷨��uuid3��ͬ����ͬ����ʹ�� Secure Hash Algorithm 1 �㷨��
'''

import uuid

def uuid_all():
    print('uuid1() ���ɻ��ڼ��������ID�͵�ǰʱ���UUID:{}'.format(uuid.uuid1()))
    print('uuid3() ���������ռ��һ���ַ���MD5���ܵ�UUID:{}'.format(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')))
    print('uuid4() �������һ��UUID:{}'.format(uuid.uuid4()))
    print('uuid5() ���������ռ��һ���ַ���SHA-1���ܵ�UUID:{}'.format(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')))
    print('other   ����ʮ�������ַ�����UUID,ת����ʮ�����Ƶ�UUID�����ַ�:{}'.format(str(uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}'))))

uuid_all()

'''
UUID�м��'-'�Ǹ��Ƚ���ֵ��ַ�����ôӦ��ȥ����
'''

def uuid_format():
    uid = uuid.uuid1()
    print(uid)	# cd67334e-3dd8-11eb-8386-54e1ad2e3c5a
    # ��ʽһ
    print(str(uid).replace('-', ''))	# cd67334e3dd811eb838654e1ad2e3c5a
    # ��ʽ��
    print(''.join(str(uid).split('-'))) # cd67334e3dd811eb838654e1ad2e3c5a


uuid_format()