# 字符串（String）
"""
    字符串就是一串字符，是编程语言中表示文本的数据类型。
    在Python中可以使用一对双引号 "" 或一对单引号 '' 定义一个字符串。
    字符串是以单引号或者双引号括起来的任意文本，也可以是以三引号''' '''或者""" """ 引起来的任意文本。
    
    运算：加法和乘法
    
    索引：可以使用索引获取一个字符串中指定位置的字符，索引计数从0开始。
"""
s1 = 'hello world     '

# 序列的通用操作
print(s1 + ' 师姐')
print(s1 * 3)
print(len(s1))
print(max(s1),min(s1))
print(ord('w'),ord(' '))  # ord() 是ASCII码值函数
# del s1
print('s' in s1)
print('abs' < 'absd')
print('cd' < 'ab')

# 字符串的遍历
for i in s1:
    print(i)

for index, value in enumerate(s1):
    print(index, value)

for i in range(len(s1)):
    print(i,s1[i])

# 类型转换
print(str(12),type(str(12)))  # int --> str
print(str([1,2,3]),type(str([1,2,3])))  # list --> str
print(str(1,),type(str(1,)))  # tuple --> str

# 常用方法
print(s1.islower())  # 判断是否小写
print(s1.isupper())  # 判断是否小写
print(s1.count('o'))  # 统计字母个数
print(s1.find('o'))  # 找到第一个'o'
print(s1.strip())  # 去空格
print(s1.split(' '))  # 以 ' ' 作为分隔符
print(s1.split())
print('#'.join(s1.split()))

# 字符串统计
s = input("请输入一篇文章：")
# 字母、数字、符号统计个数
a = b = c = 0
for i in s:
    if i.isalpha():
        a += 1
    elif i.isdigit():
        b += 1
    else:
        c += 1
print(a,b,c)
