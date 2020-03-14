"""
当你指定一个值时，Number 对象就会被创建
您也可以使用del语句删除一些对象引用
    del语句的语法是：
        del var1[,var2[,var3[....,varN]]]
    可以通过使用del语句删除单个或多个对象。例如：
        del var
        del var_a, var_b
"""
print("======del语句")
var1 = 1
var2 = 100

print(var1, var2)
del var2
print(var1, var2)  # NameError: name 'var2' is not defined