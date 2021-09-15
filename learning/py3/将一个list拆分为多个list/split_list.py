
'''
参考 https://www.jianshu.com/p/a00e8dc922cb
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def split_list(list, size, newList=[]):
    if len(list) <= size:
        newList.append(list)
        return newList
    else:
        newList.append(list[:size])
        return split_list(list[size:], size)


l = split_list(list, 1)
for x in l:
    print(x)
