# match语句是Python3.10以后版本引入的新特性，用于模式匹配。
"""
    match语句中的每个代码块由一个或多个case子句构成。
    每个case子句后面跟着一个代码块。
    当模型匹配成功时，会执行相应的代码块。
    如果没有任何模式匹配成功，则可以选择一个默认的代码块，使用下划线 _ 表示。
"""
x = 4
match x:
    case 1:
        print(111)
    case 2:
        print(222)
    case 3:
        print(333)
    case _:
        print('others')