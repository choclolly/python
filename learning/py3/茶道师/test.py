import re, time, os, sys

'''
过滤字符串前后中间空格
'''
s = ' 女 '
print(s)
print(re.sub(' ', '', s))

s = ' 女  人 '
print(s)
print(re.sub(' ', '', s))

'''
strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。

注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
'''
s = ' 女  人 '
print(s.strip())

# f 转str取小数点前面数值
f = 13609552655.0
print(str(f).split('.')[0])


# 字符串日期转时间戳
def one():
    # 字符类型的时间
    date_1 = '2021.12.31'
    # 转为时间数组
    time_array = time.strptime(date_1, '%Y.%m.%d')
    # time.struct_time(tm_year=2020, tm_mon=12, tm_mday=14, tm_hour=15, tm_min=22, tm_sec=22, tm_wday=0, tm_yday=349,tm_isdst=-1)
    print(time_array)
    # timeArray可以调用tm_year等
    print(time_array.tm_year)  # 2020
    # 转为时间戳, 十位数时间戳
    time_stamp = int(time.mktime(time_array))
    print(time_stamp)  # 1607930542
    # 转为时间戳, 十三位数时间戳
    time_stamp = int(time.mktime(time_array)) * 1000
    print(time_stamp)  # 1607930542


one()

'''
Python中字符串String去除出换行符(n,r)和空格的问题
    https://blog.csdn.net/jerrygaoling/article/details/81051447
'''
address = '广东省汕头市金砂路103号星光华庭105号铺大益茶\n' \
          '王立浩 13502633603'
print(address)
address = re.sub(' ', '', address)
print(address)
address = address.replace('\n', '').replace('\r', '')
print(address)

s2 = '哈哈'
print(str(s2))

'''
Python3 获取当前文件名
    
'''
path2 = '茶道师数据/2028-2021.8初阶汇总.xlsx'
print(path2.index('.xlsx'))
print(path2)
print(sys.argv[0])
print(os.path.dirname(path2))
print(os.path.split(path2))
print(os.path.split(path2)[-1])
print(os.path.split(path2)[-1].split(".")[0])
print(os.path.split(path2)[-1].split(".")[0])

print(os.path.split(path2)[-1][:-5])

'''
字符串截取


str = '0123456789'
print str[0:3] #截取第一位到第三位的字符
print str[:] #截取字符串的全部字符
print str[6:] #截取第七个字符到结尾
print str[:-3] #截取从头开始到倒数第三个字符之前
print str[2] #截取第三个字符
print str[-1] #截取倒数第一个字符
print str[::-1] #创造一个与原字符串顺序相反的字符串
print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
print str[-3:] #截取倒数第三位到结尾
print str[:-5:-3] #逆序截取，具体啥意思没搞明白？


'''

test_dict = {}

test_dict[0] = 1
test_dict[0] = 1

print(len(test_dict))
print(test_dict)

i = 0
test_dict_1 = {}
print(type)



print('-------------------------------')
id_num_tea_c_master_insert_sql_dict = {}
keys = id_num_tea_c_master_insert_sql_dict.keys()
s = 'd'
if s not in keys:
    print('不存在')
    id_num_tea_c_master_insert_sql_dict[s] = 4

for k,v in id_num_tea_c_master_insert_sql_dict.items():
    print(k)
    print(id_num_tea_c_master_insert_sql_dict[k])
print('-------------------------------')
id_num_tea_c_master_insert_sql_dict = {'a': 1, 'b': 2, 'c': 3}
id_num_tea_c_master_insert_sql_dict_copy = id_num_tea_c_master_insert_sql_dict.copy()
# for k,v in id_num_tea_c_master_insert_sql_dict.items():
#     if k != 'd':
#         id_num_tea_c_master_insert_sql_dict_copy['d'] = 4
#
# for k,v in id_num_tea_c_master_insert_sql_dict_copy.items():
#     print(k)
#     print(id_num_tea_c_master_insert_sql_dict_copy[k])
keys = id_num_tea_c_master_insert_sql_dict.keys()
print(type(keys))
print(keys)


s = 'd'
if s in keys:
    print('已存在')
else:
    print('不存在')
    id_num_tea_c_master_insert_sql_dict[s] = 4

for k,v in id_num_tea_c_master_insert_sql_dict.items():
    print(k)
    print(id_num_tea_c_master_insert_sql_dict[k])