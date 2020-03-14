from connector2 import DB

if __name__ == '__main__':
    with DB(host='59.110.228.110', port=3306, database='test_tea_uc_0', user='test_tea_uc_0',
            passwd='L~+SJ*F^kon[t+10l6') as db:
        db.execute('select * from uc_user limit 0,10')
        print(db)
        for i in db:
            print(i)
