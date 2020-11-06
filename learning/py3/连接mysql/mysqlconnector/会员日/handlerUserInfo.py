#!/usr/bin/env python
# coding: utf-8

import redisUtils
import time
import json
from DbManage import DbManage

# 测试
# print('测试')
# exit(2)

current_time = int(time.time() * 1000)  # 当前时间
MEMBER_INFO_PERFIX = 'seckill:user_info'  # 用户信息redis key
# 用户基础信息key
user_id = 'user_id'
user_mobile = 'mobile'
user_name = 'name'
user_type = 'user_type'
user_num = 'user_num'
query_user_sql = 'SELECT user_id, mobile, NAME as name, TYPE as user_type, user_num FROM uc_user WHERE if_del = 1 AND STATUS = STATUS'
query_user_vas_sql = 'SELECT user_id FROM uc_vas_record WHERE end_time > %d AND STOP = 0 AND invalid = 0 AND added_service_id = %s' % (current_time, 'e0316f1b70784d26924e09bc18a92fb8')

# 查询用户基本信息
with DbManage() as db:
    user_info = db.get_list(query_user_sql)
    user_vas_info = db.get_list(query_user_vas_sql)

user_vas_info = [_user['user_id'] for _user in user_vas_info]

member_info_str = '''
{
    "memberId": "",
    "memberNo": "",
    "memberLevel": "",
    "memberPhone": "",
    "memberName": "",
    "vas": ""
}
'''

member_info = json.loads(member_info_str)
member_dict = {}

for user in user_info:
    memberId = user[user_id]
    memberNo = user[user_num]
    memberPhone = user[user_mobile]
    memberLevel = user[user_type]
    memberName = user[user_name]
    vas = '1' if (memberId in user_vas_info) else '0'
    member_info['memberId'] = str(memberId)
    member_info['memberNo'] = str(memberNo)
    member_info['memberLevel'] = memberLevel
    member_info['memberPhone'] = memberPhone
    member_info['memberName'] = memberName
    member_info['vas'] = vas
    member_dict[memberId] = json.dumps(member_info, ensure_ascii=False)

print(member_dict)
r = redisUtils.get_redis(0)
r.hmset(MEMBER_INFO_PERFIX, member_dict)

print('###############end###############')
