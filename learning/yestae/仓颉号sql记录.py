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