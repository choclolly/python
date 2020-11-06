import csv
import mysql.connector
import redis
import time
import uuid
import random

member_order = {}
member_id_and_pay_time = {}
vas_member_id = []
not_in_member_order = []

def get_read1(fileName):
    with open(fileName, encoding='utf-8') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            member_order[row[0]] = row[1]
        print(len(member_order))
        # for x in member_order:
        #     print(x + "," + member_order[x])


def get_read2(fileName):
    with open(fileName, encoding='utf-8') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            vas_member_id.append(row[0])
        print(len(vas_member_id))
        # for x in vas_member_id:
        #     print(x)


get_read1("D:\club_order_vas\order_star.csv")
get_read2("D:\club_order_vas\\vas_star.csv")

print(len(member_order) - len(vas_member_id))
for x in member_order:
    if vas_member_id.count(x) == 0:
        not_in_member_order.append(x)
print(len(not_in_member_order))
mvp_vas_id = 'b77752b48ae54c9ea7d9daf7f00692f6'
all_start_vas_id = 'd3a6eb59e2264efb91a165a0f5dec231'
for member_id in not_in_member_order:

    pay_time = member_order[member_id]
    member_id_and_pay_time[member_id] = pay_time
    print(pay_time)
    id = str(uuid.uuid4()).replace("-", "")
    vas_order_no = random.randint(0, 9999999999999999999)
    uc_vas_order_sql = "INSERT INTO uc_vas_order(`id`, `user_id`, `added_service_id`, `name`, `mobile`, `order_no`, `pay_no`, `pay_amount`, `pay_pt`, `pay_order_no`, `pay_type`, `currency`, `cur_rate`, `init_pay_time`, `finish_pay_time`, `notify_pay_time`, `pay_state`, `create_year`, `create_month`, `order_state`, `order_type`, `create_time`, `update_time`) VALUES " \
                       "(id, member_id, mvp_vas_id, NULL, NULL, vas_order_no, '', 0.00, '', '', '', NULL, NULL, NULL, NULL, NULL, '3', 2020, 9, '1', NULL, pay_time, pay_time);"
    uc_vas_record_sql = "INSERT INTO uc_vas_record(`id`, `user_id`, `added_service_id`, `invitation_code`, `begin_time`, `end_time`, `stop`, `invalid`, `create_time`, `update_time`, `order_no`) VALUES " \
                        "(id, member_id, mvp_vas_id, NULL, pay_time, 1632274994000, '0', '0', pay_time, pay_time, vas_order_no);"
    # if int(str(member_id)[-1]) % 2 == 0:
    #     print(uc_vas_order_sql)
    #     print(uc_vas_record_sql)
    # else:
    #     user_cursor_1.execute(uc_user_sql, na)
    #     user_cursor_1.execute(uc_account_sql, na)
    #     user_cursor_1.execute(uc_user_online_sql, na)
    #     user_1.commit()
