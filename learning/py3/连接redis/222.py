import redis

pool = redis.ConnectionPool(
    host="172.17.186.172", port=16379, password="rAW7kGqNeyMhlvGh", db='0',
    max_connections=1024)
conn = redis.Redis(connection_pool=pool)

print(conn)

key = 'MP-ACTIVITY:draw_lots:u_lucky_all:6fb553f5d670519db2f95b5fdb8fc79f' 

list  = conn.hvals(key)


print(type(list[0])) # <class 'bytes'>
s = list[0].decode('utf-8')
print(s)
print(type(s)) # <class 'str'>
dict = eval(s) # str ת dict
print(dict)
print("\'{}\'".format(dict['lotteryCode']['id']),end = ',')

'''
for x in list:
	s = x.decode('utf-8')
	dict = eval(s)
	print("\'{}\'".format(dict['lotteryCode']['id']),end = ',')
'''

	