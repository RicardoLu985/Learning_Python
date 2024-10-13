# input()函数：输入指定内容
# 变量 = input('提示信息：')
# 输入即用代码获取用户通过键盘输入的信息。
# 用户输入的任何内容都会被认为是字符串。

# 任务1：创建变量name,保存用户输入的名字；打印变量name。

name = input("Enter your name: ")
print("欢迎%s来到Python的世界！" % name)

# 任务2：创建变量age，保存用户输入的年龄；打印用户的出生年份。
age = input("Enter your age: ")
# print(type(age))
# int()对输入的内容进行类型转换，才可以进行代数计算。
age = int(age)
# print(type(age))
year = 2024
# print(type(year))
print("您的出生年份是", year - age ,"年。",sep='')