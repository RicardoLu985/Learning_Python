# 元组的创建
tuple1 = (1,2,3,True,'hello')
print(tuple1)
print(type(tuple1))

tuple2 = (1 ,)  # 元组里只有一个元素时，需要再末端加一个括号。
print(tuple2)
print(type(tuple2))

tuple3 = tuple()
print(tuple3)
print(type(tuple3))

tuple4 = ()
print(tuple4)
print(type(tuple4))

# 类型转换
tuple5 = tuple('hello')  # str --> tuple
print(tuple5)

tuple6 = tuple([1,2,3])  # list --> tuple
print(tuple6)

list1 = list(tuple6)
print(list1)

str1 = str(tuple6)
print(str1)
print(type(str1))
print(str1[0])

# 序列的通用操作
print('-'* 40)
# 索引
print(tuple1[2])
# 切片
print(tuple1[::-1])
# 函数
print(len(tuple1))
print(max(tuple6),min(tuple6))
# 删除
# del tuple5
# +
print(tuple1 + tuple5)
# *
print(tuple1 * 3)
# in
print(1 in tuple1)

# 元组的常用方法
a = tuple1.count('hello')  # 元素计数
print(a)
b = tuple1.index('hello')  # 元素索引
print(b)

# 元组的遍历
print('-'* 40)
for i in tuple1:
    print(i)

for value,index in enumerate(tuple1):
    print(value,index)

for i in range(0,len(tuple1)):
    print(i,tuple1[i])
