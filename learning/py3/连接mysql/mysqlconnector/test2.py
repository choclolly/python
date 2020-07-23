from connector2 import DB

if __name__ == '__main__':
    with DB(host='59.110.228.110', port=3306, database='test_tea_uc_0', user='test_tea_uc_0',
            passwd='L~+SJ*F^kon[t+10l6') as db:
        db.execute('select * from uc_user limit 0,10')
        print(db)
        for i in db:
            print(i)

        list_0 = [1, 2, 3, 4, 5, 6]
        for x in list_0:
            if x < 3:
                print('22222222222222')
                continue
        print('over')