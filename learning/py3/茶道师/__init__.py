import xlrd, xlwt, json, random, csv, uuid, time, re, mysql.connector
from itertools import islice


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


level_dict = {'III': 3, 'I': 1, 'II': 2}
education_dict = {"小学": 0, "初中": 1, "高中": 2, "大专": 3, "本科": 4, "硕士": 5, "研究生": 5, "博士": 6, "博士后": 7, "中专": 8,
                  "职中": 9,
                  "职高": 9, "中技": 8, "中职": 8}
sex_dict = {'男': 1, '女': 2, '女': 2}
belong_to_dict = {"集团分子公司": 1, "专营店": 2, "其他": 3}
nation_id_dict = {'彝': 7, '维': 5, '蒙古': 2, '拉祜': 24, '布朗': 34, '黎': 19, '朝鲜': 10, '藏': 4, '泰国': "", '苗': 6, '满': 11,
                  '傣': 18, '佤': 21, '毛南': 36, '回': 3, '布依': 9, '纳西': 27, '俄罗斯': 44, '壮': 8, '基诺': 56, '傈僳': 20, '瑶': 13,
                  '羌': 33,
                  '普米': 40, '土家': 15, '仡佬': 37, '侗': 12, '景颇': 28, '达': 31, '女': "", '穿青人': "", '哈尼': 16, '土': '',
                  '白': 14, '汉': 1, '畲': 22}
country_dict = {'泰国': 2, '俄罗斯': 3, '马来西亚': 4}
id_type_dict = {'身份证': 1, '港澳台': 2, '海外护照': 3, '其它': 4, '加拿大护照': 3}
nation_set = set()

tea_c_master_insert_sql_list = []
tea_c_master_level_insert_sql_list = []

id_num_tea_c_master_insert_sql_dict = {}
id_num_tea_c_master_insert_sql_id_num_tea_c_master_id_dict = {}


def get_sheet_info(file_path):
    # path = r'茶道师数据/2021.9开始初阶信息汇总.xlsx'
    path = file_path
    # 打开文件
    # wb = xlrd.open_workbook(r'b_feed.xlsx')
    wb = xlrd.open_workbook(path)
    # 获取所有sheet
    sheet_names = wb.sheet_names()
    # print(sheet_names)  # ['精确猜中-4人', '未精确猜中-211人']
    sheet = wb.sheet_by_name('Sheet1')
    print('sheet名称:{}\n有效数据行:{}\n有效数据列:{}'.format(sheet.name, sheet.nrows, sheet.ncols))
    # time.sleep(5)
    # 输出第一行的所有值
    # print(sheet.row_values(0))  # ['_id', 'user_id', 'mobile', 'content', 'createTime']
    # 将数据和标题组合成字典
    # print(dict(zip(sheet.row_values(0), sheet.row_values(1))))

    # 构造迭代器
    iter_row_num = iter(range(sheet.nrows))
    # 2.跳过第一行读取表格
    for i in islice(iter_row_num, 1, None):
        # print(type(sheet.row_values(i))) # <class 'list'>
        row = sheet.row_values(i)
        row_num = i
        # print(row)
        # 阶位信息
        level = str(row[0])
        level = re.sub(' ', '', level)
        level = level.replace('\n', '').replace('\r', '')
        level = level_dict[level]
        number = str(row[1]).split('.')[0]
        # 字符串日期 转 13位时间戳
        issue_date = row[3]
        time_array = time.strptime(issue_date, '%Y.%m.%d')
        issue_date = int(time.mktime(time_array)) * 1000

        # 茶道师信息
        name = row[4]
        name = re.sub(' ', '', name)
        name = name.replace('\n', '').replace('\r', '')
        sex = row[5]
        if len(sex) > 0:
            # print(sex)
            # print(name)
            sex = sex_dict[re.sub(' ', '', sex.strip())]
            # print(sex)
        else:
            sex = 'NULL'
        # else:
        #     print(sex)
        #     print(row) 肖宪坚
        id_type = row[6]
        if len(id_type) > 0:
            id_type = id_type_dict[id_type]
        else:
            id_type = 4
        id_num = str(row[7])
        if len(id_num) > 0:
            id_num = str(row[7]).split('.')[0]
            id_num = re.sub(' ', '', id_num)
            id_num = id_num.replace('\n', '').replace('\r', '')
        else:
            id_num = 'NULL'

        # country = 0
        # todo 民族
        nation_id = row[8]
        # todo 有三条数据 需要确认是那个民族   土家族 or 土族
        # if nation_id == '土':
        #     print(nation_id)
        if len(nation_id) > 0:
            # nation_set.add(nation_id.strip())
            # print(nation_id)
            nation_id = nation_id_dict[nation_id.strip()]
        mobile = str(row[9]).split('.')[0]
        mobile = re.sub(' ', '', mobile)
        mobile = mobile.replace('\n', '').replace('\r', '')
        education = row[10]
        if len(education) > 0:
            education = education_dict[re.sub(' ', '', education)]
        else:
            education = 'NULL'
        belong_to = row[11]
        if len(belong_to) > 0:
            belong_to = belong_to_dict[re.sub(' ', '', belong_to)]
        else:
            belong_to = 3
        corporate_name = row[12]
        corporate_name = re.sub(' ', '', corporate_name)
        corporate_name = corporate_name.replace('\n', '').replace('\r', '')
        auth_no = row[13]
        tea_c_master_remark = row[14]
        # todo 省市县街道 id code
        province = row[15]
        province_code = ''
        city = row[16]
        city_code = ''
        area = row[17]
        area_code = ''
        address = row[18]
        if len(address) > 0:
            address = re.sub(' ', '', address)
            address = address.replace('\n', '').replace('\r', '')
        email = str(row[19])
        if len(email):
            email = re.sub(' ', '', email)
            email = email.replace('\n', '').replace('\r', '')
        country = row[21]
        if len(country) > 0:
            country = country_dict[country]
        else:
            country = 0
        tea_c_master_level_remark = row[22]
        if len(province) > 0:
            province_code = get_code(province)
            # print(province_code)
        if len(city) > 0:
            city_code = get_code(city)
            # print(city_code)
        if len(area) > 0:
            area_code = get_code(area)
            # print(area_code)

        # print('行号:{},阶位:{},证书号码:{},发证日期:{},姓名:{},性别:{},证件类型:{},证件号码:{},国家:{},民族:{}'
        #       ',手机号:{},学历:{},渠道:{},公司名称:{},授权牌号:{},茶道师备注:{}省:{},省code:{},市:{},市code:{},区:{},区code:{},详细地址:{},邮箱:{},'
        #       '阶位备注:{}'.format(row_num, level, number, issue_date, name, sex,
        #                        id_type, id_num,
        #                        country, nation_id, mobile, education,
        #                        belong_to, corporate_name, auth_no, tea_c_master_remark,
        #                        province, province_code, city, city_code, area, area_code, address, email,
        #                        tea_c_master_level_remark))
        #

        create_time = int(time.time() * 1000)
        id1 = str(uuid.uuid4()).replace('-', '')
        tea_c_master_insert_sql = "INSERT INTO `tea_c_master`.`tea_c_master`" \
                                  "(`id`, `member_id`, `name`, `sex`, `country`, " \
                                  "`nation_id`, `education`, `province_id`, `province_code`, `province`, `city_id`, `city_code`, `city`, `area_id`, `area_code`, `area`, `town_id`, `town_code`, `town`, `address`, " \
                                  "`id_type`, `id_num`, `mobile`, `email`, `belong_to`, `corporate_name`, `auth_no`, `remark`, " \
                                  "`max_level`, `create_name`, `update_name`, `create_time`, `update_time`, `delete_flag`) " \
                                  "VALUES " \
                                  "('%s', NULL, \"%s\", %s, %s, " \
                                  "'%s', %s, NULL, '%s', '%s', NULL, '%s', '%s', NULL, '%s', '%s', NULL, NULL, NULL, \"%s\", " \
                                  "%s, '%s', '%s', '%s', %s, '%s', '%s', '%s', " \
                                  "NULL, '系统', NULL, %s, NULL, 0);" \
                                  % (id1, name, sex, country,
                                     nation_id, education, province_code, province, city_code, city, area_code, area,
                                     address,
                                     id_type, id_num, mobile, email, belong_to, corporate_name, auth_no,
                                     tea_c_master_remark,
                                     create_time)
        # print(tea_c_master_insert_sql)

        # id_num 相同的视为同一个人，需要过滤数据
        keys = id_num_tea_c_master_insert_sql_dict.keys()
        if id_num not in keys:
            id_num_tea_c_master_insert_sql_dict[id_num] = tea_c_master_insert_sql
            id_num_tea_c_master_insert_sql_id_num_tea_c_master_id_dict[id_num] = id1
        else:
            id1 = id_num_tea_c_master_insert_sql_id_num_tea_c_master_id_dict[id_num]

        id2 = str(uuid.uuid4()).replace('-', '')
        tea_c_master_level_insert_sql = "INSERT INTO `tea_c_master`.`tea_c_master_level`" \
                                        "(`id`, `tea_c_master_id`, `name`, `mobile`, `level`, `id_num`, `number`, `image`, `remark`, `issue_date`, " \
                                        "`create_name`, `update_name`, `create_time`, `update_time`, `delete_flag`) " \
                                        "VALUES " \
                                        "('%s', '%s', \"%s\", '%s', %s, '%s', '%s', NULL, '%s', %s, " \
                                        "'%s', NULL, %s, NULL, 0);" \
                                        % (id2, id1, name, mobile, level, id_num, number, tea_c_master_level_remark,
                                           issue_date,
                                           '系统', create_time)
        # print(tea_c_master_level_insert_sql)

        # todo sql 写入文件
        # sql_list.append(tea_c_master_insert_sql)
        tea_c_master_level_insert_sql_list.append(tea_c_master_level_insert_sql)


def get_code(name):
    with DB(host='192.168.100.153', port='3306', user='root', passwd='lb,LtawoFcd.eV@J',
            database='tea_c_master') as db_teac_conn:
        db_teac = db_teac_conn.cursor()
        # print('db_order_0:{}'.format(db_order))
        sql = "SELECT code FROM sys_city where name = '%s'" % name
        db_teac.execute(sql, None)
        # print(sql)
        result = db_teac.fetchone()
        if result:
            province_code = result[0]
            return province_code
        else:
            return 'NULL'


if __name__ == '__main__':
    beginTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("开始时间：%r" % beginTime)
    start = time.perf_counter()

    path1 = '茶道师数据/2021.9开始初阶信息汇总.xlsx'
    path2 = '茶道师数据/2028-2021.8初阶汇总.xlsx'
    path3 = '茶道师数据/2028-2021二阶信息汇总.xlsx'
    path4 = '茶道师数据/2019.12.24三阶.xlsx'


    # 分开写入文件
    # i = 0
    #
    # get_sheet_info(path1)
    # # 写入文件
    # with open('{}_{}.txt'.format(path1.split('/')[1][:-5], time.strftime('%Y%m%d%H%M%S', time.localtime())), mode='w',
    #           encoding='utf-8') as f:
    #     for x in tea_c_master_level_insert_sql_list:
    #         f.write(x + '\n')
    # i = i + len(tea_c_master_level_insert_sql_list)
    # tea_c_master_level_insert_sql_list.clear()
    #
    # get_sheet_info(path2)
    # # 写入文件
    # with open('{}_{}.txt'.format(path2.split('/')[1][:-5], time.strftime('%Y%m%d%H%M%S', time.localtime())), mode='w',
    #           encoding='utf-8') as f:
    #     for x in tea_c_master_level_insert_sql_list:
    #         f.write(x + '\n')
    # i = i + len(tea_c_master_level_insert_sql_list)
    # tea_c_master_level_insert_sql_list.clear()
    #
    # get_sheet_info(path3)
    # # 写入文件
    # with open('{}_{}.txt'.format(path3.split('/')[1][:-5], time.strftime('%Y%m%d%H%M%S', time.localtime())), mode='w',
    #           encoding='utf-8') as f:
    #     for x in tea_c_master_level_insert_sql_list:
    #         f.write(x + '\n')
    # i = i + len(tea_c_master_level_insert_sql_list)
    # tea_c_master_level_insert_sql_list.clear()
    #
    # get_sheet_info(path4)
    # # print(len(id_num_tea_c_master_insert_sql_dict.values()))
    # # print(type(id_num_tea_c_master_insert_sql_dict.values()))
    # for x in id_num_tea_c_master_insert_sql_dict.values():
    #     # print(type(x))
    #     tea_c_master_insert_sql_list.append(x)
    #
    # # 写入文件
    # with open('{}_{}.txt'.format(path4.split('/')[1][:-5], time.strftime('%Y%m%d%H%M%S', time.localtime())), mode='w',
    #           encoding='utf-8') as f:
    #     for x in tea_c_master_level_insert_sql_list:
    #         f.write(x + '\n')
    # i = i + len(tea_c_master_level_insert_sql_list)
    #
    # # 写入文件
    # with open('tea_c_master_insert_sql_{}.txt'.format(time.strftime('%Y%m%d%H%M%S', time.localtime())),
    #           mode='w',
    #           encoding='utf-8') as f:
    #     for x in tea_c_master_insert_sql_list:
    #         f.write(x + '\n')
    #
    #
    # print("茶道师信息数：%r " % len(tea_c_master_insert_sql_list))
    # print("茶道师阶位信息数：%r " % i)
    # print("总计：%r " % (i + len(tea_c_master_insert_sql_list)))

    # print(nation_set)

    # 写入一个文件
    get_sheet_info(path1)
    get_sheet_info(path2)
    get_sheet_info(path3)
    get_sheet_info(path4)

    for x in id_num_tea_c_master_insert_sql_dict.values():
        # print(type(x))
        tea_c_master_insert_sql_list.append(x)

    print("总计：%r " % (len(tea_c_master_insert_sql_list) + len(tea_c_master_level_insert_sql_list)))
    # list 合并 参考 https://www.cnblogs.com/ray-bk/p/12916911.html
    sql_list = tea_c_master_insert_sql_list + tea_c_master_level_insert_sql_list
    print("总计：%r " % (len(sql_list)))
    # 写入文件
    with open('all_{}.txt'.format(time.strftime('%Y%m%d%H%M%S', time.localtime())), mode='w', encoding='utf-8') as f:
        for x in sql_list:
            f.write(x + '\n')
    print('程序执行完毕')
    endime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    end = time.perf_counter()
    print("结束时间：%r,The function run time is : %.03f seconds" % (endime, end - start))


    '''
    分开写入文件
        开始时间：'2022-01-24 20:08:41'
        sheet名称:Sheet1
        有效数据行:836
        有效数据列:23
        sheet名称:Sheet1
        有效数据行:7386
        有效数据列:23
        sheet名称:Sheet1
        有效数据行:4621
        有效数据列:23
        sheet名称:Sheet1
        有效数据行:413
        有效数据列:23
        茶道师信息数：9410 
        茶道师阶位信息数：13252 
        总计：22662 
        程序执行完毕
        结束时间：'2022-01-24 20:12:16',The function run time is : 215.167 seconds
    写入一个文件
        开始时间：'2022-01-24 20:35:03'
        sheet名称:Sheet1
        有效数据行:836
        有效数据列:23
        sheet名称:Sheet1
        有效数据行:7386
        有效数据列:23
        sheet名称:Sheet1
        有效数据行:4621
        有效数据列:23
        sheet名称:Sheet1
        有效数据行:413
        有效数据列:23
        总计：22662 
        总计：22662 
        程序执行完毕
        结束时间：'2022-01-24 20:38:58',The function run time is : 235.522 seconds
    '''
