# 面向对象特点： 继承、多态、封装
"""
    继承（inheritance）是面向对象编程中的一个核心概念。简单来说，继承是指一个类（称为子类）从另一个类（称为父类）获取属性和方法的机制。
父类（Parent Class）：也称为基类（Base Class）或超类（Super Class），它定义了子类所继承的属性和方法。
子类（Child Class）：也称为派生类（Derived Class），它继承父类的属性和方法，并可以增加新的属性和方法，或者覆盖父类的方法。
这种机制的好处在于：
代码复用：通过继承，子类可以重用父类的代码，而不必重新编写相同的功能。
代码扩展：子类可以在继承父类的基础上增加新的功能，扩展父类的功能。
维护性：通过继承，可以更容易地对代码进行修改和扩展，提高代码的维护性。
"""
class Player(object):  # 父类
    numbers = 0  # 类属性
    levels = ['青铜', '白银', '黄金', '铂金', '钻石', '星耀', '王者']

    def __init__(self, name, age, city, level):  # 初始化函数(构造函数)
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        if level not in Player.levels:
            raise Exception('段位设置错误！')
        else:
            self.level = level
        self.weapon = None  # 初始化 weapon 属性
        Player.numbers += 1

    def show(self):
        print('在座的各位都是垃圾，我是第%d位王者荣耀的玩家，我的名字是%s，我的段位是%s,我的金币有%d个' % (Player.numbers, self.name, self.level, self.coin))

    def level_up(self):
        index1 = Player.levels.index(self.level) + 1
        if index1 < len(Player.levels):
            self.level = Player.levels[index1]

    def get_weapon(self, weapon):
        self.weapon = weapon

    def show_weapon(self):
        if self.weapon:
            return self.weapon.show_weapon()
        else:
            print('没有装备武器')

    @classmethod
    def get_player(cls):  # 类方法
        print('王者荣耀的用户数是%d人。' % cls.numbers)

    @staticmethod
    def isVaild(**kwargs):
        if kwargs['age'] > 18:
            return True
        else:
            return False

class VIP(Player): # 子类
    # 构造函数
    def __init__(self, name, age, city, level, coin):
        # 调用父类的构造函数
        super(VIP, self).__init__(name, age, city, level)
        self.coin = coin

mia = VIP('mia', 18,'北京', '黄金', 100)
print(type(mia))
print(isinstance(mia, Player))
print(isinstance(mia, VIP))
mia.show()
print(mia.coin)
