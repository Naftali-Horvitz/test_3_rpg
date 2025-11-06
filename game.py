from core.player import Player
from core.goblin import Goblin
from core.orc import Orc
from random import randint
from enum import Enum

class Profession(Enum):
    לוחם = 0
    מרפא = 1

def start():
    menu_show()
    p1 = player_create()
    mo = monster_random_choose()
    battle(mo, p1)


def menu_show():
    is_start = ''
    while is_start != 'Y':
        is_start =  input("type y to startr game and n to not game\n").upper()

def player_create():
    profession = Profession.לוחם if randint(0,1) == 0 else Profession.מרפא
    return Player("yosef", profession)

def monster_random_choose():
    monster_random = randint(0, 1)
    if monster_random == 0:
        return Goblin("go", "חרב")
    else:
        return Orc("or", "סכין")

def battle(monster ,player: Player):

    turn = first_turn(monster ,player)
    next_turn = monster if turn == player else player
    print(f"תוקף ראשון: {turn.name}")
    print(turn)
    print(next_turn)

    while next_turn.hp > 0 or turn.hp > 0:
        res = dice_roll(20) + turn.speed
        print(f" תוקף: {turn.name} תקיפה: {res} שריון יריב: {next_turn.rating_armor}")
        if res > next_turn.rating_armor:
            damage = turn.attack(dice_roll(6))
            next_turn.hp = damage
            print(f"נזק: {damage} יתרת חיים: {next_turn.hp}")
        if next_turn.hp <= 0 or turn.hp <= 0:
            return
        turn, next_turn = next_turn, turn
    print(f"the {next_turn.name} is dead")

def first_turn(monster ,player: Player):
    player_speed = dice_roll(6) + player.speed
    monster_speed = dice_roll(6) + monster.speed
    monster.speak()
    player.speak()
    return monster if monster_speed > player_speed else player

def dice_roll(sides):
    if sides == 20:
        return randint(1, 20)
    else:
        return randint(1, 6)

if __name__ == "__main__":
    start()