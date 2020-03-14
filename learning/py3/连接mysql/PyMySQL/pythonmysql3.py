#  以 pymysql 为例，实现通过 with 简化数据库操作
from pymysql import connect, cursors


class DB:
    def __init__(self, host, port, database, user, passwd, charset='utf8'):
        # 建立连接
        self.conn = connect(host=host, port=port, db=database, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=cursors.DictCursor)

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
