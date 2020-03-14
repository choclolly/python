"""
以下假设变量a为10，变量b为20：

运算符	            描述	                    实例
=	        简单的赋值运算符	            c = a + b 将 a + b 的运算结果赋值为 c
+=	        加法赋值运算符	            c += a 等效于 c = c + a
-=	        减法赋值运算符	            c -= a 等效于 c = c - a
*=	        乘法赋值运算符	            c *= a 等效于 c = c * a
/=	        除法赋值运算符	            c /= a 等效于 c = c / a
%=	        取模赋值运算符	            c %= a 等效于 c = c % a
**=	        幂赋值运算符	                c **= a 等效于 c = c ** a
//=	        取整除赋值运算符	            c //= a 等效于 c = c // a
:=	        海象运算符，
                可在表达式内部为变量赋值。
                Python3.8 版本新增运算符。在这个示例中，赋值表达式可以避免调用 len() 两次:
                                            if (n := len(a)) > 10:
                                                print(f"List is too long ({n} elements, expected <= 10)")
"""

# !/usr/bin/python3

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)