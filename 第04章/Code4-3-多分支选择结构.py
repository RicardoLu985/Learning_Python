"""
if 条件表达式：
    下级代码
elif:
    下级代码
else:
    下级代码
"""
"""
    使用if可以判断条件
    使用else可以处理条件不成立的情况
    使用elif可以额外处理的条件
"""
# 成绩等级
score = int(input("请输入你的成绩："))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('D')

# BMI计算
# bmi = w / (h*h)

w = float(input("请输入你的体重kg："))
h = float(input("请输入你的身高m："))
bmi = w / (h*h)
print(bmi)
if bmi < 18.5:
    print("瘦了，多吃一点吧！")
elif bmi < 25:
    print("你的体型很标准")
else:
    print("运动运动更健康！")
