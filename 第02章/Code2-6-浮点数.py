# 浮点型（Floating Point Numbers）
"""
    由整数和小数部分组成。
    注意，运算可能有四舍五入的误差。
"""
# 浮点数的计算
n1 = 0.123456
n2 = 0.1
print(n1 + n2)
n3 = 0.2
print( n2 + n3 )

# 四舍五入round()
n4 = round(n2 + n3 , 2)
print(n4)

import math
# 向上取整 ceil
n5 = math.ceil(n1 + n2 )
print("向上取整的结果：", n5)
# 向下取整 floor
n6 = math.floor(n1 + n2 )
print("向下取整的结果：", n6)