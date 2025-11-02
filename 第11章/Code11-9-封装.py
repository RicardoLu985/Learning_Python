# 封装
"""
    封装（Encapsulation）是面向对象编程的基础概念之一。它指的是将对象的属性和方法打包在一起，并对外隐藏其内部细节，只暴露公共接口
    私有属性和方法：使用单个下划线 _ 或双下划线 __ 使属性和方法在类外部不可直接访问。例如：

class Car:
    def __init__(self, model, year):
        self.__model = model  # 双下划线表示私有属性
        self.__year = year

    def __str__(self):
        return f"{self.__model} ({self.__year})"

    def start_engine(self):
        print(f"{self.__model}的发动机启动了！")

    def __private_method(self):
        print("这是一个私有方法")
公共接口：使用公共方法对外提供访问和操作对象属性的途径，而不直接暴露内部数据结构。例如：

class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def start_engine(self):
        print(f"{self.__model}的发动机启动了！")
信息隐藏：通过封装，内部实现细节对外部隐藏，从而提高代码的安全性和可维护性。

封装的好处在于：

提高代码的安全性：避免外部代码随意修改对象的内部状态。

增强代码的可维护性：修改内部实现时，不影响外部代码的使用。

提高代码的灵活性：可以在不改变接口的情况下修改内部实现。
"""

class User(object):
    def __init__(self,name,age):
        self._name=name  # 受保护的变量
        self.__age=age  # 私有变量

    """
        把函数当做变量使用：
        @property 
        def name(self):  # 获取变量
        @name.setter
        def name(self):  # 修改变量
        
        上下两个变量名要一致
    """

    @property  # 获取变量
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            raise TypeError
        else:
            self.__age=age

    def _show_infos(self):
        print('我是%s，今年%d岁。' % (self._name,self.__age))

mia = User('mia', 20)
print(mia._name)  # 输出 'mia'

# print(mia._User__age)  # 尝试访问私有变量
mia._show_infos()  # 输出信息
# print(dir(mia))  # 显示所有属性和方法
# print(mia.__dict__)  # 显示实例的属性字典
# print(mia.__age)  # 尝试直接访问私有变量会报错

mia.name = 'tom'  # 修改受保护变量
mia.age = 21  # 修改私有变量
print(mia.name, mia.age)  # 输出 'tom' 和 21

# print(mia.get_age())  # get_age() 方法已被移除
# print(mia.age(10))  # 错误：不能以函数方式调用属性
# mia.age(10)  # 错误：不能以函数方式调用属性
print(mia.age)  # 正确：输出年龄 21
mia.age = 26
print(mia.age)

