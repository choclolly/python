# coding: gbk
import csv
from itertools import islice

# ���ļ�
csv_file = open('D:\\personal\\python\\�Ƚ�����csv�ļ�����������\\all-star.csv', 'r')
r= csv.reader(csv_file)

csv_file = open('D:\\personal\\python\\�Ƚ�����csv�ļ�����������\\mvp-star.csv', 'r')
r2= csv.reader(csv_file)

# ȫ����/mvp ����
s_all_star = set() 
s_mvp_star = set() 
for x in islice(r, 1, None):
	s_all_star.add(x[0])

for x in islice(r2, 1, None):
	s_mvp_star.add(x[0])

print(len(s_all_star))
print(len(s_mvp_star))

# ��ͨ��s_all_star��s_mvp_star
s_all_and_mvp_star = s_all_star & s_mvp_star
print(len(s_all_and_mvp_star))
# ֻ��ͨ��s_all_star
s_only_all_star = s_all_star - s_mvp_star
print(len(s_only_all_star))
# ֻ��ͨ��s_mvp_star
s_only_mvp_star = s_mvp_star - s_all_star
print(len(s_only_mvp_star))


# д�ļ�
csv_s_all_and_mvp_star_file = open('D:\\personal\\python\\�Ƚ�����csv�ļ�����������\\s_all_and_mvp_star.csv', 'w')
w = csv.writer(csv_s_all_and_mvp_star_file)
w.writerow(['mobile'])
for x in s_all_and_mvp_star:
	w.writerows([[x]])

csv_s_only_all_star = open('D:\\personal\\python\\�Ƚ�����csv�ļ�����������\\s_only_all_star.csv', 'w')
w = csv.writer(csv_s_only_all_star)
w.writerow(['mobile'])
for x in s_only_all_star:
	w.writerows([[x]])

csv_only_mvp_star = open('D:\\personal\\python\\�Ƚ�����csv�ļ�����������\\s_only_mvp_star.csv', 'w')
w = csv.writer(csv_only_mvp_star)
w.writerow(['mobile'])
for x in s_only_mvp_star:
	w.writerows([[x]])
