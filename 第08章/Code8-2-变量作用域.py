# 全局变量 & 局部变量
"""
    局部变量是在函数内部定义的变量，只能在函数内部使用。
    全局变量是在函数外部定义的变量，所有函数内部都可以使用这个变量。
"""

# 全局变量
num1 = 10  # 不可变数据类型
list1 = [1,2,3,4,5]  # 可变数据类型

def f():
    global num1  # 如果这里声明函数f用的num1是全局变量的num1，打印后的值也会被修改。
    num1 = 100
    num2 = 20  # 局部变量
    list1[2] = 9
    print("在函数f中，num1的值为", num1)
    print('num2的值为',num2)
    print("在函数f中，list1的值为", list1)

# print('num1的值为', num1)
f()

# print("在函数f外面num2的值为", num2)
# Traceback (most recent call last):
#   File "E:\Python01\第8章\Code8-2-变量作用域.py", line 17, in <module>
#     print("在函数f外面num2的值为", num2)
#                                    ^^^^
# NameError: name 'num2' is not defined. Did you mean: 'num1'?

# 局部变量不能再函数外面使用

print("在函数f外，num1的值为", num1)
print("在函数f外，list1的值为", list1)

"""
    函数中定义的变量作用域都只在此函数范围，函数可以直接调用全局变量；
    函数中定义变量和全局变量重名就会覆盖全局变量的值，但（函数结束后）无法修改全局变量的值。
"""