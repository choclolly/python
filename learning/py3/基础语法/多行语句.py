"""
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
"""
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)

"""
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
"""
total = [item_one, item_two,
         item_three,
         ]
print(total)
