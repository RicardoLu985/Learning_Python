# 函数的定义
"""
    使用关键字def
    确定函数名称、参数名称、参数个数、编写函数体（用于实现函数功能的代码）
"""


def func(n):  # n 为形式参数
    print('python.--' * n)  # 注意缩进


# 函数的调用
"""
    通过函数名称进行调用函数
    定义函数，只表示此函数封装完成代码。
    需要主动调用函数，函数才会执行。
"""

func(2)  # 函数名称+()，即可调用。 2 为实际参数
# 先定义，再调用。定义和调用之间默认空两行。

# 函数的参数
"""
    形参：函数定义时小括号里的参数，是用来接收参数用的，在函数内部作为变量使用。
    实参：函数调用的时候，小括号里的参数，是把数据传递到函数内部用的。
    函数可以没有形参和实参。
"""

# 函数的返回值
"""
    返回值是函数完成工作后，最后给调用者的一个结果。
    在函数中使用 return 关键字可以返回结果。
    调用函数的一方，可以使用变量来接收函数的返回结果。
"""

def sum2(a, b):
    return a + b


result = sum2(5, 4)
print(result)

# 位置参数
# 要求实参顺序必须和形参顺序完全一致，由形参顺序决定实参顺序。

# 缺省参数
# 定义函数时，可以给某个参数指定一个默认值，具有默认值的参数即为缺省参数。

def power(x, n=2):  # n 的默认值为2
    return x ** n


print(power(2))
print(power(2, 5))

def infos(name,  age, gender):
    return "大家好，我叫%s，我今年%d岁了，我是一名%s生" % (name, age, gender)


s = infos("阿山",16,"男")
print(s)

# 可变参数
# 传入的参数个数是可变的，可以是0个或多个。

a = [1,2,3,4,5]
result = 0
for i in a:
    result += i
print(result)

def total(*args):  # 可变参数 tuple
    result = 0
    for i in args:
        result += i*i
    return result


print(total(1,2,3,4,5))

# 如果传入的是字典，需要加上*。
b = [1,2,3,4,5]
print(total(*b))


def f(**kwargs):  # 可变参数，接收字典
    for k, v in kwargs.items():
        print(k, v)


d = {
    'name' : 'amei',
    'age' : 30,
}

f(**d)