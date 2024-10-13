"""
    List是Python中使用最频繁的数据类型，在其他语言中通常叫做数组。
    专门用于存储一串信息。
    列表用[]定义，数据之间使用 , 分隔
    列表的索引从 0 开始
    索引就是数据在列表中位置的编号，索引又可以称为下标
    注意：从列表中取值是，如果超出索引范围，程序会报错。
"""
"""
    语法：
    列表名 = [元素1,元素2,...]
"""
# 列表的创建
list1 = []  # 空列表
print(list1)
print(type(list1))
list2 = [1,2,3,'hello']
print(list2)
list3 = list('hello')  # 类型转换：把参数转换成列表  str --> list
print(list3)

# 列表的索引
print(list3[1])

# 列表的加法和乘法
print(list3 + list2)
print(list3 * 2)

# 列表的成员运算
print('h' in list3)
print('a' not in list3)

# 内置函数 函数名()
print(len(list3))  # 求元素个数
print(max(list3))  # 求元素最大值
print(min(list3))  # 求元素最小值

# del list3  # 删除变量
print('*' * 20)

# 列表的遍历
for i in list2:
    print(i)
for i,j in enumerate(list2):  #enumerate 枚举
    print(i,j)
for i in range(len(list2)):
    print(i,list2[i])
print('*' * 20)

# 列表的常用方法method  变量.方法名()
# 添加元素
list3.append('666')
print(list3)

# 添加列表
list3.extend([1,2,3])
print(list3)

# 插入元素
list3.insert(0,'999')
print(list3)

# 根据索引删除元素
list3.pop(3)
print(list3)
# 根据值删除元素
list3.remove('e')
print(list3)
"""
    删除索引小的值，即删除找到的第一个值。
"""
# 清空列表
list3.clear()
print(list3)






