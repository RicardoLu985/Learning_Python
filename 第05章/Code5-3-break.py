# break
"""
    作用：退出循环
    注意：只能跳出距离最近的for或者while循环。

    在循环过程中，如果某一个条件满足后，不在希望循环继续进行，可以使用break跳出循环。
"""

# while True:
#     name = input("请输入你的名字：")
#     if name == 'ricardo':
#         print("欢迎回家，",name,"！")
#         break
#     else:
#         print("Ricardo不在家，等下再来吧~")

# 判断一个数是否是质数
n = int(input("请输入需要判断的数字(n>1)："))
i = 2
flag = 0
while i < n:
    if n % i == 0 :
        print(n,"不是质数。")
        flag = 1
        break
    i = i + 1
else:
    print(n,"是质数。")


# from math import sqrt
# while True:
#     n = int(input("请输入需要判断的数字(n>1)："))
#     if n <= 1:
#         print("请输入大于2的数字。")
#         continue
#
#     is_prime = True
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print(n, "是质数。")
#         break
#     else:
#         print(n, "不是质数。")
