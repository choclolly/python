# https://www.cnblogs.com/superhin/p/11495956.html
import csv
from itertools import islice

# with open('result.csv', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in islice(reader, 1, None):
#         print(row)

'''
    读入csv跳过表头
        使用islice即可
    '''
with open('d://result.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in islice(reader, 1, None):
        print(row)
