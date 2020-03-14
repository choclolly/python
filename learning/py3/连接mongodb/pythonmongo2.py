import pymongo


class DB:
    def __init__(self, host, port, database, user, passwd):
        self.conn = pymongo.MongoClient(host=host, port=port)
        self.db = self.conn[database]
        self.db.authenticate(name=user, password=passwd)

    def __enter__(self):
        # 返回db
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with DB(host='47.94.173.249', port=27017, database='test_tea', user='test_app',
            passwd='7dWr7T12') as db:
        mycol = db["b_feed"]
        print(db)
        # 查询一条数据
        x = mycol.find_one()
        print(x)
        # 查询全量数据
        x = mycol.find()
        # for i in x:
        #     print(i)
