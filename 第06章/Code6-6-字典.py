# 字典（dict）
"""
    dictionary(字典)是除列表以外，Python之中最灵活的数据类型。
    字典同样可以存储多个数据，通常用于存储描述一个物体的相关信息
    和列表的区别：
        列表是有序对象的集合
        字典是无序对象的集合
    字典用{}定义
    字典使用 键值对 存储数据，键值对之间使用 , 分隔
    键key 是索引
    值value 是数据
    键 和 值 之间使用 : 分隔
    键必须是唯一的
    值可以取任意数据类型，但键只用用 字符串、数字、或元组。
"""

# 字典的创建
d =  {
    'name' : '阿山' ,  # 键值对
    'gender' : True ,  # 末尾写不写逗号都可以。
    # 'name' : 'jack'   # 键重复的话，会覆盖前面的值。
}
print(d)
# print(type(d))
# d = {}
# print(d)
# print(type(d))
# d = dict()
# print(d, type(d))

# 新增键值对
d['height'] = 170
print(d)

# 获取键值对
print(d['height'])

# 修改键值对
d['name'] = 'shen'
print(d)

# del d

# in
print('age' in d)

# 字典的遍历
for i in d:
    print(i,d[i])
print('-' * 30)

print(d.items())
for key,value in d.items():
    print(key,value)

for k in d.keys():
    print(k)
for v in d.values():
    print(v)

# 字典的常用方法
d.pop('name')
print(d)
a = d.copy()
print('a 的键值对', a )
b = d.get('gender')
print(b)
d.popitem()  # 弹出最后的键值对
print(d)
d.update({'age': 18})
# d.clear()  # 清空键值对
print(d)
