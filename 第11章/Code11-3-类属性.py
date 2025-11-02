class Player(object):
    numbers = 0  # 类属性
    def __init__(self, name, age, city):  # 初始化函数(构造函数)
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1

mia = Player('mia', 24, '上海')
print(mia.__dict__)
print('欢迎王者荣耀的第', Player.numbers, '个玩家！')
tom = Player('tom', 32, '重庆')
print('欢迎王者荣耀的第', Player.numbers, '个玩家！')


class Weapon(object):
    numbers = 0
    max_damage = 10000
    levels = ['青铜', '白银', '黄金', '铂金', '钻石', '星耀', '王者']
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level
        Weapon.numbers += 1
        if damage > self.max_damage:
            raise Exception('武器最大伤害值为10000，请重试！')
        if level not in level:
            raise Exception('段位设置错误！')
try :
    gun = Weapon('magic', 100, '钻石')
    print(Weapon.numbers)
    aroow = Weapon('magic', 1000, '王者')
    print(Weapon.numbers)
except Exception as e:
    print(e)


