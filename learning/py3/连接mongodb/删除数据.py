from pythonmongo3 import DB
import pythonmongo3

h = '47.94.173.249'
pr = 27017
d = 'test_tea'
u = 'test_app'
pw = '7dWr7T12'

'''
delete_one() 方法来删除一个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
'''


def delete_one():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"name": "Taobao"}
        col.delete_one(query)
        # 删除后输出
        for x in col.find():
            print(x)


'''
删除多个文档
    我们可以使用 delete_many() 方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
删除所有 name 字段中以 F 开头的文档:
'''


def delete_many():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"name": {"$regex": "^F"}}
        x = col.delete_many(query)
        # 删除后输出
        print(x.deleted_count, "个文档已删除")


'''
删除集合中的所有文档
    delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档：
'''


def delete_many_all():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {}
        x = col.delete_many(query)
        # 删除后输出
        print(x.deleted_count, "个文档已删除")


'''
删除集合
    我们可以使用 drop() 方法来删除一个集合。
'''


def drop():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {}
        col.drop(query)


if __name__ == '__main__':
    # delete_one()
    # delete_many()
    # delete_many_all()
    drop()
    # 查询   调用 pythonmongo3里的find() 方法
    pythonmongo3.find()