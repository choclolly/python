import mysql.connector
import uuid
import time


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


if __name__ == '__main__':
    with DB(host="192.168.100.153", port="3306", user="root", passwd="lb,LtawoFcd.eV@J",
            database="dev_coin") as db_coin:
        list_order_no = [1318910963968634882,
                         1318908297320988673,
                         1318916830339002369,
                         1318911210295406593,
                         1318909815113252866,
                         1318811580970037250,
                         1318911295397031937,
                         1318904590390956033,
                         1318912454515224578,
                         1318911034227421186,
                         1318488551938584578,
                         1318910798819696641,
                         1318898750277021697,
                         1318911216880852994,
                         1318362471814148098]
        print("*******************begin*******************")
        for order_no in list_order_no:
            sql = 'SELECT user_id,order_no,amount,source FROM yestae_coin_detail WHERE direction = 2 AND type = 0 and order_no = %s'
            na = (order_no,)
            db_coin.execute(sql, na)
            result = db_coin.fetchall()
            for x in result:
                userId = x[0]
                orderNo = x[1].decode('utf-8')
                amount = x[2]
                source = x[3]
                id = str(uuid.uuid4()).replace("-", "")
                flowNo = str(uuid.uuid4()).replace("-", "")
                print("user_id:{},order_no:{},amount:{}".format(userId, orderNo, amount))
                sql = 'SELECT amount from yestae_coin WHERE user_id = %d' % userId
                db_coin.execute(sql, None)
                coin_fetchone = db_coin.fetchone()
                for b in coin_fetchone:
                    balance = b
                    later_amount = amount + b
                    createTime = millis_time = int(round(time.time() * 1000))
                    sql = 'INSERT INTO yestae_coin_detail (`id`, `user_id`, `flow_no`, `order_no`, `product`, `source`, `direction`, `type`, `amount`, `pre_amount`, `later_amount`, `remark`, `create_time`, `invalid_time`) VALUES ' \
                          '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NULL);'
                    na = (id, userId, flowNo, orderNo, 0, source, '1', '3', amount, balance, later_amount,
                          '订单编号:[{}],订单退款退回已使用的受益券:{}'.format(orderNo, amount), createTime)
                    db_coin.execute(sql, na)

                    sql = 'UPDATE yestae_coin SET amount =%s,update_time = %s WHERE user_id = %s'
                    na = (later_amount, millis_time, userId)
                    db_coin.execute(sql, na)
                    print(sql)
        print("*******************end  *******************")