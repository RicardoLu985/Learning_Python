# 题目要求：输入指定日期，输出这一天是今年的第几天。
# 2023-12-21

date = input("请输入指定日期：").split('-')
year = int(date[0])
month = int(date[1])
day = int(date[2])

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]  # 0 占位符
if not year % 4 and year % 100 or not year % 400 :
    days[2] += 1
result = 0
for i in range(month):
    result += days[i]
result += day
print("这天是%d年的第%d天。" % (year, result))
