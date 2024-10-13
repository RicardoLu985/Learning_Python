# 包（package）
"""
    包是Python模块的一种组织形式，将多个模块组合在一起，形成一个大的Python工具库。
    包通常是一个拥有__init__.py文件的目录，它定义了包的属性和方法。
"""

from my_package import my_math, my_card
from my_package import *  # 调用包结果与调用模块结果略有不同
result = my_math.total(1,2,3)
print(result)

my_card.menu()

