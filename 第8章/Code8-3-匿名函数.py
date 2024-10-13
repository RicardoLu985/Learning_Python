# lambda函数是一种快速定义单行的最小函数。可以用在任何需要函数的地方。
# 优点：让代码更加简洁，不需要考虑命名的问题。

fun = lambda a,b : a+b
result = fun(2,4)
print(result)


# list1 = [1,2,3,4,5]
# def f(x):
#     return x ** 2
#
# result = map(f, list1)
# print(list(result))

list1 = [1,2,3,4,5]
result = map(lambda x : x**3, list1)  # map 映射函数
print(list(result))

# reduce 累积函数
from functools import reduce
result = reduce(lambda x,y:x*y,list1)
print(result)

# result = 1
# for i in list1:
#     result *= i
# print(result)

# filter 过滤
# b = []
# for i in list1:
#     if i % 2 == 0:
#         b.append(i)
# print(b)

result1 = filter(lambda x : x%2==0,list1)
result2 = filter(lambda x : x%2,list1)
print(list(result1))
print(list(result2))


# 了解内置函数
