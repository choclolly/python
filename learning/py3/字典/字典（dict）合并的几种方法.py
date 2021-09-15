# 参考 https://blog.csdn.net/weixin_33929309/article/details/89693777
'''
method 1 : 字典的update()方法
'''
dict1 = {'Bob': 70, 'Asia': 89}
dict2 = {'Sery': 80, 'Jony': 92}
dict3 = {}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)  # {'Bob': 70, 'Asia': 89, 'Sery': 80, 'Jony': 92}

'''
method 2 : 字典的dict(d1,**d2)方法 和 (**d1,**d2)方法
'''

dict4 = dict(dict1, **dict2)
print(dict4)    # {'Bob': 70, 'Asia': 89, 'Sery': 80, 'Jony': 92}

dict5 = {**dict1, **dict2}
print(dict5)    # {'Bob': 70, 'Asia': 89, 'Sery': 80, 'Jony': 92}