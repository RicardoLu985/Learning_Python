# 多态：同一个方法，传入不同的参数，运行不同的逻辑。简单来说，多态允许同一个方法在不同对象上表现出不同的行为。
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# 使用多态
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)  # 输出：Bark
make_sound(cat)  # 输出：Meow

"""
    在这个例子中，Dog 和 Cat 类都继承自 Animal 类，并且重载了 sound 方法。尽管 make_sound 函数只调用了 Animal 类的方法，但由于多态的特性，它可以处理任何 Animal 子类对象并调用相应的方法。
"""