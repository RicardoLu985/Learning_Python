try:
    pwd = input("请输入你的密码：")
    if len(pwd) < 8:
        raise Exception('请输入长度八位以上的密码。')
except Exception as e:
    print(e)