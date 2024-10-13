# # 读取当前文件夹内的文件
# # 打开文件
# file1 = open('test.txt',encoding='utf-8')
#
# # 提取文件
# context = file1.read()
# print(context)
#
# # 关闭文件
# file1.close()
#
# print('-' * 80)
# # 读取其他文件夹内的文件
# # 打开文件
# file2 = open('../第9章/test2.txt',encoding='utf-8')
#
# # 提取文件
# context = file2.read()
# print(context)
#
# # 关闭文件
# file2.close()

print('-' * 80)
# 用绝对路径打开文件
import os
path = os.getcwd()  # 全称是 “get current working directory”。它用于获取当前的工作目录路径。
file1_path = path + '/test.txt'
file1 = open(file1_path,encoding='utf-8')
# context = file1.read()  # 写入参数的话就会读取指定字数。

# context = file1.readline()  # readline()每次读取文件的一行内容

context = file1.readlines()  # readlines()读取多行文件直至结束
print(context)

# import os
#
# # 分隔线
# print('-' * 80)
#
# # 用绝对路径打开文件
# path = os.getcwd()  # 获取当前的工作目录路径
# file1_path = os.path.join(path, 'test.txt')  # 使用 os.path.join 来拼接路径
#
# # 使用 with 语句打开文件
# with open(file1_path, encoding='utf-8') as file1:
#     context = file1.readlines()  # 读取多行文件直至结束
#
# # 打印读取的内容
# print(context)
