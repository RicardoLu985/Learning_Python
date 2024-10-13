"""
if 条件表达式：
    下级代码
else:
    下级代码
"""
# if和else语句以及各自的缩进部分共同是一个完整的代码块。
weather = "非下雨"
if weather == "下雨":
    print("记得带伞出门！")  # if语句的下级代码
else:
    print("戴个帽子。")

# 判断年龄
age = int(input("请输入你的你的年龄："))
if age >= 18:
    print("可以去网吧。")
else:
    print("还是乖乖在家写作业吧。")
