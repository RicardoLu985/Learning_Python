# Python的小整数，通常是指[-5,256]之间的整数。
# id()获取的内存地址不是小整数真正的额内存地址。

a = b = 3
print(id(a),id(b))

c = 300
d = 300
print(id(c),id(d))

# Python自带的IDLE和Pycharm都经过了优化，测试显示都是一致的；
# 这些整数对象是提前建立好的，不会被垃圾回收。在一个 Python 的程序中，无论这个整数处于LEGB(局部变量，闭包，全局，内建模块)中的哪个位置，所有位于这个范围内的整数使用的都是同一个对象。

# 需要CMD终端测试。
# >>> a = b = 3
# >>> print(id(a),id(b))
# 140727680240120 140727680240120
# >>> c = 300
# >>> d = 300
# >>> print(id(c),id(d))
# 1926488217072 1926488217584
# >>> a is b
# True
# >>> c is d
# False
# >>>
