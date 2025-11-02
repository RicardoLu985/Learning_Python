class Player(object):
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
        print('在座的各位都是垃圾，我是第%d位王者荣耀的玩家，我的名字是%s，我的段位是%s' % (Player.numbers, self.name, self.level))

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

class GameWeapon(object):
    numbers = 0
    max_damage = 10000
    levels = ['青铜', '白银', '黄金', '铂金', '钻石', '星耀', '王者']

    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level
        GameWeapon.numbers += 1
        if damage > GameWeapon.max_damage:
            raise Exception('武器最大伤害值为10000，请重试！')
        if level not in GameWeapon.levels:
            raise Exception('段位设置错误！')

    def show_weapon(self):
        for k, v in self.__dict__.items():
            print(k, v)


mia = Player('mia', 24, '南宁', '青铜')
mia.show()
mia.level_up()
mia.show()

gun = GameWeapon('magic', 111, '白银')
mia.get_weapon(gun)
mia.show_weapon()
