
weapon_val = {
    'סכין': 0.5,
    'חרב': 1,
    'גרזן':1.5
}

class Monster:
    def __init__(self, name, type_m, weapon):
        self.name = name
        self.type_m = type_m
        self.weapon = weapon

    def speak(self):
        print(f"my name is: {self.name}, my type is: {self.type_m}")

    def attack(self, value):
        return (self.power + value) * weapon_val[self.weapon]