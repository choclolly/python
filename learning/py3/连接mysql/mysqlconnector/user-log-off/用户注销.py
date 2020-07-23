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
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


# redis连接池
pool = redis.ConnectionPool(
    host="59.110.228.110",
    port=6381,
    password="aB(D2f9",
    db='5',
    max_connections=1024)
conn = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    # 最近30天内,用户有更改登录密码以及认证手机号
    l_modify_phone = []
    # 大益卡账户有余额
    l_balance = []
    # 有未完成订单的
    l_no_finish_order = []
    # 有未提取存茶订单的
    l_no_finish_order_save_tea = []
    # 有未完成的宝盒订单
    l_no_finish_order_box = []
    # 符合注销条件的列表
    l_accord_with_condition_user_id = []
    # 用户中心库
    with DB(host="59.110.228.110",
            port="3306",
            user="test_tea_uc",
            passwd="pw@kbm9p0Yl@!t3bZD",
            database="test_tea_uc") as user:
        print(user)

        sql = "SELECT user_id,mobile from uc_user_cancel_record where verify_state = %s"
        na = (1,)
        user.execute(sql, na)
        result = user.fetchall()
        for x in result:
            user_id = x[0]
            mobile = x[1]
            # 校验最近30天内,用户是否有更改登录密码以及认证手机号的操作
            sql = "SELECT * from uc_user_modify_phone_log where FROM_UNIXTIME(round(create_time / 1000,0)) BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND " \
                  "user_id = %s;"
            uc_user_cancel_record_sql = "UPDATE uc_user_cancel_record SET verify_state = 2 where user_id = %s"
            na = (user_id,)
            user.execute(sql, na)
            # print(type(result))   <class 'tuple'>
            result = user.fetchall()
            if len(result) > 0 is not None:
                print("最近30天内,用户有更改登录密码以及认证手机号的操作,user_id:{},mobile:{}".format(user_id, mobile))
                l_modify_phone.append(user_id)
                # 注销审核不通过
                user.execute(uc_user_cancel_record_sql, na)
                continue
            # 校验大益卡预存款余额是否为0
            sql = "SELECT amount from uc_account where user_id = %s;"
            na = (user_id,)
            user.execute(sql, na)
            result = user.fetchone()
            if result is not None and result[0] > 0:
                print("大益卡预存款余额不为0,user_id:{},mobile:{},amount:{}".format(user_id, mobile, result[0]))
                d_balance = {'userId': user_id, 'mobile': mobile, 'amount': result[0]}
                l_balance.append(d_balance)
                # 注销审核不通过
                user.execute(uc_user_cancel_record_sql, na)
                continue
            # 订单中心库
            with DB(host="59.110.228.110",
                    port="3306",
                    user="tea_admin_mall",
                    passwd="euRyC7S1Il75AiI",
                    database="tea_admin_mall") as order:
                print(order)
                # 校验是否有未完成的订单
                sql = "SELECT order_no FROM sdb_b2c_order where pay_state = 1 " \
                      "AND (receive_state = 0 or " \
                      "(receive_state = 1 AND receive_time IS NOT NULL AND DATE_ADD(FROM_UNIXTIME(round(receive_time / 1000,0)), INTERVAL 10 DAY) > NOW())) " \
                      "AND member_id = %s;"
                na = (user_id,)
                order.execute(sql, na)
                result = order.fetchall()
                # print(type(result))
                if len(result) > 0:
                    for y in result:
                        print("有未完成的订单,user_id:{},mobile:{},orderNo:{}".format(user_id, mobile, str(y[0])))
                        d_no_finish_order = {'userId': user_id, 'mobile': mobile, 'orderNo': str(y[0])}
                        l_no_finish_order.append(d_no_finish_order)
                        # 注销审核不通过
                        user.execute(uc_user_cancel_record_sql, na)
                    continue
                # 校验是否有未提取存茶订单
                sql = "SELECT * FROM sdb_b2c_order_savetea WHERE member_id = %s AND (biz_no NOT IN (SELECT id FROM sdb_b2c_order_savetea) OR (biz_no IN (SELECT id FROM sdb_b2c_order_savetea) AND receive_state = 0))"
                na = (user_id,)
                order.execute(sql, na)
                result = order.fetchall()
                if len(result) > 0:
                    for y in result:
                        print("有未提取存茶订单,user_id:{},mobile:{},orderNo:{}".format(user_id, mobile, str(y[0])))
                        d_no_finish_order_save_tea = {'userId': user_id, 'mobile': mobile, 'orderNo': str(y[0])}
                        l_no_finish_order_save_tea.append(d_no_finish_order_save_tea)
                        # 注销审核不通过
                        user.execute(uc_user_cancel_record_sql, na)
                    continue
            tuple_user_id_and_mobile = (user_id, mobile)
            l_accord_with_condition_user_id.append(tuple_user_id_and_mobile)
    for x in l_accord_with_condition_user_id:
        user_id = x[0]
        mobile = x[1]
        uc_user_cancel_record_sql = "UPDATE uc_user_cancel_record SET verify_state = 3 where user_id = %s"
        na = (user_id,)
        # 注销审核通过
        user.execute(uc_user_cancel_record_sql, na)
        # redis 删除缓存
        sql = "SELECT source from uc_user where user_id = %s"
        na = (user_id,)
        user.execute(sql, na)
        result = user.fetchone()
        if result is not None:
            mobile_set_key_value = mobile
            user_id_set_key_value = user_id
            userid_mobile_set_key_value = str(user_id) + "__" + str(mobile)
            token_hash_key_value = str(user_id) + "__" + str(result[0])
            conn.srem('mobile_set_key', mobile_set_key_value)
            conn.srem('user_id_set_key', user_id_set_key_value)
            conn.srem('userid_mobile_set_key', userid_mobile_set_key_value)
            conn.hdel('token_hash_key', token_hash_key_value)
        # user
        # 校验是否实名
        uc_user_real_name_authenticationsql = "SELECT * FROM uc_user_real_name_authentication WHERE verify = 2 AND user_id = %s AND if_del = %s;"
        na = (user_id, 1)
        user.execute(uc_user_real_name_authenticationsql, na)
        result = user.fetchone()
