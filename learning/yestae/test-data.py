'''
已发货订单，模拟三批批物流
    个人电票
        1.未申请发票
            无消息
        2.第一批物流申请了电票
            {
                "custName": "dddddddddd",
                "custTaxNo": "",
                "custTelephone": "13100000011",
                "invoiceType": "1",
                "isRedFlag": false,
                "memberId": "1412960183862292481",
                "memberName": "T19380797",
                "memberNo": 1353124,
                "memberPhone": "15376727112",
                "orderId": "1412962980048715777",
                "orderNo": "1413024413990842370",
                "orders": [
                    {
                        "billNo": "1413024413990842370",
                        "items": [
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足1343",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 1,
                                "totalAmount": 2,
                                "unit": "把"
                            },
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足ticketFlag",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 2,
                                "totalAmount": 4,
                                "unit": "箱"
                            },
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足",
                                "percent": 100,
                                "quantity": 3,
                                "taxPrice": 2,
                                "totalAmount": 6,
                                "unit": "箱"
                            }
                        ]
                    }
                ],
                "platformType": "1",
                "receiverEmail": "q@qq.com"
            }
        2.1.第一批物流申请了电票，已开,同步第二批物流
            {
                "custName": "dddddddddd",
                "custTaxNo": "",
                "custTelephone": "13100000011",
                "invoiceType": "1",
                "isRedFlag": false,
                "memberId": "1412960183862292481",
                "memberName": "T19380797",
                "memberNo": 1353124,
                "memberPhone": "15376727112",
                "orderId": "1412962980048715777",
                "orderNo": "1413031042600976386",
                "orders": [
                    {
                        "billNo": "1413031042600976386",
                        "items": [
                            {
                                "code": "1001",
                                "name": "木兰组合",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 485,
                                "totalAmount": 970,
                                "unit": "把"
                            },
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足ticketFlag",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 3,
                                "totalAmount": 6,
                                "unit": "本"
                            }
                        ]
                    }
                ],
                "platformType": "1",
                "receiverEmail": "q@qq.com"
            }
        2.1.第一批物流申请了电票，已开,同步第二批物流,已开,同步第三批物流
            {
                "custName": "dddddddddd",
                "custTaxNo": "",
                "custTelephone": "13100000011",
                "invoiceType": "1",
                "isRedFlag": false,
                "memberId": "1412960183862292481",
                "memberName": "T19380797",
                "memberNo": 1353124,
                "memberPhone": "15376727112",
                "orderId": "1412962980048715777",
                "orderNo": "1413031042702438402",
                "orders": [
                    {
                        "billNo": "1413031042702438402",
                        "items": [
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足storeSaleFlag",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 2,
                                "totalAmount": 4,
                                "unit": "袋"
                            },
                            {
                                "code": "1001",
                                "name": "大益茶道研修服 男款 衬衣+围巾",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 385,
                                "totalAmount": 770,
                                "unit": "把"
                            },
                            {
                                "code": "1001",
                                "name": "商品基本信息3687",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 1,
                                "totalAmount": 2,
                                "unit": "袋"
                            }
                        ]
                    }
                ],
                "platformType": "1",
                "receiverEmail": "q@qq.com"
            }
        3.第一批物流未申请，第二批物流申请了电票，
            {
                "custName": "dddddddddd",
                "custTaxNo": "",
                "custTelephone": "13100000011",
                "invoiceType": "1",
                "isRedFlag": false,
                "memberId": "1412960183862292481",
                "memberName": "T19380797",
                "memberNo": 1353124,
                "memberPhone": "15376727112",
                "orderId": "1412962980048715777",
                "orderNo": "1413024413990842370",
                "orders": [
                    {
                        "billNo": "1413024413990842370",
                        "items": [
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足1343",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 1,
                                "totalAmount": 2,
                                "unit": "把"
                            },
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足ticketFlag",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 2,
                                "totalAmount": 4,
                                "unit": "箱"
                            },
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足",
                                "percent": 100,
                                "quantity": 3,
                                "taxPrice": 2,
                                "totalAmount": 6,
                                "unit": "箱"
                            }
                        ]
                    }
                ],
                "platformType": "1",
                "receiverEmail": "q@qq.com"
            }


            {
                "custName": "dddddddddd",
                "custTaxNo": "",
                "custTelephone": "13100000011",
                "invoiceType": "1",
                "isRedFlag": false,
                "memberId": "1412960183862292481",
                "memberName": "T19380797",
                "memberNo": 1353124,
                "memberPhone": "15376727112",
                "orderId": "1412962980048715777",
                "orderNo": "1413031042600976386",
                "orders": [
                    {
                        "billNo": "1413031042600976386",
                        "items": [
                            {
                                "code": "1001",
                                "name": "木兰组合",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 485,
                                "totalAmount": 970,
                                "unit": "把"
                            },
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足ticketFlag",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 3,
                                "totalAmount": 6,
                                "unit": "本"
                            }
                        ]
                    }
                ],
                "platformType": "1",
                "receiverEmail": "q@qq.com"
            }
        3.1第一批物流未申请，第二批物流申请了电票，同步第三批物流
            {
                "custName": "dddddddddd",
                "custTaxNo": "",
                "custTelephone": "13100000011",
                "invoiceType": "1",
                "isRedFlag": false,
                "memberId": "1412960183862292481",
                "memberName": "T19380797",
                "memberNo": 1353124,
                "memberPhone": "15376727112",
                "orderId": "1412962980048715777",
                "orderNo": "1413031042702438402",
                "orders": [
                    {
                        "billNo": "1413031042702438402",
                        "items": [
                            {
                                "code": "1001",
                                "name": "商品限购普金卡全满足storeSaleFlag",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 2,
                                "totalAmount": 4,
                                "unit": "袋"
                            },
                            {
                                "code": "1001",
                                "name": "大益茶道研修服 男款 衬衣+围巾",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 385,
                                "totalAmount": 770,
                                "unit": "把"
                            },
                            {
                                "code": "1001",
                                "name": "商品基本信息3687",
                                "percent": 100,
                                "quantity": 2,
                                "taxPrice": 1,
                                "totalAmount": 2,
                                "unit": "袋"
                            }
                        ]
                    }
                ],
                "platformType": "1",
                "receiverEmail": "q@qq.com"
            }
        4.第三批物流申请
            mq消息体body:
                {"custName": "dddddddddd", "custTaxNo": "", "custTelephone": "13100000011", "invoiceType": "1", "isRedFlag": false, "memberId": "1412960183862292481", "memberName": "T19380797", "memberNo": 1353124, "memberPhone": "15376727112", "orderId": "1412962980048715777", "orderNo": "1413024413990842370", "orders": [{"billNo": "1413024413990842370", "items": [{"code": "1001", "name": "商品限购普金卡全满足1343", "percent": 100, "quantity": 2.0, "taxPrice": 1.0, "totalAmount": 2.0, "unit": "把"}, {"code": "1001", "name": "商品限购普金卡全满足ticketFlag", "percent": 100, "quantity": 2.0, "taxPrice": 2.0, "totalAmount": 4.0, "unit": "箱"}, {"code": "1001", "name": "商品限购普金卡全满足", "percent": 100, "quantity": 3.0, "taxPrice": 2.0, "totalAmount": 6.0, "unit": "箱"}]}], "platformType": "1", "receiverEmail": "q@qq.com"}
            mq消息体body:
                {"custName": "dddddddddd", "custTaxNo": "", "custTelephone": "13100000011", "invoiceType": "1", "isRedFlag": false, "memberId": "1412960183862292481", "memberName": "T19380797", "memberNo": 1353124, "memberPhone": "15376727112", "orderId": "1412962980048715777", "orderNo": "1413031042600976386", "orders": [{"billNo": "1413031042600976386", "items": [{"code": "1001", "name": "木兰组合", "percent": 100, "quantity": 2.0, "taxPrice": 485.0, "totalAmount": 970.0, "unit": "把"}, {"code": "1001", "name": "商品限购普金卡全满足ticketFlag", "percent": 100, "quantity": 2.0, "taxPrice": 3.0, "totalAmount": 6.0, "unit": "本"}]}], "platformType": "1", "receiverEmail": "q@qq.com"}
            mq消息体body:
                {"custName": "dddddddddd", "custTaxNo": "", "custTelephone": "13100000011", "invoiceType": "1", "isRedFlag": false, "memberId": "1412960183862292481", "memberName": "T19380797", "memberNo": 1353124, "memberPhone": "15376727112", "orderId": "1412962980048715777", "orderNo": "1413031042702438402", "orders": [{"billNo": "1413031042702438402", "items": [{"code": "1001", "name": "商品限购普金卡全满足storeSaleFlag", "percent": 100, "quantity": 2.0, "taxPrice": 2.0, "totalAmount": 4.0, "unit": "袋"}, {"code": "1001", "name": "大益茶道研修服 男款 衬衣+围巾", "percent": 100, "quantity": 2.0, "taxPrice": 385.0, "totalAmount": 770.0, "unit": "把"}, {"code": "1001", "name": "商品基本信息3687", "percent": 100, "quantity": 2.0, "taxPrice": 1.0, "totalAmount": 2.0, "unit": "袋"}]}], "platformType": "1", "receiverEmail": "q@qq.com"}

'''
'''
    专票
        1.未申请发票
            无消息
        2.第一批物流申请了专票
            
'''