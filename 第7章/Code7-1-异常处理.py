# 异常
"""
    如果代码没有语法问题，可以运行，但会出现运行时的错误，例如除零错误、下标越界等问题，这种在运行期间检测到的错误被称为异常。
    出现了异常必须处理否则程序会终止执行，用户体验变差。
    Python支持程序员自己处理检测到的异常。
    可以使用try-except语句进行异常的检测和处理。
"""
# 常见错误类型
# NameError
# ptlnt('hello world!')  # 函数名拼写错误
print('hello world!')
a = '123'
# print(aa)  # 变量名拼写错误
print(a)
# print(b)  # 不存在的变量

# SyntaxError  # 语法错误
# if 'he' == 'hi'
#     print('True')
#IndentationError  # 缩进错误
# if 'he' == 'hi':
# print('True')
# TypeError  # 类型错误
# print(3+'2')
# AttributeError  # 属性错误
# tp = (1,2,3)
# tp.append(4)
# print(tp)
# IndexError  # 索引错误
# print(tp[4])
# KeyError  # 键值错误
# d = {1:2,3:4}
# print(d[2])