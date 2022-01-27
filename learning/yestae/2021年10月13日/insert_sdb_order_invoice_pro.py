import xlrd, time, uuid, mysql.connector, json
from itertools import islice

'''
    电票 && 未开具
    select * from sdb_order_invoice where invoice_type = '2' and do_invoice_time is null and invoice_state = '2' limit 2
'''


class DB:
    def __init__(self, host, port, database, user, passwd):
        self.conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            database=database,
            buffered=True
        )
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


def method_1():
    path = r'仓颉号10.25-12.8发票.xls'
    # 打开文件
    # wb = xlrd.open_workbook(r'b_feed.xlsx')
    wb = xlrd.open_workbook(path)
    # 获取所有sheet
    sheet_names = wb.sheet_names()
    print(sheet_names)  # ['电子发票', '专票', 'Sheet3']
    sheet_name_1 = wb.sheet_by_index(0)
    iter_row_num = iter(range(sheet_name_1.nrows))
    for i in islice(iter_row_num, 1, None):
        row_value = sheet_name_1.row_values(i)
        row_value.pop(0)  # 移除列表中第一个元素
        #print(row_value)

        order_no = row_value[0]

        with DB(host='order-mysql-master', port='3306', user='ebs_operate', passwd='7hayoHyOd5n7xADU',
                database='ebs_operate') as db_order_conn:
            db_order = db_order_conn.cursor()
            # print('db_order_0:{}'.format(db_order))
            sql = "SELECT order_id,member_id,member_no,member_name,member_phone,member_level,province_code,province,city_code,city,area_code,area,receiver_phone,receiver_address FROM sdb_order_address WHERE order_no = '%s'" % order_no
            db_order.execute(sql, None)
            result = db_order.fetchone()
            if result:
                id = str(str(uuid.uuid1()).replace("-", ""))
                member_id = result[1]  # .decode('utf-8')
                member_no = result[2]  # .decode('utf-8')
                member_name = result[3]
                member_phone = result[4]
                member_level = result[5]
                order_id = result[0]  # .decode('latin-1')
                order_no = order_no
                receiver_phone = result[12]
                invoice_type = '2'
                # 电票
                invoice_content = {"content": row_value[4], "id": id, "isDefault": 0,
                                       "mail": row_value[3], "mobile": result[12],
                                       "taxpayerIdentityNumber": row_value[5], "title": "单位", "type": 2,
                                       "uid": result[1]}
                invoice_state = '2'
                receiver_address = result[13]
                province_code = result[6]
                province = result[7]
                city_code = result[8]
                city = result[9]
                area_code = result[10]
                area = result[11]
                create_time = int(time.time() * 1000)
                create_year = time.localtime(time.time()).tm_year
                create_month = time.localtime(time.time()).tm_mon
                order_type = '1'

                receiver_name = result[3]
                is_confirm = '1'
                shop_id = '1350358452802686978'
                shop_name = '大益商城'
                delete_flag = 0
                is_ask = 0
                i = int(str(member_no)) % 3
                if i == 0:
                    insert_order_invoice_sql = "INSERT INTO `sdb_order_invoice`(" \
                                               "`id`, `member_id`, `member_no`, `member_name`, `member_phone`, `member_level`, " \
                                               "`order_id`, `order_no`, `receiver_phone`, `invoice_type`, " \
                                               "`invoice_content`, " \
                                               "`invoice_state`,`receiver_address`, `province_code`, `province`, `city_code`, `city`, `area_code`, `area`, `zip`, " \
                                               "`create_time`, `update_time`, `create_year`, `create_month`, " \
                                               "`logistic_type`, `order_type`, `invoice_no`, `invoice_code`, `company_name`, `delivery_no`, `invoice_url`, `return_msg`, " \
                                               "`biz_id`, `receiver_name`, `is_confirm`, `do_invoice_time`, `invoice_pic_url`, " \
                                               "`shop_id`, `shop_name`, `create_id`, `create_name`, `update_id`, `update_name`, `delete_flag`, `is_ask`) VALUES (" \
                                               "'%s', '%s', %s, '%s', '%s', '%s', " \
                                               "'%s', '%s', '%s', '2', " \
                                               "'%s', " \
                                               "'2', '%s', '%s', '%s', '%s', '%s', '%s', '%s', NULL, " \
                                               "%s, NULL, %s, %s, " \
                                               "NULL, '1', NULL, NULL, NULL, NULL, NULL, NULL, " \
                                               "NULL, '%s', '1', NULL, NULL, " \
                                               "'1350358452802686978', '大益商城', '', '', '', '', 0, 0);" % (
                                                   id, member_id, member_no, member_name, member_phone, member_level,
                                                   order_id, order_no, receiver_phone,
                                                   json.dumps(invoice_content, ensure_ascii=False),
                                                   receiver_address, province_code, province, city_code, city, area_code,
                                                   area,
                                                   create_time, create_year, create_month,
                                                   receiver_name)
                    print(insert_order_invoice_sql)

    print('//////////////分割线////////////////')
    sheet_name_2 = wb.sheet_by_index(1)
    for i in range(sheet_name_2.nrows):
        row_value = sheet_name_2.row_values(i)
        row_value.pop(0)
        #print(row_value)

        order_no = row_value[0]

        with DB(host='order-mysql-master', port='3306', user='ebs_operate', passwd='7hayoHyOd5n7xADU',
                database='ebs_operate') as db_order_conn:
            db_order = db_order_conn.cursor()
            # print('db_order_0:{}'.format(db_order))
            sql = "SELECT order_id,member_id,member_no,member_name,member_phone,member_level,province_code,province,city_code,city,area_code,area,receiver_phone,receiver_address FROM sdb_order_address WHERE order_no = '%s'" % order_no
            db_order.execute(sql, None)
            result = db_order.fetchone()
            if result:
                id = str(str(uuid.uuid1()).replace("-", ""))
                member_id = result[1]  # .decode('utf-8')
                member_no = result[2]  # .decode('utf-8')
                member_name = result[3]
                member_phone = result[4]
                member_level = result[5]
                order_id = result[0]  # .decode('latin-1')
                order_no = order_no
                receiver_phone = result[12]
                invoice_type = '5'
                # 专票
                invoice_content = {"content": row_value[3], "id": id, "isDefault": 0,
                     "specialBankAccount": row_value[8], "specialCompanyAddr": row_value[5],
                     "specialCompanyBank": row_value[7], "specialCompanyName": row_value[3],
                     "specialCompanyTel": row_value[6], "taxpayerIdentityNumber": row_value[4],
                     "title": row_value[3], "type": 5, "uid": member_id}
                invoice_state = '2'
                receiver_address = result[13]
                province_code = result[6]
                province = result[7]
                city_code = result[8]
                city = result[9]
                area_code = result[10]
                area = result[11]
                create_time = int(time.time() * 1000)
                create_year = time.localtime(time.time()).tm_year
                create_month = time.localtime(time.time()).tm_mon
                order_type = '1'

                receiver_name = result[3]
                is_confirm = '1'
                shop_id = '1350358452802686978'
                shop_name = '大益商城'
                delete_flag = 0
                is_ask = 0
                i = int(str(member_no)) % 3
                if i == 0:
                    insert_order_invoice_sql = "INSERT INTO `sdb_order_invoice`(" \
                                               "`id`, `member_id`, `member_no`, `member_name`, `member_phone`, `member_level`, " \
                                               "`order_id`, `order_no`, `receiver_phone`, `invoice_type`, " \
                                               "`invoice_content`, " \
                                               "`invoice_state`,`receiver_address`, `province_code`, `province`, `city_code`, `city`, `area_code`, `area`, `zip`, " \
                                               "`create_time`, `update_time`, `create_year`, `create_month`, " \
                                               "`logistic_type`, `order_type`, `invoice_no`, `invoice_code`, `company_name`, `delivery_no`, `invoice_url`, `return_msg`, " \
                                               "`biz_id`, `receiver_name`, `is_confirm`, `do_invoice_time`, `invoice_pic_url`, " \
                                               "`shop_id`, `shop_name`, `create_id`, `create_name`, `update_id`, `update_name`, `delete_flag`, `is_ask`) VALUES (" \
                                               "'%s', '%s', %s, '%s', '%s', '%s', " \
                                               "'%s', '%s', '%s', '5', " \
                                               "'%s', " \
                                               "'2', '%s', '%s', '%s', '%s', '%s', '%s', '%s', NULL, " \
                                               "%s, NULL, %s, %s, " \
                                               "NULL, '1', NULL, NULL, NULL, NULL, NULL, NULL, " \
                                               "NULL, '%s', '1', NULL, NULL, " \
                                               "'1350358452802686978', '大益商城', '', '', '', '', 0, 0);" % (
                                                   id, member_id, member_no, member_name, member_phone, member_level,
                                                   order_id, order_no, receiver_phone,
                                                   json.dumps(invoice_content, ensure_ascii=False),
                                                   receiver_address, province_code, province, city_code, city, area_code,
                                                   area,
                                                   create_time, create_year, create_month,
                                                   receiver_name)
                    print(insert_order_invoice_sql)


method_1()
