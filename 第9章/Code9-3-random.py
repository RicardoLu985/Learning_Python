import random
# 随机小数，范围0~1
a = random.random()
print(a)

# 随机整数
b = random.randint(1,100)  # 闭区间
print(b)

# 获取列表中的随机元素
list1 = [1,2,3,4,5,6,7]
print(random.randint(list1[0],list1[len(list1)-1]))
print(random.choice(list1))
print(random.choice('hello world'))


print(ord('A'),ord('Z'))

# 生成一个随机大写字母的列表
a = []
n = 5
for i in range(20):
    s = ''
    for j in range(n):
        t = random.randint(65,90)
        s += chr(t)
    a.append(s)
print(a)

from my_package import my_tools
print(my_tools.random_string(6))

random.shuffle(list1)
print(list1)
