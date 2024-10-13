# 集合（Set）
"""
    不允许有重复元素，如果添加重复元素，则会自动过滤，可以进行交集、并集的运算。
    是一种无序且无重复元素的数据结构。
    与dict类似，是一组key的集合（但不存储value）。
"""

# 集合的创建
s =set()
print(s, type(s))
s = {1,2,3,4,1,2}
print(s, type(s))

s = set( [1, 2, 3, 2])  # list --> set
print(s, type(s))
s = set((1, 2, 3, 4, 3))  # tuple --> set
print(s, type(s))
s = set('1232')  # str --> set
print(s, type(s))
s = set({1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f'})  # dict --> set
print(s, type(s))

# in
print( 1 in s)
# len
print(len(s))
# max/min
print(max(s), min(s))
# del
# 集合不支持索引
print('-' * 30)

# 集合的遍历
for i in s:
    print(i)

# 集合的常用方法
s.remove(1)
print(s)
s.update({1})
print(s)
s.add(9)
print(s)

# 交集、并集
s2 = {5,6,7,8,9}
print(s2)
print(s & s2)
print(s | s2)

# 列表去重
score = [80,70,60,80,70,60,40]
s = set(score)
print(s)
# 统计各个分数有几个学生
d = {}
for i in s:
    t = score.count(i)
    # print("得分为%d的学生有%d个人" % (i, t))
    d[i] = t
print(d)
for k,v in d.items():
    print("得分为%d的学生有%d个人" % (k, v))








