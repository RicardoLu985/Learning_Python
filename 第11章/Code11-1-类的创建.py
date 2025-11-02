# 类
"""
    class:表明是一个类
    ClassName：类的名字
    ():父类集合的开始和结束
    object：父类的名字，定义的类继承自父类，可以不写，默认是object。
            object是所有类的直接或间接父类。
"""
# 实例（对象）
"""
    类的实例化（创建对象）
    实例名 = 类() 的方式实例化对象，为类创建一个实例。 
"""
class Player(object):  # object 基类
    pass

tom = Player()  # 类的实例化（创建对象）
print(type(tom))
print(isinstance(tom, Player))
print(isinstance(tom, object))
