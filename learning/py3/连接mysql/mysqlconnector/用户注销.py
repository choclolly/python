import mysql.connector
import redis
import time
import uuid

# 用户中心库
user = mysql.connector.connect(
    host="172.17.186.153",
    port="3306",
    user="test_tea_uc",
    passwd="pw@kbm9p0Yl@!t3bZD",
    database="test_tea_uc"
)
user_cursor = user.cursor()

# 用户分片 偶
user_0 = mysql.connector.connect(
    host="172.17.186.153",
    port="3306",
    user="test_tea_uc_0",
    passwd="L~+SJ*F^kon[t+10l6",
    database="test_tea_uc_0"
)
user_cursor_0 = user_0.cursor()

# 用户分片 奇
user_1 = mysql.connector.connect(
    host="172.17.186.153",
    port="3306",
    user="test_tea_uc_1",
    passwd="]J1tFUzKh8oI#LU9ih",
    database="test_tea_uc_1"
)
user_cursor_1 = user_1.cursor()

# 订单中心库
order = mysql.connector.connect(
    host="172.17.186.153",
    port="3306",
    user="tea_admin_mall",
    passwd="euRyC7S1Il75AiI",
    database="tea_admin_mall"
)
order_cursor = order.cursor()

# 订单分片0
order_0 = mysql.connector.connect(
    host="172.17.186.153",
    port="3307",
    user="mall_order_1",
    passwd="QwbchBKoizep",
    database="mall_order_1"
)
order_cursor_0 = order_0.cursor()

# 订单分片1
order_1 = mysql.connector.connect(
    host="172.17.186.154",
    port="3308",
    user="mall_order_2",
    passwd="gozap123",
    database="mall_order_2"
)
order_cursor_1 = order_1.cursor()

# 订单分片2
# order_2 = mysql.connector.connect(
#     host="172.17.186.153",
#     port="3306",
#     user="tea_admin_mall",
#     passwd="euRyC7S1Il75AiI",
#     database="tea_admin_mall"
# )
# order_cursor_2 = order_2.cursor()

# redis连接池
pool = redis.ConnectionPool(
    host="172.17.186.153",
    port=6381,
    password="aB(D2f9",
    db='5',
    max_connections=1024)
conn = redis.Redis(connection_pool=pool)

# 获取所有申请注销的用户[user_id,mobile]
sql = "SELECT user_id,mobile from uc_user_cancel_record where verify_state = %s"
na = (1,)
user_cursor.execute(sql, na)
result = user_cursor.fetchall()
# print(type(result))   <class 'list'>

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
# 操作记录
s = ''
if len(result) == 0:
    print("无注销申请")
else:
    for x in result:
        user_id = x[0]
        mobile = x[1]
        # 校验最近30天内,用户是否有更改登录密码以及认证手机号的操作
        sql = "SELECT * from uc_user_modify_phone_log where FROM_UNIXTIME(round(create_time / 1000,0)) BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND " \
              "user_id = %s;"
        uc_user_cancel_record_sql = "UPDATE uc_user_cancel_record SET verify_state = 2 where user_id = %s"
        na = (user_id,)
        user_cursor.execute(sql, na)
        # print(type(result))   <class 'tuple'>
        result = user_cursor.fetchall()
        if len(result) > 0:
            print("最近30天内,用户有更改登录密码以及认证手机号的操作,user_id:{},mobile:{}".format(user_id, mobile))
            l_modify_phone.append(user_id)
            # 注销审核不通过
            user_cursor.execute(uc_user_cancel_record_sql, na)
            user.commit()
            continue
        # 校验大益卡预存款余额是否为0
        sql = "SELECT amount from uc_account where user_id = %s;"
        na = (user_id,)
        user_cursor.execute(sql, na)
        result = user_cursor.fetchone()
        if result != 0 and result[0] > 0:
            print("大益卡预存款余额不为0,user_id:{},mobile:{},amount:{}".format(user_id, mobile, result[0]))
            d_balance = {'userId': user_id, 'mobile': mobile, 'amount': result[0]}
            l_balance.append(d_balance)
            # 注销审核不通过
            user_cursor.execute(uc_user_cancel_record_sql, na)
            user.commit()
            continue
        # 校验是否有未完成的订单
        sql = "SELECT order_no FROM sdb_b2c_order where pay_state = 1 " \
              "AND (receive_state = 0 or " \
              "(receive_state = 1 AND receive_time IS NOT NULL AND DATE_ADD(FROM_UNIXTIME(round(receive_time / 1000,0)), INTERVAL 10 DAY) > NOW())) " \
              "AND member_id = %s;"
              # "AND order_type = 1 AND member_id = %s;"

        na = (user_id,)
        order_cursor.execute(sql, na)
        result = order_cursor.fetchall()
        # print(type(result))
        if len(result) > 0:
            for y in result:
                print("有未完成的订单,user_id:{},mobile:{},orderNo:{}".format(user_id, mobile, y[0].decode('utf-8')))
                d_no_finish_order = {'userId': user_id, 'mobile': mobile, 'orderNo': y[0].decode('utf-8')}
                l_no_finish_order.append(d_no_finish_order)
                # 注销审核不通过
                user_cursor.execute(uc_user_cancel_record_sql, na)
                user.commit()
            continue
        # 校验是否有未提取存茶订单
        # sql = "SELECT order_no FROM sdb_b2c_order_savetea WHERE member_id = %s AND (biz_no NOT IN (SELECT id FROM sdb_b2c_order_savetea) OR (biz_no IN (SELECT id FROM sdb_b2c_order_savetea) AND receive_state = 0))"
        sql = "SELECT order_no FROM sdb_b2c_order_savetea WHERE member_id = %s AND biz_no IN (SELECT id FROM sdb_b2c_order_savetea) AND receive_state = 0"
        na = (user_id,)
        order_cursor.execute(sql, na)
        result = order_cursor.fetchall()
        if len(result) > 0:
            for y in result:
                print("有未提取存茶订单,user_id:{},mobile:{},orderNo:{}".format(user_id, mobile, y[0].decode('utf-8')))
                d_no_finish_order_save_tea = {'userId': user_id, 'mobile': mobile, 'orderNo': y[0].decode('utf-8')}
                l_no_finish_order_save_tea.append(d_no_finish_order_save_tea)
                # 注销审核不通过
                user_cursor.execute(uc_user_cancel_record_sql, na)
                user.commit()
            continue
        # # 校验是否有未完成的宝盒订单
        # sql = "SELECT order_no from sdb_b2c_order where order_type = 2 AND member_id = %s;"
        # na = (user_id,)
        # order_cursor.execute(sql, na)
        # result = order_cursor.fetchall()
        # if len(result) > 0:
        #     for y in result:
        #         print("有未提取存茶订单,user_id:{},mobile:{},orderNo:{}".format(user_id, mobile, str(y[0])))
        #         d_no_finish_order_box = {'userId': user_id, 'mobile': mobile, 'orderNo': str(y[0])}
        #         l_no_finish_order_box.append(d_no_finish_order_box)
        #     continue
        tuple_user_id_and_mobile = (user_id, mobile)
        l_accord_with_condition_user_id.append(tuple_user_id_and_mobile)
for x in l_accord_with_condition_user_id:
    print("符合注销条件的用户user_id:{}".format(x[0]))
    user_id = x[0]
    mobile = x[1]
    # 获取user_num
    uc_user_sql = "SELECT user_num from uc_user where user_id = %s AND if_del = %s"
    na = (user_id, 1)
    user_cursor.execute(uc_user_sql, na)
    result = user_cursor.fetchone()
    userNum = result[0]
    uc_user_cancel_record_sql = "UPDATE uc_user_cancel_record SET verify_state = 3 where user_id = %s and verify_state = 1"
    na = (user_id,)
    # 注销审核通过
    user_cursor.execute(uc_user_cancel_record_sql, na)
    user.commit()
    # user
    # 校验是否实名
    uc_user_real_name_authenticationsql = "SELECT * FROM uc_user_real_name_authentication WHERE verify = 2 AND user_id = %s AND if_del = %s;"
    na = (user_id, 1)
    user_cursor.execute(uc_user_real_name_authenticationsql, na)
    result = user_cursor.fetchone()
    if result is not None:
        sql = "UPDATE uc_user_real_name_authentication SET if_del = 2 WHERE user_id = %s"
        na = (user_id,)
        if int(str(user_id)[-1]) % 2 == 0:
            user_cursor_0.execute(sql, na)
            user_0.commit()
            s = s + sql
        else:
            user_cursor_1.execute(sql, na)
            user_1.commit()
    uc_user_sql = "UPDATE uc_user SET if_del = 2 WHERE user_id = %s"
    uc_account_sql = "UPDATE uc_account SET if_del = 2 WHERE user_id = %s"
    uc_user_online_sql = "DELETE FROM uc_user_online WHERE user_id = %s"
    na = (user_id,)
    if int(str(user_id)[-1]) % 2 == 0:
        user_cursor_0.execute(uc_user_sql, na)
        user_cursor_0.execute(uc_account_sql, na)
        user_cursor_0.execute(uc_user_online_sql, na)
        user_0.commit()
    else:
        user_cursor_1.execute(uc_user_sql, na)
        user_cursor_1.execute(uc_account_sql, na)
        user_cursor_1.execute(uc_user_online_sql, na)
        user_1.commit()
    if len(s) > 0:
        s = s + ";\n" + uc_user_sql + ";\n" + uc_account_sql + ";\n" + uc_user_online_sql
    else:
        s = s + uc_user_sql + ";\n" + uc_account_sql + ";\n" + uc_user_online_sql + ";\n"
    # redis 删除缓存
    sql = "SELECT name,source from uc_user where user_id = %s"
    na = (user_id,)
    user_cursor.execute(sql, na)
    result = user_cursor.fetchone()
    if result != 0:
        name = result[0]
        mobile_set_key_value = mobile
        user_id_set_key_value = user_id
        userid_mobile_set_key_value = str(user_id) + "__" + str(mobile)
        token_hash_key_value = str(user_id) + "__" + str(result[1])
        conn.srem('mobile_set_key', mobile_set_key_value)
        conn.srem('user_id_set_key', user_id_set_key_value)
        conn.srem('userid_mobile_set_key', userid_mobile_set_key_value)
        conn.hdel('token_hash_key', token_hash_key_value)
        s = s + uc_user_cancel_record_sql + ";\n" + 'SREM mobile_set_key ' + str(
            mobile_set_key_value) + ";\n" + 'SREM user_id_set_key ' + str(
            user_id_set_key_value) + ";\n" + 'SREM userid_mobile_set_key ' + str(
            userid_mobile_set_key_value) + ";\n" + 'HDEL token_hash_key ' + str(token_hash_key_value) + ";\n"
    # order [订单,存茶单]
    sdb_b2c_order_query_sql = "SELECT * FROM sdb_b2c_order where member_id = %s"
    sdb_b2c_order_savetea_query_sql = "SELECT * FROM sdb_b2c_order_savetea where member_id = %s"
    sdb_b2c_order_sql = "UPDATE sdb_b2c_order set state = 0, remark = '用户注销删除订单信息' where member_id = %s"
    sdb_b2c_order_savetea_sql = "UPDATE sdb_b2c_order_savetea set state = 0, remark = '用户注销删除存取茶单信息' where member_id = %s"
    na = (user_id,)
    # i = int(str(userNum)) % 3
    # if i == 0:
    #     order_cursor_0.execute(sdb_b2c_order_query_sql, na)
    #     result = order_cursor_0.fetchall()
    #     order_cursor_0.execute(sdb_b2c_order_savetea_query_sql, na)
    #     result2 = order_cursor_0.fetchall()
    #     if len(result) != 0:
    #         order_cursor_0.execute(sdb_b2c_order_sql, na)
    #         order_0.commit()
    #         s = s + sdb_b2c_order_sql + ";\n"
    #     if len(result2) != 0:
    #         order_cursor_0.execute(sdb_b2c_order_savetea_sql, na)
    #         order_0.commit()
    #         s = s + sdb_b2c_order_savetea_sql + ";\n"
    # elif i == 1:
    #     order_cursor_1.execute(sdb_b2c_order_query_sql, na)
    #     result = order_cursor_1.fetchall()
    #     order_cursor_1.execute(sdb_b2c_order_savetea_query_sql, na)
    #     result2 = order_cursor_1.fetchall()
    #     if len(result) != 0:
    #         order_cursor_1.execute(sdb_b2c_order_sql, na)
    #         order_1.commit()
    #         s = s + sdb_b2c_order_sql + ";\n"
    #     if len(result2) != 0:
    #         order_cursor_1.execute(sdb_b2c_order_savetea_sql, na)
    #         order_1.commit()
    #         s = s + sdb_b2c_order_savetea_sql + ";\n"
    # # elif i == 1:
    # #     order_cursor_2.execute(sdb_b2c_order_query_sql, na)
    # #     result = order_cursor_2.fetchall()
    # #     order_cursor_2.execute(sdb_b2c_order_savetea_query_sql, na)
    # #     result2 = order_cursor_2.fetchall()
    # #     if len(result) != 0:
    # #         order_cursor_2.execute(sdb_b2c_order_sql, na)
    # #         order_2.commit()
    # #     if len(result2) != 0:
    # #         order_cursor_2.execute(sdb_b2c_order_savetea_sql, na)
    # #         order_2.commit()

    i = int(str(userNum)) % 2
    if i == 0:
        order_cursor_1.execute(sdb_b2c_order_query_sql, na)
        result = order_cursor_1.fetchall()
        order_cursor_1.execute(sdb_b2c_order_savetea_query_sql, na)
        result2 = order_cursor_1.fetchall()
        if len(result) != 0:
            order_cursor_1.execute(sdb_b2c_order_sql, na)
            order_1.commit()
            s = s + sdb_b2c_order_sql + ";\n"
        if len(result2) != 0:
            order_cursor_1.execute(sdb_b2c_order_savetea_sql, na)
            order_1.commit()
            s = s + sdb_b2c_order_savetea_sql + ";\n"
    else:
        order_cursor_0.execute(sdb_b2c_order_query_sql, na)
        result = order_cursor_0.fetchall()
        order_cursor_0.execute(sdb_b2c_order_savetea_query_sql, na)
        result2 = order_cursor_0.fetchall()
        if len(result) != 0:
            order_cursor_0.execute(sdb_b2c_order_sql, na)
            order_0.commit()
            s = s + sdb_b2c_order_sql + ";\n"
        if len(result2) != 0:
            order_cursor_0.execute(sdb_b2c_order_savetea_sql, na)
            order_0.commit()
            s = s + sdb_b2c_order_savetea_sql + ";\n"

    # elif i == 1:
    #     order_cursor_2.execute(sdb_b2c_order_query_sql, na)
    #     result = order_cursor_2.fetchall()
    #     order_cursor_2.execute(sdb_b2c_order_savetea_query_sql, na)
    #     result2 = order_cursor_2.fetchall()
    #     if len(result) != 0:
    #         order_cursor_2.execute(sdb_b2c_order_sql, na)
    #         order_2.commit()
    #     if len(result2) != 0:
    #         order_cursor_2.execute(sdb_b2c_order_savetea_sql, na)
    #         order_2.commit()
    s = s
    s = s.replace('%s', str(user_id))
    # 用户注销操作记录
    # print('符合注销条件的用户注销操作记录:\n' + s)
    ID = str(uuid.uuid1()).replace('-', '')
    millis_time = int(round(time.time() * 1000))
    sql = "INSERT INTO uc_user_cancel_record_log(`id`, `user_id`, `mobile`, `name`, `operation`, `type`, `create_time`) VALUES " \
          "(%s, %s, %s, %s, %s, %s, %s);"
    na = (ID, user_id, mobile, name, s, '1', millis_time)
    user_cursor.execute(sql, na)
    user.commit()
    print('用户user_id:{},mobile:{} 注销完毕'.format(x[0], x[1]))
user_cursor.close()
user.close()
user_cursor_0.close()
user_0.close()
user_cursor_1.close()
user_1.close()
user_cursor.close()
user.close()
order_cursor.close()
order.close()
order_cursor_0.close()
order_0.close()
order_cursor_1.close()
order_1.close()
# order_cursor_2.close()
# order_2.close()
