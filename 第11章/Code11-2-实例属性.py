class Player(object):
    def __init__(self, name, age, city):  # 初始化函数(构造函数)
        self.name = name
        self.age = age
        self.city = city

Ricardo = Player('Ricardo', 21, 'San Francisco')
print(Ricardo.name, Ricardo.age, Ricardo.city)
tom = Player('tom', '23', 'Beijing')
tom.height = '177'
print(tom.name)
print(tom.__dict__, type(tom.__dict__))  # 获取实例（对象）的所有属性

# 武器：名字 攻击力 等级
class Weapon(object):
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level

dao = Weapon('wuqie', '648', '90')
print(dao.name, dao.damage, dao.level)
