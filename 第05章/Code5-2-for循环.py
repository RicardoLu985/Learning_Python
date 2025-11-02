"""
    range()函数可以用来创建一个数字序列，
    常与for循环结合使用来重复执行代码块指定的次数。
"""
# 任务1：重复打印
for x in range(5):
    print("Hello,Python!")

# 任务2：高斯求和
result = 0
for i in range(101):
    result += i
print(result)

# 任务3：n阶乘的和 1！+ 2！+ 3！+...+n！

n = int(input("请输入n的值："))
count = 0
for x in range(n + 1):
    if x > 0:
        result = 1
        for i in range(x + 1):
            if i > 0:
                result *= i
        # print(result)
        count += result
print(count)

# 扩展
n = int(input("请输入n的值："))
count = 0
m = 1
while m <= n:
    result = 1
    a = 1
    while a <= m:
        result *= a
        a += 1
    count += result
    m += 1
print(count)
