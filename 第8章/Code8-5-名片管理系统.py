from operator import truediv

cards = [{'name': '艺宝', 'phone': '123', 'qq': '456', 'email': '789'},
         {'name': '阿山', 'phone': '111', 'qq': '222', 'email': '333'}]  # 测试用例
def menu():
    print('*' * 30)
    print('''欢迎使用【名片管理系统】V1.0
        1、新建名片
        2、显示全部
        3、查询名片
        0、退出系统''')
    print('*' * 30)

def new_card(name, phone, qq, email):
    user = {
        'name': name,
        'phone': phone,
        'qq': qq,
        'email': email
    }
    cards.append(user)
    return True

def show_card():
    print(f"{'姓名':<10}{'电话':<15}{'QQ':<15}{'Email':<20}")  # 表头打印：打印表头行，包含列名“姓名”、“电话”、“QQ”和“Email”。<符号表示左对齐，后面的数字表示每列占用的空间。
    print('-' * 60)  # 分隔线：打印一行破折号，用于分隔表头和数据。
    for card in cards:
        print(f"{card['name']:<10}{card['phone']:<15}{card['qq']:<15}{card['email']:<20}")  # 数据行：迭代cards列表中的每个名片，并打印详细信息，使其在对应的列下对齐。

def query_card(kw):
    for card in cards:
        for key, value in card.items():
            if kw == value:
                return card
    return False

def modify_card(kw, new_name = None, new_phone = None, new_qq = None, new_email = None):
    card = query_card(kw)
    if card:
        if new_name:
            card['name'] = new_name
        if new_phone:
            card['phone'] = new_phone
        if new_qq:
            card['qq'] = new_qq
        if new_email:
            card['email'] = new_email
        return True
    return False

def del_card(kw):
    card = query_card(kw)
    if card:
        cards.remove(card)
        return True
    return False

def quit():
    print("欢迎下次使用【名片管理系统】V1.0")

menu()
while True:
    op = input("请选择操作选项：")
    if op == '1':
        name = input('请输入你的姓名：')
        phone = input('请输入你的电话：')
        qq = input('请输入你的QQ：')
        email = input('请输入你的email：')
        result = new_card(name, phone, qq, email)
        if result:
            print('成功新建 %s 的名片' % name)
        else:
            print('请重试！')
    elif op == '2':
        show_card()
    elif op == '3':
        kw = input('请输入查询关键字：')
        result = query_card(kw)
        if result:
            print(result)
            op2 = input('输入4修改名片，输入5删除名片，输入0退出操作：')
            if op2 == '4':
                new_name = input('输入新的姓名（留空则不修改）：')
                new_phone = input('输入新的电话（留空则不修改）：')
                new_qq = input('输入新的QQ（留空则不修改）：')
                new_email = input('输入新的email（留空则不修改）：')
                modify_card(kw, new_name, new_phone, new_qq, new_email)
            elif op2 == '5':
                del_card(kw)
            else:
                break
        else:
            print('没有查询到相关信息。')
    elif op == '0':
        quit()
        break
    else:
        print("请重试！")
