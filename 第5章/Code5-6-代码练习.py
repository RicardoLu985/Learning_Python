# 打印四行五列
m = 4
n = 5
for i in range(m):
    for j in range(n):
        print('* ', end='')
    print()

# 打印等腰三角形
n = 3
a = 1
b = n - 1
for i in range(n):
    print(' '* b + '*' * a, end='')
    a = a + 2
    b = b - 1
    print()

"""
    每行星形数为 2n-1 个，需要的空格为 (2n-1-1)/2 = n-1 个。
    i 和 a、b的关系：
    i = 0, b = n-1, a = 1
    i = 1, b = n-2, a = 3
    i = 2, b = n-3, a = 5
    ...
    所以：
    b = n-1-i，a = i * 2 +1
"""
# 优化
n = 3
for i in range(n):
    print(' '* (n-1-i) + '*' * (i * 2 + 1), end='')
    print()

# 小猴吃桃（穷举法）
peach = 1
while True:
    d1 = peach // 2 - 1
    d2 = d1 // 2 - 1
    d3 = d2 // 2 - 1
    d4 = d3 // 2 - 1
    if d4 == 1:
        print(peach)
        break
    peach += 1








