age = input("请输入您的年龄：")
if age.isdigit():
    age = int(age)
    if 0 <= age <= 120:
        print("输入正确。")
    else:
        print("输入错误，请重新输入。")
else:
    print("请输入阿拉伯数字!")
