#  以 连接mysql.connector 为例，实现通过 with 简化数据库操作
import mysql.connector


class DB:
    def __init__(self, host, port, database, user, passwd):
        self.conn = mysql.connector.connect(
            host=host,  # 数据库主机地址
            port=port,
            user=user,  # 数据库用户名
            passwd=passwd,  # 数据库密码
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


if __name__ == '__main__':
    with DB(host='59.110.228.110', port=3306, database='test_tea_uc_0', user='test_tea_uc_0',
            passwd='L~+SJ*F^kon[t+10l6') as db:
        db.execute('select * from uc_user limit 0,10')
        print(db)
        for i in db:
            print(i)
