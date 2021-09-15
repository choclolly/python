import requests, json, mysql.connector, time, uuid

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


'''
分页获取仓颉号订单 ID 列表
'''
cangjie_delivered_id_list = []


def get_cangjie_delivered_id():
    url = 'http://192.168.100.176:8011/oms-order-service/order/getOrderIdPage'
    param_dict = {'pageIndex': 1, 'pageSize': 1000000, 'markIdList': ['15720338721951744'], 'statusList': ['2000']}
    header_dict = {'Content-Type': 'application/json; charset=utf8', 'userId': '6485566782930945'}
    strMapA = json.dumps(param_dict)
    r = requests.post(url, data=strMapA, headers=header_dict)
    print(r.text)
    status_code = r.status_code  # 200
    # print(status_code)
    if status_code == 200:
        # 转字典
        resule_dict = json.loads(r.text)
        code = resule_dict['code']
        if code == 0:
            result = resule_dict['result']
            # print('返回code:{},返回结果result:{}'.format(code,result))
            if result:
                result_list = resule_dict['result']
                for x in result_list:
                    cangjie_delivered_id_list.append(x['id'])


'''
物流对应的物流类型
'''
logistic_dict = {'2866535282245633': 'JH_001'}

'''goodsku 字典'''
# goodsSku_mapping_goods_properties_dict_0 = {'product_id': '1bc141e3481b98c839296d4d023fc47e', 'product_no': 'BH18S4B',
#                                             'goods_no': 'BH18S4B',
#                                             'goods_cost': 0.00, 'sale_price': 0.00, 'prom_price': 0.00,
#                                             'member_price': 0.00, 'goods_unit': '片', 'goods_nums': '1',
#                                             'sale_type': '1', 'goods_weight': 0.00}
# # goodsSku 对应的商品属性
# goodSku_product_id_dict = {'DB000227': goodsSku_mapping_goods_properties_dict_0}
goodSku_product_id_dict = {}

'''
获取单个仓颉号订单详细信息
'''


def get_cangjie_order_get_by_id(id):
    url = 'http://192.168.100.176:8011/oms-order-service/order/get'
    param_dict = {'id': id}
    header_dict = {'Content-Type': 'application/json; charset=utf8', 'userId': '6485566782930945'}
    strMapA = json.dumps(param_dict)
    r = requests.post(url, data=strMapA, headers=header_dict)
    # print(r.text)
    status_code = r.status_code  # 200
    print(status_code)
    if status_code == 200:
        # 转字典
        resule_dict = json.loads(r.text)
        code = resule_dict['code']
        result = resule_dict['result']
        print('返回code:{},返回结果result:{}'.format(code, result))
        if code == 0:
            if result:
                # 会员收货信息
                receiveInfo = result['receiveInfo']
                print(receiveInfo)
                detailList = result['detailList']
                print(detailList)
                order_no = result['outOrderCode']
                order_delivery_no = result['outOrderCode']
                delivery_no = receiveInfo['waybillNo']
                receiver_name = receiveInfo['receiveName']
                receiver_phone = receiveInfo['receiveTel']
                receiver_address = receiveInfo['address']
                province_code = receiveInfo['provinceId']
                province = receiveInfo['provinceName']
                city_code = receiveInfo['cityId']
                city = receiveInfo['cityName']
                area_code = receiveInfo['areaId']
                area = receiveInfo['areaName']
                zip = receiveInfo['zipCode']
                company_id = result['companyId']
                company_name = result['companyName']
                logistic_type = logistic_dict[receiveInfo['logisticsId']]
                delivery_state = '1'
                create_time = int(time.time() * 1000)
                create_year = time.localtime(time.time()).tm_year
                create_month = time.localtime(time.time()).tm_mon
                '''
                根据订单编号获取商城订单信息
                '''
                # todo 订单库 写库需要分库
                with DB(host='dev-sharding-m.tae-tea.net', port='3306', user='dev_mall_order_new',
                        passwd='O8RzX#3mhbm0pDP7',
                        database='dev_mall_order_new') as db_order_conn:
                    db_order = db_order_conn.cursor()
                    print('db_order_0:{}'.format(db_order))
                    # 根据订单编号获取订单相关信息
                    sql = "SELECT id,member_id,member_name,member_no,member_phone,member_level,order_type,shop_id,shop_name,create_time FROM sdb_order WHERE order_no = '%s'" % order_no
                    db_order.execute(sql, None)
                    result = db_order.fetchone()
                    if result:
                        order_id = result[0].decode('utf-8')
                        member_id = result[1].decode('utf-8')
                        member_name = result[2].decode('utf-8')
                        member_no = result[3]
                        member_phone = result[4].decode('utf-8')
                        member_level = result[5].decode('utf-8')
                        order_type = result[6].decode('utf-8')
                        shop_id = result[7]
                        shop_name = result[8]
                        shipping_time = result[9]
                        print(
                            '订单order_id:{},编号order_no:{},类型order_type:{},的订单信息.member_id:{},member_name:{},member_no:{},'
                            'member_phone:{},member_level:{},shop_id:{},shop_name:{}'.format(
                                order_id, order_no, order_type, member_id, member_name, member_no, member_phone,
                                member_level,
                                shop_id, shop_name))
                        try:
                            '''查询发货单是否存在'''
                            query_sdb_order_delivery = "SELECT * FROM sdb_order_delivery WHERE order_no = '%s' AND member_id = '%s' and delivery_no = '%s'" % (
                                order_no, member_id, delivery_no)
                            db_order.execute(query_sdb_order_delivery, None)
                            result = db_order.fetchone()
                            if result:
                                print('用户member_id:{},订单编号:{},物流单号:{},的发货单已存在'.format(member_id, order_no,
                                                                                      delivery_no))
                                return
                            else:
                                '''insert 订单发货信息表'''
                                delivery_id = str(uuid.uuid1()).replace('-', '')
                                insert_sdb_order_delivery = "INSERT INTO `sdb_order_delivery`(" \
                                                            "`id`, `member_id`, `member_no`, `member_name`, `member_phone`, `order_delivery_no`, `member_level`, " \
                                                            "`order_id`, `order_no`, `receiver_name`, `receiver_phone`, `receiver_address`, `province_code`, `province`, " \
                                                            "`city_code`, `city`, `area_code`, `area`, `zip`, `receiver_days`, `receiver_times`, `shipping_time`, `delivery_type`, " \
                                                            "`company_id`, `company_name`, `logistic_type`, `delivery_no`, `delivery_state`, `sender_name`, `sender_phone`, " \
                                                            "`sender_address`, `is_confirm`, `create_time`, `update_time`, `create_year`, `create_month`, `express_content`, " \
                                                            "`order_type`, `shop_id`, `shop_name`, `create_id`, `create_name`, `update_id`, `update_name`, `delete_flag`) VALUES " \
                                                            "(%s, %s, %s, %s, %s, %s, %s, " \
                                                            "%s, %s, %s, %s, %s, %s, %s," \
                                                            "%s, %s, %s, %s, NULL, NULL, NULL, %s, NULL, " \
                                                            "%s, %s, %s, %s, %s, NULL, NULL, " \
                                                            "NULL, '0', %s, %s, %s, %s, NULL, " \
                                                            "%s, %s, %s, '', '', '', '', 0);"
                                na = (delivery_id, member_id, member_no, member_name, member_phone, order_delivery_no,
                                      member_level,
                                      order_id, order_no, receiver_name, receiver_phone, receiver_address,
                                      province_code, province,
                                      city_code, city, area_code, area, shipping_time,
                                      company_id, company_name, logistic_type, delivery_no, delivery_state,
                                      create_time, create_time, create_year, create_month,
                                      order_type, shop_id, shop_name)
                                db_order.execute(insert_sdb_order_delivery, na)
                                '''insert 发货单商品明细表'''
                                for x in detailList:
                                    goods_id = x['goodsId']
                                    goods_type = x['goodsCategoryId']
                                    goods_name = x['goodsName']
                                    goods_spec = x['goodsSpec']
                                    pay_amount = x['payment']
                                    goodsSku = x['goodsSku']
                                    goods_nums = x['goodsQty']
                                    goods_unit = x['goodsUnitName']
                                    # goodsWeight = x['goodsWeight']
                                    ID = str(uuid.uuid1()).replace('-', '')
                                    insert_sdb_order_delivery_goods = "INSERT INTO `sdb_order_delivery_goods`(" \
                                                                      "`id`, `member_id`, `member_no`, `member_name`, `member_phone`, `member_level`, `order_id`, `order_no`, `delivery_id`," \
                                                                      "`product_id`, `product_no`, `goods_id`, `goods_no`, `goods_type`, `goods_name`, `goods_cost`, `sale_price`, " \
                                                                      "`prom_price`, `member_price`, `goods_unit`, `goods_nums`, `sale_type`, `goods_spec`, `goods_size`, `goods_weight`, " \
                                                                      "`create_time`, `update_time`, `create_year`, `create_month`, `pay_amount`, `shop_id`, `shop_name`, `create_id`, " \
                                                                      "`create_name`, `update_id`, `update_name`, `delete_flag`) VALUES " \
                                                                      "(%s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                                                                      "%s, %s, %s, %s, %s, %s, 0.00, %s, " \
                                                                      "0.00, %s, %s, %s, NULL, %s, NULL, %s, " \
                                                                      "%s, %s, %s, %s, %s, %s, %s, '', " \
                                                                      "'', '', '', 0);"
                                    # todo 替换 goodsSku
                                    get_goods_properties_by_goodsSku('商品504950')
                                    na = (ID, member_id, member_no, member_name, member_phone, member_level, order_id,
                                          order_no, delivery_id,
                                          goodSku_product_id_dict['product_id'],
                                          goodSku_product_id_dict['product_no'], goods_id,
                                          goodSku_product_id_dict['goods_no'], goods_type, goods_name,
                                          goodSku_product_id_dict['ordinary_card_price'],
                                          goodSku_product_id_dict['ordinary_card_price'],
                                          goods_unit, goods_nums, goods_spec, goodSku_product_id_dict['weight'],
                                          create_time, create_time, create_year, create_month, pay_amount, shop_id,
                                          shop_name)
                                    db_order.execute(insert_sdb_order_delivery_goods, na)
                                '''update 订单表发货与订单状态'''
                                update_sdb_order = "update sdb_order set deliver_state='1',order_state='3',update_time=unix_timestamp(now())*1000 where order_no= '%s' AND deliver_state <>'1'AND order_state <> '3'" % order_no
                                db_order.execute(update_sdb_order, None)
                        except Exception as e:
                            print(e)
                            db_order_conn.rollback()
                    else:
                        print('订单编号order_no:{}的订单不存在'.format(orderNo))


'''
根据goodsSku查询商品相关属性
'''


def get_goods_properties_by_goodsSku(goodsSku):
    with DB(host='172.17.180.11 ', port='30001', user='mall-operate',
            passwd='(MU$UjZ$0UYPT^0N',
            database='mall-operate') as db_order_conn:
        db_order = db_order_conn.cursor()
        print('db_order_0:{}'.format(db_order))
        sql = "SELECT t1.item_no as goods_no,t2.id as product_id,t2.item_no as product_no,t2.ordinary_card_price as goods_cost,t2.weight " \
              "from sdb_goods_info_basic t1,sdb_goods_product t2 WHERE t1.id= t2.goods_id AND t2.item_no = '%s'" % goodsSku
        db_order.execute(sql, None)
        result = db_order.fetchone()
        if result:
            goodSku_product_id_dict['goods_no'] = result[0]
            goodSku_product_id_dict['product_id'] = result[1]
            goodSku_product_id_dict['product_no'] = result[2]
            goodSku_product_id_dict['ordinary_card_price'] = result[3]
            goodSku_product_id_dict['weight'] = result[4]


if __name__ == '__main__':
    get_cangjie_delivered_id()
    # for x in cangjie_delivered_id_list:
    #     get_cangjie_order_get_by_id(x)
    #get_cangjie_order_get_by_id('15833898300342272')
    # get_goods_properties_by_goodsSku('商品504950')
    print('程序执行完毕')
