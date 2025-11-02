# 魔法方法
"""
    Python中的魔法方法（也称为特殊方法或双下划线方法）是一种在类定义中使用的特殊命名约定的方法。
    当Python遇到某些内置操作时，它会尝试在对象上调用这些方法。
    包括不限于算术运算、属性访问、类型转换等。
"""
'''
    魔法方法（Magic Methods），也称为双下划线方法（dunder methods），是Python类中的特殊方法。它们以双下划线开头和结尾，用于定义类的行为。例如，__init__ 方法就是一个常见的魔法方法。
'''

class User(object):
    def __init__(self, name):
        print('__init__被调用')
        self.name = name

mia = User('mia')


# __init__(self, ...)：构造函数，在创建对象时初始化对象属性。

def __init__(self, name, age):
    self.name = name
    self.age = age

# __str__(self)：定义对象的字符串表示，用于 print 函数。

def __str__(self):
    return f"{self.name} is {self.age} years old"

# __repr__(self)：提供对象的官方字符串表示，通常用于调试。

def __repr__(self):
    return f"User(name={self.name}, age={self.age})"

# __add__(self, other)：定义加法操作符 + 的行为。

def __add__(self, other):
    return self.age + other.age

# __len__(self)：定义对象的长度，用于 len() 函数。

def __len__(self):
    return len(self.name)

# __getitem__(self, key)：定义索引操作，用于 obj[key]。

def __getitem__(self, key):
    return self.data[key]

# __setitem__(self, key, value)：定义赋值操作，用于 obj[key] = value。

def __setitem__(self, key, value):
    self.data[key] = value

# __delitem__(self, key)：定义删除操作，用于 del obj[key]。

def __delitem__(self, key):
    del self.data[key]