from pythonmongo3 import DB

h = '47.94.173.249'
pr = 27017
d = 'test_tea'
u = 'test_app'
pw = '7dWr7T12'


def find():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"alexa": "12345"}
        for y in col.find(query):
            print(y)


'''
MongoDB 中使用 update_one() 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段。
    如果查找到的匹配数据多余一条，则只会修改第一条。
'''


def update_one():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"alexa": "12345"}
        newvalues = {"$set": {"alexa": "10000"}}
        col.update_one(query, newvalues)
        # 输出修改后的  "sites"  集合
        for x in col.find(query):
            print(x)


'''
update_one() 方法只能修匹配到的第一条记录，
    如果要修改所有匹配到的记录，可以使用 update_many()。
以下实例将查找所有以 F 开头的 name 字段，并将匹配到所有记录的 alexa 字段修改为 123：
'''


def update_many():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"alexa": "12345"}
        newvalues = {"$set": {"alexa": "10000"}}
        col.update_many(query, newvalues)
        # 输出修改后的  "sites"  集合
        for x in col.find(query):
            print(x)


if __name__ == '__main__':
    find()
    update_one()
    update_many()
