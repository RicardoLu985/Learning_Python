# 用户名、密码、黑名单
users = {
    '艺宝' : {
        'name' : '艺宝',
        'password' : '123',
        'status' : True
    },
    'shenlei' : {
        'name' : 'shenlei',
        'password' : '456',
        'status' : True
    },
    'jack' : {
        'name' : 'jack',
        'password' : '789',
        'status' : False
    }
}
print(users)

for j in range(3):
    user = input("请输入你的用户名：")
    pwd = input("请输入你的密码：")
    if user in users and pwd in users[user]['password'] and users[user]['status'] == True:
        print("欢迎%s登录系统" % user)
        break
    elif user in users and users[user]['status'] == False:
        print("账号失效，请联系管理员。")
    elif user in users and pwd != users[user]['password']:
        print("密码输入错误，请重试！")
    else:
        print("用户不存在，请先注册！")
