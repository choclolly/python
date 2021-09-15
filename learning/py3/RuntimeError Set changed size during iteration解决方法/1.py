'''
参考：
    https://blog.csdn.net/weixin_43848469/article/details/106470927
写代码的时候报了这样一个错，有一种非常简单的解决方法，因为一般是你 set 删除了一些东西，可以使用复制一个相同的集合进行循环，这样就不会报错了，比如
'''
order_delivery_no_set = set()

# 会报错 RuntimeError: Set changed size during iteration
for order_delivery_no in order_delivery_nos:
    order_delivery_nos.discard(order_delivery_no)

# order_delivery_nos.copy() 复制一个相同的集合进行循环
for order_delivery_no in order_delivery_nos.copy():
    order_delivery_nos.discard(order_delivery_no)
