import pymongo

'''
创建一个mongo库
    在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
'''
# 建立连接
client = pymongo.MongoClient("47.94.173.249", 27017)

'''
连接自己的mongodb
    mydb = client.test_tea  和   mydb = client["test_tea"]
    是一样的
'''
db = client.test_tea

# 认证用户密码
db.authenticate('test_app', '7dWr7T12')

# 创建test集合和插入数据
col = db.test
col.insert_one({"name": "this is test"})
# 打印数据输出
for item in col.find():
    print(item)
'''
指定mongodb中的集合
    查询一条数据
'''
mycol = db["b_feed"]
x = mycol.find_one()
print(x)
'''
查询集合中所有数据
'''
y = mycol.find()
for x in y:
    print(x)

# 关闭连接
client.close()
