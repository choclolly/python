"""
Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）
来截取字符串

如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
"""


def reverse(s):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    s = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    s = s[-1::-1]

    # 重新组合字符串
    output = ' '.join(s)

    return output


if __name__ == "__main__":
    s = 'I like runoob'
    rw = reverse(s)
    print(rw)

'''
runoob like I
'''
