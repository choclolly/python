import mysql.connector
import redis


class DB:
    def __init__(self, host, port, database, user, passwd):
        self.conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            database=database,
            buffered=True
        )
        self.cur = self.conn.cursor()

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


# 获取redis连接
def get_redis(db=0):
    user_info = {'host': '100.114.66.90', 'password': 'Dayl@%L7r', 'port': 5672,
                 'db': db, 'decode_responses': True}
    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=db, decode_responses=True) #redis连接池
    pool = redis.ConnectionPool(**user_info)  # redis连接池
    r = redis.Redis(connection_pool=pool)
    return r


if __name__ == '__main__':
    # 用户中心库
    with DB(host="uc-mysql-master", port="3306", user="tea_uc", passwd="!xkpLr6aW2Z~XW!B8.k~",
            database="tea_uc") as db_user:
        # 尊享增值服务id
        # vasId = 'e0316f1b70784d26924e09bc18a92fb8'
        vasId = 'af650e3e0a024bed8384ec419f93d1f0'
        # 尊享有效且已注销的,申请注销时间在购买尊享之前的,恢复会员身份
        sql = 'SELECT user_id,mobile,source FROM uc_user WHERE user_id IN (SELECT t1.user_id FROM uc_vas_record AS t1,(SELECT * FROM uc_user_cancel_record WHERE verify_state = 3) AS t2 ' \
              'WHERE t1.added_service_id = \'%s\' AND t1.invalid = 0 AND t1.end_time > REPLACE(unix_timestamp(current_timestamp(3)),\'.\',\'\') AND t1.user_id = t2.user_id ' \
              'AND t1.create_time > t2.create_time ORDER BY t1.end_time DESC)' % vasId
        db_user.execute(sql, None)
        result = db_user.fetchall()
        if len(result) != 0:
            print("###################start###################")
            for x in result:
                user_id = x[0]
                mobile = x[1]
                source = x[2]

                # 账号恢复
                sql_1 = 'update uc_user_cancel_record set verify_state = 2,verify_desc = \'账号恢复\' where user_id = %s and verify_state = 3' % user_id
                sql_2 = 'delete from uc_user_cancel_record_log where user_id = %s' % user_id
                sql_3 = 'update uc_user set if_del = 1 where user_id = %s' % user_id
                sql_4 = 'update uc_account set if_del = 1 where user_id = %s' % user_id
                sql_5 = 'update uc_user_real_name_authentication set if_del = 1 where user_id = %s' % user_id
                db_user.execute(sql_1, None)
                db_user.execute(sql_2, None)
                i = int(str(user_id)) % 2
                if i == 0:
                    with DB(host="shard-uc-1-master", port="3306", user="tea_uc_1", passwd="EpeL4fQO+]sPJDvt",
                            database="tea_uc_1") as db_user_0:
                        db_user_0.execute(sql_3, None)
                        db_user_0.execute(sql_4, None)
                        db_user_0.execute(sql_5, None)
                if i == 1:
                    with DB(host="shard-uc-2-master", port="3306", user="ebs_manage", passwd="Xu~eQa(,.EBE]0ud8Spz",
                            database="tea_uc_2") as db_user_1:
                        db_user_1.execute(sql_3, None)
                        db_user_1.execute(sql_4, None)
                        db_user_1.execute(sql_5, None)
                # redis
                r = get_redis(5)
                r.sadd('mobile_set_key', mobile)
                r.sadd('user_id_set_key', user_id)
                r.sadd('userid_mobile_set_key', str(user_id) + "__" + mobile)
                # 需要逻辑删除的数据
                sql = 'SELECT user_id,if_del FROM uc_user where mobile = %s' % mobile
                db_user.execute(sql, None)
                result = db_user.fetchall()
                for y in result:
                    other_user_id = y[0]
                    if other_user_id != user_id:
                        sql_1 = 'update uc_user set if_del = 2 where user_id = %s' % other_user_id
                        sql_2 = 'update uc_user_real_name_authentication SET if_del = 2 WHERE user_id = %s' % other_user_id
                        sql_3 = 'update uc_account SET if_del = 2 WHERE user_id = %s' % other_user_id
                        sql_4 = 'delete from uc_user_online WHERE user_id = %s' % other_user_id
                        sql_5 = 'update uc_user_real_name_authentication set if_del = 2 where user_id =  %s;' % other_user_id
                        i = int(str(other_user_id)) % 2
                        if i == 0:
                            with DB(host="shard-uc-1-master", port="3306", user="tea_uc_1", passwd="EpeL4fQO+]sPJDvt",
                                    database="tea_uc_1") as db_user_0:
                                db_user_0.execute(sql_1, None)
                                db_user_0.execute(sql_2, None)
                                db_user_0.execute(sql_3, None)
                                db_user_0.execute(sql_4, None)
                                db_user_0.execute(sql_5, None)
                        if i == 1:
                            with DB(host="shard-uc-2-master", port="3306", user="ebs_manage",
                                    passwd="Xu~eQa(,.EBE]0ud8Spz",
                                    database="tea_uc_2") as db_user_1:
                                db_user_1.execute(sql_1, None)
                                db_user_1.execute(sql_2, None)
                                db_user_1.execute(sql_3, None)
                                db_user_1.execute(sql_4, None)
                                db_user_1.execute(sql_5, None)
                        r = get_redis(5)
                        r.srem('user_id_set_key', other_user_id)
                        r.srem('userid_mobile_set_key', str(other_user_id) + "__" + mobile)
                        r.hdel('token_hash_key', str(other_user_id) + "__" + str(source))
                print('用户userId:{},手机号:{},会员身份恢复'.format(user_id, mobile))
            print("###################end#####################")
        else:
            print("无符合条件的数据")
