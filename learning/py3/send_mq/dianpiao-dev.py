import pika
import time


def send_message():
    # 获取与rabbitmq 服务的连接，虚拟队列需要指定参数 virtual_host，如果是默认的可以不填（默认为/)，也可以自己创建一个
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='dev-mq-1.tae-tea.net', port=5672,
                                                                   credentials=pika.PlainCredentials('admin',
                                                                                                     'adm1n@Dl7w4r')))
    # 创建一个 AMQP 信道（Channel）,建造一个大邮箱，隶属于这家邮局的邮箱
    channel = connection.channel()
    # 声明消息队列tester，消息将在这个队列传递，如不存在，则创建
    channel.queue_declare(queue='order_electronic_invoice_queue_test', durable=True)
    failNum = succNum = 0
    array = []
    with open('1.txt', 'r', encoding='utf-8') as lines:
        array = lines.readlines()

    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print("总计：%r，开始时间：%r" % (len(array), nowtime))

    for message in array:
        try:
            channel.basic_publish(exchange='port.notify.exchange_test', routing_key='order.electronic.invoice.queue',
                                  body=message, properties=pika.BasicProperties(reply_to='order_invoice_flow_queue'))
            succNum += 1
        except Exception as e:
            failNum += 1
            print("发送异常：" + message)
        time.sleep(2)  # 休眠1秒

    print("成功：%r，失败：%r，结束时间：%r" % (succNum, failNum, nowtime))
    # 关闭连接
    connection.close()


if __name__ == "__main__":
    send_message()
