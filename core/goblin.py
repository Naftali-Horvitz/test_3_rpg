# from monster import Monster
from random import randint

weapon_val = {
    'סכין': 0.5,
    'חרב': 1,
    'גרזן':1.5
}

class Goblin:
    def __init__(self, name, weapon):
        self.name = name
        self.__hp = 20
        self.type = 'goblin'
        self.__speed = randint(5, 10)
        self.power = randint(5, 10)
        self.rating_armor = 1
        self.weapon = weapon

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed += value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp -= value

    def speak(self):
        print(f"my name is: {self.name}, my type is: {self.type}")

    def attack(self, value):
        return (self.power + value) * weapon_val[self.weapon]

    def __str__(self):
        return f"name: {self.name}, hp: {self.hp}, speed: {self.speed}, power: {self.power}, rating_armor: {self.rating_armor}, weapon: {self.weapon} "

    def away_run(self):
        pass


# g1 = Goblin("ss", 'סכין')
# g2 = Goblin("ss", 'גרזן')
# g3 = Goblin("ss", 'חרב')
#
# print(g1.weapon, g1.power)
# g1.attack()
# print(g1.weapon, g1.power)

