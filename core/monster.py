from enum import Enum
from random import randint

class Monster():
    def __init__(self, name, type_m, weapon):
        self.name = name
        self.type_m = type_m
        self.weapon = weapon

    def speak(self):
        pass

    def attack(self):
        pass