# 纸的厚度
x = int(input("请输入对折的次数："))
n = 0.1
w = n
for i in range(x):
    w *= 2
print("对折%d次后，纸的厚度为%.2f毫米。" % (x, w))

# 国王麦粒
g = 1  # 当前格子麦粒数
total = 0  # 总麦粒数
b = int(input("请输入格子的个数："))  # 棋盘格子数目
a = 0
while a < b:
    total += g  # 计算当前总麦粒数
    a += 1  # 走到下一个格子
    g *= 2  # 当前格子应放麦粒数*2
print("在放满%d格子后，麦粒总数为%d个。" % (a, total))

# 人生的复利公式（1+0.01）
day = 0
n = int(input("请输入学习的天数："))
total  = 1
while day < n:
    total *= 1.01
    day += 1
print(total)