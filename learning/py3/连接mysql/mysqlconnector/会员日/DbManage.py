#!/usr/bin/env python
# coding: utf-8

import pymysql
from DBUtils.PooledDB import PooledDB


class DbManage(object):

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.doConnect()

    # 连接
    def doConnect(self):
        # info = {'host':'127.0.0.1', 'port': 3306, 'user':'root','passwd':'root', 'db':'test1', 'charset':'utf8'}
        pool = PooledDB(pymysql, 5, host='uc-mysql-master', user='tea_uc', passwd='!xkpLr6aW2Z~XW!B8.k~', db='tea_uc',
                        port=3306, setsession=[
                'SET AUTOCOMMIT = 1'])  # 5为连接池里的最少连接数，setsession=['SET AUTOCOMMIT = 1']是用来设置线程池是否打开自动更新的配置，0为False，1为True
        self.conn = pool.connection()
        # 以字典返回结果,可以通过key来获取数据
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 进入执行
    def __enter__(self):
        return self

    # 退出执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # 断开连接
    def close(self):
        self.conn.commit()
        self.conn.close()
        self.cursor.close()

    # 获取单个结果
    def get_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    # 获取多个结果集
    def get_list(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchall()

    # 执行插入或修改操作，返回插入的结果id
    def execute(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.lastrowid

    # 批量执行插入获取修改操作
    def execute_many(self, sql, args=None):
        self.cursor.executemany(sql, args)

    # 查询记录的数量
    def count(self, sql, args=None):
        return len(self.get_list(sql, args))


if __name__ == '__main__':
    with DbManage() as db:
        print(db.count('select * from users where userName = %s', '李四'))
        # print(db.execute('insert into users (userName,passWord,user_sex,nick_name) VALUES (%s,%s,%s,%s) ', ('李四','qaz123',1,'四爷')))
        # pass
