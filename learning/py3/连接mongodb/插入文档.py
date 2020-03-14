from pythonmongo3 import DB

h = '47.94.173.249'
pr = 27017
d = 'test_tea'
u = 'test_app'
pw = '7dWr7T12'
'''
插入集合
    集合中插入文档使用 insert_one() 方法，该方法的第一参数是字典 name => value 对。
以下实例向 sites 集合中插入文档：
'''


def insert_one():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        d_dict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
        # 集合中插入文档
        x = col.insert_one(d_dict)
        print(x)


'''
返回 _id 字段
    insert_one() 方法返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值。
如果我们在插入文档时没有指定 _id，MongoDB 会为每个文档添加一个唯一的 id。
'''


def inserted_id():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        d_dict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
        # 集合中插入文档
        x = col.insert_one(d_dict)
        print(x)
        # 返回 _id 字段
        print(x.inserted_id)


'''
插入多个文档
    集合中插入多个文档使用 insert_many() 方法，该方法的第一参数是字典列表。
insert_many() 方法
    返回 InsertManyResult 对象，该对象包含 inserted_ids 属性，该属性保存着所有插入文档的 id 值。
'''


def insert_many():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        l_list = [
            {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
            {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
            {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
            {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
            {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
        ]
        # 集合中插入文档
        x = col.insert_many(l_list)
        print(x)
        # 输出插入的所有文档对应的 _id 值
        print(x.inserted_ids)


'''
插入指定 _id 的多个文档
    我们也可以自己指定 id，插入，以下实例我们在 site2 集合中插入数据，_id 为我们指定的：
'''


def insert_many2():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        l_list = [
            {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
            {"_id": 2, "name": "Google", "address": "Google 搜索"},
            {"_id": 3, "name": "Facebook", "address": "脸书"},
            {"_id": 4, "name": "Taobao", "address": "淘宝"},
            {"_id": 5, "name": "Zhihu", "address": "知乎"}
        ]
        # 集合中插入文档
        x = col.insert_many(l_list)
        print(x)
        # 输出插入的所有文档对应的 _id 值
        print(x.inserted_ids)


if __name__ == '__main__':
    # insert_one()
    inserted_id()
    # insert_many()
    # insert_many2()
