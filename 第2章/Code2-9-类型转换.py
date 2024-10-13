# 数据类型转换
"""
    函数名             函数值
    int(x,[基数])    将数字或字符串转换为整数，如果x为浮点数，则自动截断小数部分
    float(x)        将x转换为浮点型
    bool(x)         转换成bool类型的True或False
    str(x)          将x转换成字符串
"""
# 转换成整数int
# 字符串str --> 整数int
# 纯数字的字符串
s = '2024'
n = int(s)
print(type(s),type(n))
# 浮点数float --> 整数int
s1 = 1.23
n1 = int(s1)
print(type(s1),type(n1))
# 布尔bool --> 整数int
s2,s3 = True,False
n2,n3 = int(s2),int(s3)
print(type(s2),type(n2))
print('*' * 40)

# 转换成浮点数float
# 字符串str --> 浮点数float
s = '12.34'
n = float(s)
print(type(s),type(n))  # 有没有小数点均可以转换
# 整数int --> 浮点数float
s1 = 100
n1 = float(s1)
print(type(s1),type(n1))
# 布尔bool --> 浮点数float
s2,s3 = True,False
n2,n3 = float(s2),float(s3)
print(type(s2),type(n2))
print('*' * 40)

# 转换成布尔bool
# 字符串str --> 布尔bool
s = 'asd123'
n = bool(s)
print(type(s),type(n))
st = ''  # 空串
print(bool(st))
st = ' '  # 空字符串
print(bool(st))
# 整数int --> 布尔bool
s1,s2 = 1,0
n1,n2 = bool(s1),bool(s2)
print(type(s1),type(n1))
# 浮点数float --> 布尔bool
s3 = 1.0
n3 = bool(s3)
print(type(s3),type(n3))
print('*' * 40)

# 转换成字符串str
# 整数int -- > 字符串str
n = 10
s = str(n)
print(type(n),type(s))
# 浮点数float -- > 字符串str
n1 = 12.0
s1 = str(n1)
print(type(n1),type(s1))
# 布尔bool -- > 字符串str
a = True
b = str(a)
print(type(a),type(b))

# 进制的转换
s = '1a'
n = int(s,16)
print(n)