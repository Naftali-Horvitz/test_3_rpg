from enum import Enum
from random import randint

class Profession(Enum):
    לוחם = 0
    מרפא = 1

class Player:
    def __init__(self, name, profession):
        self.name = name
        self.__hp = 60 if profession == 'לוחם' else 50
        self.__speed = randint(5,10)
        self.power = randint(5,10) if profession == 'מרפא' else + randint(5,10) + 2
        self.__rating_armor = randint(5,15)
        self.profession = profession

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp -= value

    @property
    def speed(self):
        return self.__speed


    @property
    def rating_armor(self):
        return self.__rating_armor

    def attack(self, value):
        return self.power + value

    def speak(self):
        print(f"my name is: {self.name}")

    def __str__(self):
        return f"name: {self.name}, hp: {self.hp}, speed: {self.speed}, power: {self.power}, rating_armor: {self.rating_armor}, profession: {self.profession}"


# p1 = Player("yosef", "לןחם")

# print(p1.hp)
# print(p1.power)
