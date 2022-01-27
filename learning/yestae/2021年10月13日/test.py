import mysql.connector,json


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


with DB(host='dev-sharding-m.tae-tea.net', port='3306', user='dev_mall_order_new',
        passwd='O8RzX#3mhbm0pDP7',
        database='dev_mall_order_new') as db_order_conn:
    db_order = db_order_conn.cursor()
    # print('db_order_0:{}'.format(db_order))
    sql = "SELECT invoice_content FROM sdb_order_invoice WHERE id = '%s'" % 'e910c0b02cbf11eca334f8da0c5e5ae1'
    db_order.execute(sql, None)
    result = db_order.fetchone()
    if result:
        invoice_content = result[0]
        invoice_content = json.loads(invoice_content)
        if invoice_type == '1':  # 1：电子个人
            custName = invoice_content['content']
            custTelephone = apply_order_invoice_order_id_receiver_phone[order_id]
            invoiceType = '1'
            receiverEmail = invoice_content['mail']
        elif invoice_type == '2':  # 2：电子公司
            custName = invoice_content['content']
            custTaxNo = invoice_content['taxpayerIdentityNumber']
            custTelephone = apply_order_invoice_order_id_receiver_phone[order_id]
            invoiceType = '2'
            receiverEmail = invoice_content['mail']
