try:
    print("有可能出现异常的代码")
    n = int(input("请输入一个数字："))
    n = 5 / n
    print(n)
except ZeroDivisionError as e:
    print("数字不能为 0 ！",e)
except ValueError:
    print("请输入一个数字：")
else:
    print('运行没报错，没被except捕获，则进入else模块')
finally:
    print('无论如何都会进入finally模块。')
