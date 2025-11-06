from core.monster import Monster
from random import randint

weapon_val = {
    'סכין': 0.5,
    'חרב': 1,
    'גרזן':1.5
}

class Orc(Monster):
    def __init__(self, name, weapon):
        self.__hp = 50
        self.type = 'orc'
        self.speed = randint(0,5)
        self.power = randint(10,15)
        self.rating_armor = randint(2,8)
        super().__init__(name, self.type, weapon)

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp -= value

    def __str__(self):
        return f"name: {self.name}, hp: {self.hp}, speed: {self.speed}, power: {self.power}, rating_armor: {self.rating_armor}, weapon: {self.weapon} "
