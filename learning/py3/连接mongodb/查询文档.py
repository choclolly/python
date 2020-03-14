from pythonmongo3 import DB

'''
注意：
    你引入的模块中的主程序会先执行。即
    if __name__ == '__main__':
        print("我是pythonmongo3.py")
        
'''

h = '47.94.173.249'
pr = 27017
d = 'test_tea'
u = 'test_app'
pw = '7dWr7T12'

"""
查询一条数据
    我们可以使用 find_one() 方法来查询集合中的一条数据
"""


def find_one():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        # 查询一条数据
        x = col.find_one()
        print(x)


"""
查询全量数据
    find() 方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作
"""


def find():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        # 查询全量数据
        x = col.find()
        for y in x:
            print(y)


'''
查询指定字段的数据
    可以使用 find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。
'''


def find_colum():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        for y in col.find({}, {"_id": 0, "name": 1, "alexa": 1}):
            print(y)


# 注意：除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1
# 以下实例除了 alexa 字段外，其他都返回：
def find_colum2():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        for y in col.find({}, {"alexa": 0}):
            print(y)


# 以下代码同时指定了 0 和 1 则会报错：
# 错误内容：pymongo.errors.OperationFailure: Projection cannot have a mix of inclusion and exclusion.
def find_colum3():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        for y in col.find({}, {"name": 1, "alexa": 0 }):
            print(y)


'''
根据指定条件查询
    我们可以在 find() 中设置参数来过滤数据。
以下实例查找 name 字段为 "RUNOOB" 的数据：
'''


def find_query():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"name": "RUNOOB"}
        for y in col.find(query):
            print(y)


'''
高级查询
    查询的条件语句中，我们还可以使用修饰符。
以下实例用于读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} 
'''


def find_senior():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"name": {"$gt": "H"}}
        for y in col.find(query):
            print(y)


'''
使用正则表达式查询
    我们还可以使用正则表达式作为修饰符。
    正则表达式修饰符只用于搜索字符串的字段。
以下实例用于读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"} :
'''


def find_regular():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        query = {"name": {"$regex": "^R"}}
        for y in col.find(query):
            print(y)


'''
返回指定条数记录
    如果我们要对查询结果设置指定条数的记录可以使用 limit() 方法，该方法只接受一个数字参数。
以下实例返回 3 条文档记录：
'''


def find_limit():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        result = col.find().limit(3)
        for y in result:
            print(y)


if __name__ == '__main__':
    # with DB(host=h, port=pr, database=d, user=u,
    #         passwd=pw) as dbs:
    #     mycol = dbs["sites"]
    #     print(dbs)
    #     # 查询一条数据
    #     a = mycol.find_one()
    #     print(a)
    #     # 查询全量数据
    #     a = mycol.find()
    #     # for i in a:
    #     #     print(i)

    '''
    调用自定义方法
    '''
    # find_one()
    # find()
    # find_colum()
    # find_colum2()
    # # find_colum3()
    # find_query()
    # find_senior()
    # find_regular()
    find_limit()
