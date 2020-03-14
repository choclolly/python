from pythonmongo3 import DB

"""
sort() 方法可以指定升序或降序排序。
sort() 方法第一个参数为要排序的字段，第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序。
"""

h = '47.94.173.249'
pr = 27017
d = 'test_tea'
u = 'test_app'
pw = '7dWr7T12'

'''
对字段 alexa 按升序排序：
'''


def sort_asc():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        a = col.find().sort("alexa")
        for x in a:
            print(x)


'''
对字段 alexa 按降序排序：
'''


def sort_desc():
    with DB(host=h, port=pr, database=d, user=u,
            passwd=pw) as db:
        # 指定集合
        col = db["sites"]
        print(db)
        a = col.find().sort("alexa", -1)
        for x in a:
            print(x)


if __name__ == '__main__':
    sort_asc()
    sort_desc()

'''
    Database(MongoClient(host=['47.94.173.249:27017'], document_class=dict, tz_aware=False, connect=True), 'test_tea')
    {'_id': ObjectId('5e6c8410bfed5b9281f460b1'), 'name': 'Facebook', 'alexa': '10', 'url': 'https://www.facebook.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460af'), 'name': 'Taobao', 'alexa': '100', 'url': 'https://www.taobao.com'}
    {'_id': ObjectId('5e6c8434b6687ed632bbb6eb'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460b0'), 'name': 'QQ', 'alexa': '101', 'url': 'https://www.qq.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460b2'), 'name': '知乎', 'alexa': '103', 'url': 'https://www.zhihu.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460b3'), 'name': 'Github', 'alexa': '109', 'url': 'https://www.github.com'}
    Database(MongoClient(host=['47.94.173.249:27017'], document_class=dict, tz_aware=False, connect=True), 'test_tea')
    {'_id': ObjectId('5e6c8410bfed5b9281f460b3'), 'name': 'Github', 'alexa': '109', 'url': 'https://www.github.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460b2'), 'name': '知乎', 'alexa': '103', 'url': 'https://www.zhihu.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460b0'), 'name': 'QQ', 'alexa': '101', 'url': 'https://www.qq.com'}
    {'_id': ObjectId('5e6c8434b6687ed632bbb6eb'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460af'), 'name': 'Taobao', 'alexa': '100', 'url': 'https://www.taobao.com'}
    {'_id': ObjectId('5e6c8410bfed5b9281f460b1'), 'name': 'Facebook', 'alexa': '10', 'url': 'https://www.facebook.com'}
    
    观察数据
        为什么'101' 大于 '10000' ????????
'''
