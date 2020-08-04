import mysql.connector
import time
import datetime
import csv


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


def counter():
    i = 0

    def f(n):
        nonlocal i
        i += n
        return i

    return f


header = ['用户userId', '订单编号order_no', '用户编号是user_num', '订单交易完成返券amount']
count = counter()
if __name__ == '__main__':
    # 受益券数据库
    with DB(host='10.26.25.95', port=3306, database='yestae_coin', user='yestae_coin',
            passwd='O3DYwq#qo%ZZ2DiU841Ue0') as db_coin:
        na = (1, 1, 0.00)
        sql = 'SELECT user_id,order_no,amount FROM yestae_coin_detail WHERE direction = %s and type  = %s and amount > %s'
        db_coin.execute(sql, na)
        result = db_coin.fetchall()  # fetchall() 获取所有记录
        # print(type(result))  # <class 'list'>
        print("交易完成返还受益券的记录数量为%s" % len(result))
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        start = datetime.datetime.now()
        print("开始执行订单数据库订单主表受益券返券字段更新,开始时间:{}".format(start_time))
        data = []
        for x in result:
            user_id = x[0]
            order_no = x[1].decode('utf-8')
            amount = x[2]
            #
            '''
                按string来显示,byarray代表接收到的数据
                order_no = x[1].decode('utf-8')
                    order_no
                        订单编号:1282505070692298754
                order_no = x[1]
                    str(order_no)
                    
                        订单编号:bytearray(b'1282505070692298754')
                    
            '''
            # 用户中心库
            with DB(host="uc-mysql-master", port="3306", user="tea_uc", passwd="!xkpLr6aW2Z~XW!B8.k~",
                    database="tea_uc") as db_user:
                na = (user_id,)
                sql = 'SELECT user_num FROM uc_user WHERE user_id = %s'
                db_user.execute(sql, na)
                result = db_user.fetchall()
                for y in result:
                    user_num = y[0]
                    utime = int(round(time.time() * 1000))
                    na = (amount, utime, user_id, user_num, order_no)
                    modify_record = []
                    # pro
                    # 取user_num 取余3 来确定数据库位置
                    # 0号库库
                    if int(str(user_num)) % 3 == 0:
                        with DB(host="shard-order-0-master", port="3306", user="mall_order_0",
                                passwd="leREe6BAC_TndsJl",
                                database="mall_order_0") as order_0:
                            sql = 'UPDATE sdb_b2c_order SET receive_coin_num = %s,update_time = %s WHERE member_id = %s AND member_no = %s AND order_no = %s'
                            order_0.execute(sql, na)
                            if order_0.rowcount > 0:
                                x = count(1)
                                print(
                                    str(x) + ",用户userId:{},订单编号:{},的用户编号是user_num:{},订单交易完成返券amount:{}".format(
                                        user_id,
                                        order_no,
                                        user_num,
                                        amount))
                                modify_record.append(user_id)
                                modify_record.append(order_no)
                                modify_record.append(user_num)
                                modify_record.append(amount)
                                data.append(modify_record)
                            else:
                                print("订单编号:{}不存在".format(order_no))
                    # 1号库库
                    if int(str(user_num)) % 3 == 1:
                        with DB(host="shard-order-1-master", port="3306", user="mall_order_1",
                                passwd=".05zf-+VCT0YeIfx",
                                database="mall_order_1") as order_1:
                            sql = 'UPDATE sdb_b2c_order SET receive_coin_num = %s,update_time = %s WHERE member_id = %s AND member_no = %s AND order_no = %s'
                            order_1.execute(sql, na)
                            if order_1.rowcount > 0:
                                x = count(1)
                                print(
                                    str(x) + ",用户userId:{},订单编号:{},的用户编号是user_num:{},订单交易完成返券amount:{}".format(
                                        user_id,
                                        order_no,
                                        user_num,
                                        amount))
                                modify_record.append(user_id)
                                modify_record.append(order_no)
                                modify_record.append(user_num)
                                modify_record.append(amount)
                                data.append(modify_record)
                            else:
                                print("订单编号:{}不存在".format(order_no))
                    # 2号库库
                    if int(str(user_num)) % 3 == 2:
                        with DB(host="shard-order-2-master", port="3306", user="mall_order_2",
                                passwd="rmdj@+lbbA96C15v",
                                database="mall_order_2") as order_2:
                            sql = 'UPDATE sdb_b2c_order SET receive_coin_num = %s,update_time = %s WHERE member_id = %s AND member_no = %s AND order_no = %s'
                            order_2.execute(sql, na)
                            if order_2.rowcount > 0:
                                x = count(1)
                                print(
                                    str(x) + ",用户userId:{},订单编号:{},的用户编号是user_num:{},订单交易完成返券amount:{}".format(
                                        user_id,
                                        order_no,
                                        user_num,
                                        amount))
                                modify_record.append(user_id)
                                modify_record.append(order_no)
                                modify_record.append(user_num)
                                modify_record.append(amount)
                                data.append(modify_record)
                            else:
                                print("订单编号:{}不存在".format(order_no))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        end = datetime.datetime.now()
        print("执行结束订单数据库订单主表受益券返券字段更新,结束时间:{}.执行更新了:{}条记录.耗时:{}秒".format(end_time, count(1) - 1,
                                                                         (end - start).total_seconds()))
        with open('订单数据库订单主表受益券返券字段更新.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
