import requests, json, mysql.connector, time, uuid, pika, csv, re
from itertools import islice

'''
DB类
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


# filter_special_characters = u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])"
filter_special_characters = "['!#$%&\'*+,./:;<=>?@，。?★、…【】《》？“”‘'！[\\]^_`{|}~\s]+"

'''
根据sku获取订单商品信息,筛选已发货的订单
'''
cangjie_order_id_list = []
cangjie_order_id_member_info = {}


def get_orderId_by_sku(product_no):
    # 订单中心库
    with DB(host='dev-sharding-m.tae-tea.net', port='3306', user='dev_mall_order_new',
            passwd='O8RzX#3mhbm0pDP7',
            database='dev_mall_order_new') as db_order_conn:
        db_order = db_order_conn.cursor()
        # print('db_order_0:{}'.format(db_order))
        # 包含仓颉好商品所有的订单order_id
        sql = "SELECT order_id FROM sdb_order_goods WHERE product_no = '%s'" % product_no
        db_order.execute(sql, None)
        result = db_order.fetchall()
        if result:
            for x in result:
                order_id = x[0]  # .decode('utf-8')
                # print(order_id)
                # 已发货的订单
                sql = "SELECT member_id,member_name,member_no,member_phone FROM sdb_order WHERE id = '%s' AND deliver_state = 1 AND order_state in (3,4)" % order_id
                db_order.execute(sql, None)
                result = db_order.fetchone()
                if result:
                    member_info_dict = {'member_id': result[0], 'member_name': result[1], 'member_no': str(result[2]),
                                        'member_phone': result[3]}
                    cangjie_order_id_list.append(order_id)
                    cangjie_order_id_member_info[order_id] = member_info_dict
        print('已发货的仓颉号订单数量为:{}'.format(len(cangjie_order_id_list)))


'''根据订单id查询申请电票的信息'''
# 申请了发票的仓颉号订单id
apply_order_invoice_order_id = []
apply_order_invoice_order_id_invoice_type_content_dict = {}
apply_order_invoice_order_id_receiver_phone = {}


def get_apply_order_invoice_info(cangjie_order_id_list):
    # 订单中心库
    with DB(host='dev-sharding-m.tae-tea.net', port='3306', user='dev_mall_order_new',
            passwd='O8RzX#3mhbm0pDP7',
            database='dev_mall_order_new') as db_order_conn:
        db_order = db_order_conn.cursor()
        # print('db_order_0:{}'.format(db_order))
        if len(cangjie_order_id_list) > 0:
            for order_id in cangjie_order_id_list:
                # 查询是否申请了开票 invoice_type 2-电票 5-专票
                sql = "SELECT invoice_type,invoice_content,receiver_phone FROM sdb_order_invoice WHERE order_id = '%s' and invoice_type in ('1','2')" % order_id
                db_order.execute(sql, None)
                result = db_order.fetchone()
                if result:
                    invoice_type = result[0]  # .decode('latin-1')
                    invoice_content = result[1]  # .decode('utf-8')
                    receiver_phone = result[2]  # .decode('utf-8')
                    invoice_type_content_dict = {invoice_type: invoice_content}
                    apply_order_invoice_order_id.append(order_id)
                    apply_order_invoice_order_id_invoice_type_content_dict[order_id] = invoice_type_content_dict
                    apply_order_invoice_order_id_receiver_phone[order_id] = receiver_phone
        print('申请了电票的仓颉号订单数量:{}'.format(len(apply_order_invoice_order_id)))


'''根据订单id,查询发货单信息'''

# key:order_id,value:order_delivery_no
order_id_order_delivery_no_dict = {}

# key:order_delivery_no,value:delivery_id
order_delivery_no_delivery_id_product_no_goods_num_dict = {}
order_delivery_no_delivery_id_product_no_goods_unit_dict = {}
# key:goodsSku,value:unit
goodsSku_unit_dict = {}
# key ：order_delivery_goods_id，value：order_delivery_goods_id_product_no
order_delivery_no_product_no_goods_num_dict = {}
order_delivery_no_product_no_goods_unit_dict = {}


# product_properties = {"code": "1001", "name": "7572+7542（2001）", "percent": 100,
#                       "quantity": 1, "taxPrice": 128, "totalAmount": 128, "unit": "对"}
# product_no_product_properties_dict = {'商品504950': product_properties}


def get_cangjie_delivered_order_delivery_no_by_order_id(apply_order_invoice_order_id):
    # 订单中心库
    with DB(host='dev-sharding-m.tae-tea.net', port='3306', user='dev_mall_order_new',
            passwd='O8RzX#3mhbm0pDP7',
            database='dev_mall_order_new') as db_order_conn:
        db_order = db_order_conn.cursor()
        # print('db_order_0:{}'.format(db_order))
        if len(apply_order_invoice_order_id) > 0:
            for order_id in apply_order_invoice_order_id:
                order_delivery_no_list = []
                sql = "SELECT id,order_delivery_no FROM sdb_order_delivery WHERE order_id = '%s'" % order_id
                db_order.execute(sql, None)
                result = db_order.fetchall()
                if result:
                    for x in result:
                        order_id_order_delivery_goods_product_no_list = []
                        order_id_order_delivery_goods_product_no_goods_num_dict = {}
                        order_id_order_delivery_goods_product_no_goods_unit = {}
                        # 发货单ID
                        delivery_id = x[0]  # .decode('utf-8')
                        # 发货单单号
                        order_delivery_no = x[1]  # .decode('utf-8')
                        order_delivery_no_list.append(order_delivery_no)

                        # 根据发货单id查询发货单商品
                        sql = "SELECT product_no,goods_nums,goods_unit FROM sdb_order_delivery_goods WHERE delivery_id = '%s'" % delivery_id
                        db_order.execute(sql, None)
                        result = db_order.fetchall()
                        if result:
                            for y in result:
                                product_no = y[0]
                                goods_nums = y[1]
                                goods_unit = y[2]
                                order_id_order_delivery_goods_product_no_list.append(y[0])
                                order_id_order_delivery_goods_product_no_goods_num_dict[product_no] = goods_nums
                                order_id_order_delivery_goods_product_no_goods_unit[product_no] = goods_unit
                            order_delivery_no_product_no_goods_num_dict[
                                order_delivery_no] = order_id_order_delivery_goods_product_no_goods_num_dict
                            order_delivery_no_product_no_goods_unit_dict[
                                order_delivery_no] = order_id_order_delivery_goods_product_no_goods_unit
                    order_id_order_delivery_no_dict[order_id] = order_delivery_no_list
            '''
            if len(order_id_order_delivery_no_dict) > 0:
                order_ids = order_id_order_delivery_no_dict.keys()
                for order_id in order_ids:
                    order_delivery_nos = order_id_order_delivery_no_dict[order_id]
                    for order_delivery_no in order_delivery_nos.copy():
                        # 读取已开电票的订单物流单
                        with open('cangjie_order_invoice_202108051217.csv', encoding='utf-8') as f:
                            reader = csv.reader(f)
                            for row in islice(reader, 1, None):
                                if row[2] == '1' or row[2] == '2':
                                    order_id_csv = row[1]
                                    order_delivery_no_csv = row[0]
                                    if order_id_csv == order_id and order_delivery_no_csv == order_delivery_no:
                                        order_delivery_nos.remove(order_delivery_no)
                    if len(order_delivery_nos) == 0:
                        del[order_id_order_delivery_no_dict[order_id]]
            '''


'''根据订单id与发货单单号查询发票流水,成功的不发送消息;失败以及没有记录的发消息'''

canjie_dianpiao_mq_msg_list = []


def get_order_invoice_info(order_id_order_delivery_no_dict):
    # 发票数据库
    # with DB(host='172.17.180.13', port='30001', user='invoice_flow_mgr',
    #         passwd='!pp$VPFS4FAMsT41',
    #         database='invoice_flow_mgr') as db_order_conn:
    with DB(host='192.168.100.153', port='3306', user='root',
            passwd='lb,LtawoFcd.eV@J',
            database='invoice_flow_mgr') as db_order_conn:
        db_order = db_order_conn.cursor()
        # print('db_order_0:{}'.format(db_order))
        order_ids = order_id_order_delivery_no_dict.keys()
        for order_id in order_ids:
            order_delivery_nos = order_id_order_delivery_no_dict[order_id]
            for order_delivery_no in order_delivery_nos:
                flag = False

                # 读取已开电票的订单物流单
                with open('cangjie_order_invoice_202108051217.csv', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in islice(reader, 1, None):
                        if row[2] == '1' or row[2] == '2':
                            order_id_csv = row[1]
                            order_delivery_no_csv = row[0]
                            if order_id_csv == order_id and order_delivery_no_csv == order_delivery_no:
                                flag = True

                if flag is not True:
                    # state 状态 1:成功，0:失败    and state = '1'
                    sql = "SELECT state FROM sdb_b2c_invoice_flow WHERE order_id = '%s' AND order_no = '%s'" % (
                        order_id, order_delivery_no)
                    db_order.execute(sql, None)
                    result = db_order.fetchone()

                    if result is None:
                        # 发送消息'
                        # 开票信息
                        for invoice_type, invoice_content in apply_order_invoice_order_id_invoice_type_content_dict[
                            order_id].items():
                            custName = ''
                            custTaxNo = ''
                            custTelephone = ''
                            invoiceType = ''
                            receiverEmail = ''
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
                        # 用户信息
                        member_id_ = cangjie_order_id_member_info[order_id]['member_id']
                        memberName_ = cangjie_order_id_member_info[order_id]['member_name']
                        memberNo_ = cangjie_order_id_member_info[order_id]['member_no']
                        memberPhone_ = cangjie_order_id_member_info[order_id]['member_phone']
                        # 订单信息
                        orderId = order_id
                        orderNo = order_delivery_no
                        # 订单商品信息
                        orders = []
                        order_dict = {}
                        billNo = order_delivery_no
                        items = []
                        product_no_goods_num_dict = order_delivery_no_product_no_goods_num_dict[order_delivery_no]
                        product_nos = product_no_goods_num_dict.keys()
                        for product_no in product_nos:
                            properties_by_goods_sku = get_goods_properties_by_goodsSku(product_no, order_delivery_no)
                            item = properties_by_goods_sku
                            items.append(item)
                        order_dict['billNo'] = billNo
                        order_dict['items'] = items
                        orders.append(order_dict)
                        # 构造电票消息体
                        body = {}
                        body['custEmail'] = receiverEmail
                        body['custName'] = re.sub(filter_special_characters, '', custName)
                        body['custTaxNo'] = custTaxNo
                        body['custTelephone'] = re.sub(filter_special_characters, '', custTelephone)
                        body['invoiceType'] = invoiceType
                        body['isRedFlag'] = False
                        body['memberId'] = member_id_
                        body['memberName'] = memberName_
                        body['memberNo'] = memberNo_
                        body['memberPhone'] = memberPhone_
                        body['orderId'] = orderId
                        body['orderNo'] = orderNo
                        body['orders'] = orders
                        body['platformType'] = '1'
                        body['receiverEmail'] = receiverEmail

                        # 消息队列
                        exchange = 'port.notify.exchange_test'
                        routing_key = 'order.electronic.invoice.queue'
                        queue = 'order_electronic_invoice_queue_test'
                        body = json.dumps(body,
                                          ensure_ascii=False)  # json.dumps()有一个ensure_ascii参数，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列。在dump时将ensure_ascii设置为False，此时存入json的中文可正常显示。
                        # print('mq消息体body:\n{}'.format(body))
                        print('订单id:{},物流单号:{},电票mq消息体body:\n{}'.format(order_id, order_delivery_no, body))
                        canjie_dianpiao_mq_msg_list.append(body)
                        # send_mq_message(exchange, routing_key, queue, body)


'''
根据goodsSku查询商品相关属性
'''
# todo key:goodsSku,value:code
goodsSku_code_dict = {'DS000102': '1004', 'DS000098': '1004', 'DB000227': '1001'}
# key:goodsSku,value:价格
goodsSku_single_price = {'DS000102': 70.00, 'DS000098': 60.00, 'DB000227': 10120.00}
# key:goodsSku,value:发票服务名称
goodsSku_invoice_service_name = {'DS000102': '大益文学《呼唤》21-2', 'DS000098': '大益文学《所向》21-1', 'DB000227': '357g仓颉号生饼（2101）'}


def get_goods_properties_by_goodsSku(goodsSku, order_delivery_no):
    '''
    # with DB(host='172.17.180.11 ', port='30001', user='mall-operate',
    #         passwd='(MU$UjZ$0UYPT^0N',
    #         database='mall-operate') as db_order_conn:
    with DB(host='dev-sharding-m.tae-tea.net', port='3306', user='root',
            passwd='pP^EcsD$#KqTjksP',
            database='dev_mall_order_new') as db_order_conn:
        db_order = db_order_conn.cursor()
        #print('db_order_0:{}'.format(db_order))
        sql = "SELECT t1.name,t2.ordinary_card_price as goods_cost " \
              "from sdb_goods_info_basic t1,sdb_goods_product t2 WHERE t1.id= t2.goods_id AND t2.item_no = '%s'" % goodsSku
        db_order.execute(sql, None)
        result = db_order.fetchone()
        goodSku_product_id_dict = {}
        if result:
            goodSku_product_id_dict['code'] = '1001' #goodsSku_code_dict[goodsSku]
            goodSku_product_id_dict['name'] = result[0]#.decode('utf-8')
            goodSku_product_id_dict['percent'] = 100
            goodSku_product_id_dict['quantity'] = order_id_order_delivery_goods_product_no_goods_num_dict[goodsSku]
            goodSku_product_id_dict['taxPrice'] = float(result[1])
            goodSku_product_id_dict['totalAmount'] = float(result[1]) * float(
                order_id_order_delivery_goods_product_no_goods_num_dict[goodsSku])
            goodSku_product_id_dict['unit'] = goodsSku_unit_dict[goodsSku]
            # {"code": "1001", "name": "7572+7542（2001）", "percent": 100,
            #                       "quantity": 1, "taxPrice": 128, "totalAmount": 128, "unit": "对"}
        return goodSku_product_id_dict
    '''
    goodSku_product_id_dict = {'code': goodsSku_code_dict[goodsSku], 'lineType': '0','name': goodsSku_invoice_service_name[goodsSku],
                               'percent': 100.0, 'quantity': 1.0, 'taxPrice': float(goodsSku_single_price[goodsSku]),
                               'totalAmount': float(goodsSku_single_price[goodsSku]) * float(
                                   order_delivery_no_product_no_goods_num_dict[order_delivery_no][goodsSku]),
                               'unit': order_delivery_no_product_no_goods_unit_dict[order_delivery_no][goodsSku]}
    return goodSku_product_id_dict


'''发送rabbit mq消息'''


def send_mq_message(exchange, routing_key, queue, body):
    # 获取与rabbitmq 服务的连接，虚拟队列需要指定参数 virtual_host，如果是默认的可以不填（默认为/)，也可以自己创建一个
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='dev-mq-1.tae-tea.net', port=5672,
                                  credentials=pika.PlainCredentials('admin',
                                                                    'adm1n@Dl7w4r')))
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_publish(exchange=exchange, routing_key=routing_key,
                          properties=pika.BasicProperties(reply_to='order_invoice_flow_queue'), body=body)
    # 关闭连接
    connection.close()


if __name__ == '__main__':
    # 仓颉号sku
    product_no = 'DB000227PDH'
    # product_no = 'BH20S3S'
    get_orderId_by_sku(product_no)
    get_apply_order_invoice_info(cangjie_order_id_list)
    get_cangjie_delivered_order_delivery_no_by_order_id(apply_order_invoice_order_id)
    get_order_invoice_info(order_id_order_delivery_no_dict)
    with open('canjie_dianpiao_mq_msg_{}.csv'.format(time.strftime('%Y%m%d%H%M%S', time.localtime())), 'w',
              newline='') as f:
        for x in canjie_dianpiao_mq_msg_list:
            w = csv.writer(f, quotechar=' ')
            w.writerows([[x]])
    print('程序执行完毕')
