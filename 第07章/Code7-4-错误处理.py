# 运行，从错误信息中找到问题
# print(a)
# Traceback (most recent call last):
#   File "E:\Project01\第7章\Code7-4-错误处理.py", line 2, in <module>
#     print(a)
#           ^
# NameError: name 'a' is not defined

# 打印相关信息
for i in range(10):
    print('-' * 30)
    print(i)
    for j in range(5):
        print("内层循环")
        print('*'* j)

# 注释代码、逐行寻找
# 断点调试、单步执行
