while True:
    try:
        op = input("请输入一个四则运算式（例如1+2）：")
        if '+' in op:  # 加法
            a = op.split('+')
            result = int(a[0]) + int(a[1])
            print(result)
        elif '-' in op:
            a = op.split('-')
            result = int(a[0]) - int(a[1])
            print(result)
        elif '*' in op:
            a = op.split('*')
            result = int(a[0]) * int(a[1])
            print(result)
        elif '/' in op:
            a = op.split('/')
            result = int(a[0]) / int(a[1])
            print(result)
        elif op == 'C':
            print("感谢您的使用！")
            break
        else:
            raise Exception("请按照提示的格式输入式子。")
    except ZeroDivisionError:
        print("除法运算除数不能为 0 。")
    except Exception as e:
        print(e)