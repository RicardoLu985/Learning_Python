# 模块（module）
"""
    模块就好比是工具包，要想使用这个工具包里的工具，就需要导入（import）这个模块。
    每一个以.py扩展名结尾的python源代码文件的都是一个模块。
    在模块中定义的全局变量、函数都是模块能够提供给外界直接使用的工具。
"""

# # 全局导入
# import my_module
# # 使用时需要写上模块名字
#
# result = my_module.add(2,4)
# print(result)
#
# result = my_module.total(1,2,3,4)
# print(result)
#
# print(my_module.author)

# # 部分导入
# from my_module import add
# # 使用时不需要写上模块名字
# result = add(2,4)
# print(result)

# # 杂交导入
# from my_module import *
# # 使用时不需要写上模块名字，但又全部导入了函数
# result = add(2,4)
# print(result)
#
# result = total(1,2,3,4)
# print(result)

# # 改名导入
from my_package.my_math import add as jia
# 给 add 取了别名 jia
result = jia(2,4)
print(result)