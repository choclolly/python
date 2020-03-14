import mysql.connector
'''
创建数据库连接
'''
mydb = mysql.connector.connect(
    host="59.110.228.110",  # 数据库主机地址
    port='3306',
    user="test_tea_uc_0",  # 数据库用户名
    passwd="L~+SJ*F^kon[t+10l6",  # 数据库密码
    database='test_tea_uc_0',
    buffered=True

)
mycursor = mydb.cursor()

print(mydb.server_port)
print(mydb.charset)

'''
创建数据库
    创建数据库使用 "CREATE DATABASE" 语句，以下创建一个名为 runoob_db 的数据库：
'''
# mydb = 连接mysql.connector.connect(
#     host="59.110.228.110",
#     user="test_tea_uc_0",
#     passwd="L~+SJ*F^kon[t+10l6",
#     buffered=True
# )
#
# mycursor = mydb.cursor()
# # 创建数据库前我们也可以使用 "SHOW DATABASES" 语句来查看数据库是否存在
# print(mycursor.execute("SHOW DATABASES"))
# mycursor.execute("CREATE DATABASE runoob_db")

'''
创建数据表
    方式一
        创建数据表
            mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
        主键设置：创建表的时候我们一般都会设置一个主键（PRIMARY KEY），我们可以使用 "INT AUTO_INCREMENT PRIMARY KEY" 语句
            来创建一个主键，主键起始值为 1，逐步递增。
            mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    方式二
        如果你还未创建 sites 表，可以直接使用以下代码创建。
        mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
'''
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

'''
插入数据
    插入数据使用 "INSERT INTO" 语句：
'''
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句
# 如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码
print(str(mycursor.rowcount) + " 条记录已插入, ID:", mycursor.lastrowid)

'''
批量插入
    批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
'''
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(str(mycursor.rowcount) + " 条记录已插入")

'''
查询数据
    查询数据使用 SELECT 语句：
'''
mycursor.execute("select * from sites limit 0,20")
# fetchall() 获取所有记录
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

'''
查询数据
    读取指定的字段数据
'''
mycursor.execute("SELECT name, url FROM sites")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
只想读取一条数据，可以使用 fetchone() 方法：
'''
mycursor.execute("SELECT name, url FROM sites")

myresult = mycursor.fetchone()

for x in myresult:
    print(x)

'''
where 条件语句
    如果我们要读取指定条件的数据，可以使用 where 语句：
'''
sql = "SELECT * FROM sites WHERE name ='RUNOOB'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
where 条件语句
    使用通配符 %
'''
sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
where 条件语句
    为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
'''
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)

mycursor.execute(sql, na)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
排序
    查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。
'''
sql = "SELECT * FROM sites ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
Limit
    如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定
'''
mycursor.execute("SELECT * FROM sites LIMIT 3")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
Limit
    指定起始位置，使用的关键字是 OFFSET：
'''
# 从第二条开始读取前 3 条记录：
mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''
删除记录
    删除记录使用 "DELETE FROM" 语句：
'''
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")

'''
注意：
    要慎重使用删除语句，删除语句要确保指定了 WHERE 条件语句，否则会导致整表数据被删除。
为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件：
'''
sql = "DELETE FROM sites WHERE name = %s"
na = ("stackoverflow",)

mycursor.execute(sql, na)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")

'''
更新表数据
    数据表更新使用 "UPDATE" 语句：
'''
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")

'''
注意：
    UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。
为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件：
'''
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("Zhihu", "ZH")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")

'''
删除表
    删除表使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除：
'''
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

mycursor.execute(sql)
