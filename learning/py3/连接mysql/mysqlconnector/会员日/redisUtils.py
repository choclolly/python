#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Redis工具类
import redis


# 获取redis连接
def get_redis(db=0):
    user_info = {'host': '172.17.186.153', 'password': 'aB(D2f9', 'port': 6381,
                 'db': db, 'decode_responses': True}
    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=db, decode_responses=True) #redis连接池
    pool = redis.ConnectionPool(**user_info)  # redis连接池
    r = redis.Redis(connection_pool=pool)
    return r


r = get_redis(9)
r.sadd('user_id_set_key', str('hao_'))
print(r)
