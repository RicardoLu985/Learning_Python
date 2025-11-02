"""
    普通闰年的年份是4的倍数，且不是100的倍数；
    世纪闰年的年份必须是100的倍数。
"""

# 方法一：
# year = int(input("请输入年份："))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("%d 是闰年。" % year)
# else:
#     print("%d 不是闰年。" % year)


# 方法二
year = int(input("请输入年份："))
if not year % 4 and year % 100 or not year % 400 :
    print("%d 年是闰年。" % year)
else:
    print("%d 年不是闰年。" % year)

"""
    方法二采用bool运算，year % 4 and year % 100 == 0 是 False，
    加上not之后变成True。
"""