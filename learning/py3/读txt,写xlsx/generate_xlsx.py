import csv, json, mysql.connector, openpyxl, time
from itertools import islice


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


'''
读取txt文件获取发票信息
'''
# key:order_no,value:order_id
order_no_order_id_dict = {}

order_invoice_db_invoice_info_dict = {}
order_no_invoice_db_order_invoice_info_dict = {}


def read_csv(path):
    with open(path, 'r', encoding='utf-8') as lines:
        array = lines.readlines()
        if len(array) > 0:
            for x in array:
                amount = 0
                json_loads = json.loads(x)[0]
                orderId = json_loads['orderId']  # 订单id
                orderDeliveryNo = json_loads['orderNo']  # 订单号
                # 发票号
                memberName = json_loads['memberName']  # 用户名
                custName = json_loads['custName']  # 发票抬头
                custTaxNo = json_loads['custTaxNo']  # 纳税人识别号
                # 发票申请时间
                items_ = json_loads['orders'][0]['items']
                if len(items_) > 0:
                    for item in items_:
                        amount = amount + item['totalAmount']
                amount = amount  # 开票金额
                # custName = json_loads['custName']  # 收货人姓名
                custPhone = json_loads['custPhone']  # 收货人手机号
                # 收货省份
                # 收货城市
                # 收货区域
                custAddr = json_loads['custAddr']  # 详细地址
                order_invoice_info_dict = {'orderId': orderId, 'memberName': memberName, 'custName': custName,
                                           'custTaxNo': custTaxNo,
                                           'amount': amount, 'custPhone': custPhone,
                                           'orderDeliveryNo': orderDeliveryNo}
                order_no_invoice_db_order_invoice_info_dict[orderDeliveryNo] = order_invoice_info_dict
                order_no_order_id_dict[orderDeliveryNo] = orderId
                print(custAddr)


'''
获取发票号,收货省份/城市/区域,发票申请时间
'''
order_no_invoice_yfphm_dict = {}
order_id_order_db_order_invoice_info_dict = {}
order_no_invoice_receiver_address_dict = {}


def get_invoice_other_info(order_no_order_id_dict):
    # 发票数据库
    with DB(host='192.168.100.153', port='3306', user='root',
            passwd='lb,LtawoFcd.eV@J',
            database='invoice_flow_mgr') as db_invoice_conn:
        db_invoice = db_invoice_conn.cursor()
        if len(order_no_order_id_dict) > 0:
            for order_delivery_no, order_id in order_no_order_id_dict.items():
                sql = "select invoice_yfphm,member_name,cust_name,cust_tax_no,cust_phone,receiver_address from sdb_b2c_invoice_flow where order_id = '%s' and order_no = '%s'" % (
                    order_id, order_delivery_no)
                db_invoice.execute(sql, None)
                result = db_invoice.fetchone()
                if result:
                    invoiceYfphm = result[0]  # 发票号
                    receiverAddress = result[5]  # 收票地址
                    order_no_invoice_yfphm_dict[order_delivery_no] = invoiceYfphm
                    order_no_invoice_receiver_address_dict[order_delivery_no] = receiverAddress
    # 订单中心库
    with DB(host='dev-sharding-m.tae-tea.net', port='3306', user='dev_mall_order_new',
            passwd='O8RzX#3mhbm0pDP7',
            database='dev_mall_order_new') as db_order_conn:
        db_order = db_order_conn.cursor()
        if len(order_no_order_id_dict) > 0:
            for order_delivery_no, order_id in order_no_order_id_dict.items():
                sql = "select order_no,create_time,province,city,area,receiver_name from sdb_order_invoice,receiver_name where order_id = '%s'" % order_id
                db_order.execute(sql, None)
                result = db_order.fetchone()
                if result:
                    orderNo = result[0]
                    createTime = result[1]
                    province = result[2]
                    city = result[3]
                    area = result[4]
                    receiver_name = result[5]
                    order_order_db_invoice_info_dict = {'orderNo': orderNo, 'createTime': createTime,
                                                        'province': province,
                                                        'city': city, 'area': area, 'receiverName':receiver_name}
                    order_id_order_db_order_invoice_info_dict[order_id] = order_order_db_invoice_info_dict
                    # print('订单order_id:{},订单编号order_no:{},发票申请时间:{},收货省份:{},收货城市:{},收货区域"{}'.format(order_id, orderNo,
                    #                                                                                createTime,
                    #                                                                                province, city, area))


'''
数据整合
'''
order_no_invoicd_info_dict = {}


def data_union(order_no_order_id_dict):
    if len(order_no_order_id_dict) > 0:
        for order_delivery_no, order_id in order_no_order_id_dict.items():
            invoice_info_one = order_no_invoice_db_order_invoice_info_dict[order_delivery_no]
            invoiceYfphm = ''
            receiverAddress = ''
            if order_delivery_no in order_no_invoice_yfphm_dict:
                invoiceYfphm = order_no_invoice_yfphm_dict[order_delivery_no]
            if order_delivery_no in order_no_invoice_receiver_address_dict:
                receiverAddress = order_no_invoice_receiver_address_dict[order_delivery_no]
            invoice_info_two = order_id_order_db_order_invoice_info_dict[order_id]

            invoicd_info_dict = invoice_info_one.copy()
            invoicd_info_dict.update(invoice_info_two)
            invoicd_info_dict['invoiceYfphm'] = invoiceYfphm
            invoicd_info_dict['custAddr'] = receiverAddress

            order_no_invoicd_info_dict[order_delivery_no] = invoicd_info_dict


'''
写xlsx文件
'''


def write_excel_xlsx(name, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    workbook.save(name)


if __name__ == '__main__':
    ''' '''
    path = '2.txt'
    read_csv(path)
    get_invoice_other_info(order_no_order_id_dict)
    data_union(order_no_order_id_dict)

    name = '仓颉号已开专票-{}.xlsx'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()))
    sheet = 'Sheet1'
    value_list = []
    xlsx_title = ["订单号", "发票号", "用户名", "发票抬头", "纳税人识别号", "发票申请时间", "开票金额", "收货人姓名", "收货人手机号", "收货省份", "收货城市",
                  "收货区域", "详细地址"]
    value_list.append(xlsx_title)
    for order_delivery_no, invoice_info in order_no_invoicd_info_dict.items():
        xlsx_value_list = [invoice_info['orderId'], invoice_info['orderNo'], invoice_info['orderDeliveryNo'],
                           invoice_info['invoiceYfphm'], invoice_info['memberName'],
                           invoice_info['custName'], invoice_info['custTaxNo'],
                           time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(invoice_info['createTime'] / 1000)))
            , invoice_info['amount'], invoice_info['receiverName'], invoice_info['custPhone'], invoice_info['province'],
                           invoice_info['city'], invoice_info['area'], invoice_info['custAddr']]
        value_list.append(xlsx_value_list)
    write_excel_xlsx(name, sheet, value_list)
