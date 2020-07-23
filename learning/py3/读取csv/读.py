# https://www.cnblogs.com/superhin/p/11495956.html
import csv

import csv

with open('result.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)