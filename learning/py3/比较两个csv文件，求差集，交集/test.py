# coding: gbk
import csv
from itertools import islice

# 读文件
csv_file = open('D:\\personal\\python\\比较两个csv文件，求差集，交集\\all-star.csv', 'r')
r= csv.reader(csv_file)

csv_file = open('D:\\personal\\python\\比较两个csv文件，求差集，交集\\mvp-star.csv', 'r')
r2= csv.reader(csv_file)

# 全明星/mvp 集合
s_all_star = set() 
s_mvp_star = set() 
for x in islice(r, 1, None):
	s_all_star.add(x[0])

for x in islice(r2, 1, None):
	s_mvp_star.add(x[0])

print(len(s_all_star))
print(len(s_mvp_star))

# 开通了s_all_star和s_mvp_star
s_all_and_mvp_star = s_all_star & s_mvp_star
print(len(s_all_and_mvp_star))
# 只开通了s_all_star
s_only_all_star = s_all_star - s_mvp_star
print(len(s_only_all_star))
# 只开通了s_mvp_star
s_only_mvp_star = s_mvp_star - s_all_star
print(len(s_only_mvp_star))


# 写文件
csv_s_all_and_mvp_star_file = open('D:\\personal\\python\\比较两个csv文件，求差集，交集\\s_all_and_mvp_star.csv', 'w')
w = csv.writer(csv_s_all_and_mvp_star_file)
w.writerow(['mobile'])
for x in s_all_and_mvp_star:
	w.writerows([[x]])

csv_s_only_all_star = open('D:\\personal\\python\\比较两个csv文件，求差集，交集\\s_only_all_star.csv', 'w')
w = csv.writer(csv_s_only_all_star)
w.writerow(['mobile'])
for x in s_only_all_star:
	w.writerows([[x]])

csv_only_mvp_star = open('D:\\personal\\python\\比较两个csv文件，求差集，交集\\s_only_mvp_star.csv', 'w')
w = csv.writer(csv_only_mvp_star)
w.writerow(['mobile'])
for x in s_only_mvp_star:
	w.writerows([[x]])
