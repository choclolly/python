'''

已发货 && 订单状态是 已发货 or 交易完成的 && 申请了开局电票的 && 开具状态是 待开具 or 开具失败

product_no = 'DB000227PDH' 仓颉号商品goodsSku
deliver_state = 1           已发货
order_state in (3,4)        3- 已发货，4- 交易完成
invoice_type IN ('1','2')   1- 电票个人，2- 电票公司
invoice_state in (2,4)      2- 待开具，3- 已开具 . 4- 开具失败


select order_id FROM sdb_order_invoice
WHERE order_id IN
    (SELECT id
     FROM sdb_order
     WHERE id IN
         (SELECT order_id
          FROM sdb_order_goods
          WHERE product_no = 'DB000227PDH')
       AND deliver_state = 1
       AND order_state in (3,4) )
  AND invoice_type IN ('1',
                       '2') and invoice_state in (2,4)
'''



'1408610604359884802',
'1408610566825447425',
'1408610544742641666',
'1408610594601689089',
'1408610559141093378',
'1408610515151622145',
'1408610591432097793',
'1408610542356082690',
'1408610564376178689',
'1408610487640793090',
'1408610600247222273',
'1408610535873044481',
'1408610485337178113',
'1408610542796279810',
'1408610513211219970',
'1408610562777944065'