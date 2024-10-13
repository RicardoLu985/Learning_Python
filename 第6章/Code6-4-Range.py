"""
    系统提供的内置函数
    range(start,end,[step = -1]),生成一个等差序列[start,end)

    注意序列属于不可变序列、不支持元素修改，不支持运算（+ 或 *）操作。

    range一般用于for-in循环遍历。

    原型：range([start,]stop[,step])
    -range(stop)
    -range(start,stop)
    -range(start,stop,step)

    功能：生成列表
    参数：start：表示列表起始值。包含且默认为 0 。
         stop：表示列表结束值。不包含。
         step：步长，默认为 1 。
"""

print(list(range(10)))  # end
print(list(range(2,10)))  # start, end
print(list(range(2,10,3)))  # start, end, step

for i in range (3):
    print('hello')

# 高斯求和
total = 0
for i in range (101):
    total += i
print(total)

# 水仙花数：三位数，每一位数字的立方和等于数字本身。
for i in range (100,1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i % 10
    if  i == a ** 3 + b ** 3 + c ** 3:
        print(i)
# 优化
print('-'* 40)
for i in range (100,1000):
    t = str(i)
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])
    if  i == a ** 3 + b ** 3 + c ** 3:
        print(i)
