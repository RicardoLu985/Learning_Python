# 字符串（String）
"""
    字符串就是一串字符，是编程语言中表示文本的数据类型。
    在Python中可以使用 “一对双引号” 或者 '一对单引号' 定义一个字符串；
    字符串是以单引号、双引号或是三引号引起来的任意文本。
"""
# 创建字符串
str1 = 'hello world!'
print(str1)

str2 = "hi baby!"
print(str2)

str3 = '''2024
hello world!'''
print(str3)

str4 = "It's an apple."
print(str4)

str5 = '123\'\"456'  #  \ 转义符
print(str5)

# 字符串运算
# 加法（字符串的拼接）
print('------------字符串拼接-------------')
print(str1 +' '+ str4 )
# 注意：字符串和数字不能相加

# 乘法（字符串的复制）
print(str1 * 2)
print('#' * 30)

# 索引
# 可以使用索引获取一个字符串中从指定位置的字符，索引计数从0开始。从右往左是-1开始。
# 以str1为例，0位是h，-1位是！
print(str1[0]+str1[-1])
# 切片
# 变量名[起始索引:结束索引+1:步数]
# 步数默认为1，可省略不写
# 起始索引默认为0，可省略不写
# 结束索引默认为列表或字符串长度，可省略不写
print(str1[0:4])  # 包头不包尾，冒号前是开始的位置，冒号后为结束的位数加一。
print(str1[0:9:2])  # 第三位参数表示间隔一位。
s = '123456789'
print(s[0:9:2])
print(s[::2])
# 字符串反转
print(s[-1:-10:-1])
print(s[::-1])
