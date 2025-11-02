from datetime import datetime


def write_txt():
    date = input('请输入今天的日期和天气（格式：YYYY-MM-DD 天气）：')
    text = input('请输入日记的内容：')
    file_name = '日记本.txt'
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(date + '\n')
        f.write(text + '\n')
    return True


def read_txt(day='-1'):
    file_name = '日记本.txt'
    with open(file_name, 'r', encoding='utf-8') as f:
        context = f.readlines()

    if day != '-1':
        found = False
        for i in range(0, len(context), 2):
            record_date = context[i].split(' ')[0]  # 提取日期部分
            if record_date == day:
                print(context[i], end='')
                print(context[i + 1], end='')
                found = True
        if not found:
            print("没有找到对应日期的日记。")
    else:
        for line in context:
            print(line, end='')
    return True


def quit():
    print("感谢使用Python日志管理系统")


def menu():
    print('*' * 40)
    print('''欢迎使用Python日志管理系统
    1、记日记
    2、读日记
    3、退出系统''')
    print('*' * 40)

def main():
    menu()
    while True:
        op = input('请输入你的选择：')
        if op == '1':
            if write_txt():
                print('日记保存成功了！')
        elif op == '2':
            day = input('请输入查询的日期（格式：YYYY-MM-DD，查询全部请输入 -1）：')
            if read_txt(day):
                print("日记已读取完毕！")
        elif op == '3':
            quit()
            break
        else:
            print('请重新选择！')
