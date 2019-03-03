from Player import Player
from Enemy import Enemy
from BattleSystem import BattleSystem


enemStat = {
    "Level": 1,
    "MaxHP" : 10,
    "HP": 5,
    "Atk": 1,
    "Def": 0,
    "Heal": 0,
    "XPDrop": 5
}

enemStat2 = {
    "Level": 1,
    "MaxHP" : 10,
    "HP": 5,
    "Atk": 10,
    "Def": 0,
    "Heal": 0,
    "XPDrop": 100
}

stats = {
    "Level": 1,
    "MaxHP" : 10,
    "HP": 10,
    "Atk": 10,
    "Def": 1,
    "Heal": 0,
    "XP": 0
}

stats2 = {
    "Level": 1,
    "MaxHP" : 10,
    "HP": 10,
    "Atk": 1,
    "Def": 1,
    "Heal": 0,
    "XP": 0
}


ralph = Player("Ralph", stats)
james = Player("James", stats2)


basicEnemy = Enemy("Basic", enemStat)
basicEnemy2 = Enemy("cuwa", enemStat2)

battle1 = BattleSystem(ralph, basicEnemy)
battle2 = BattleSystem(james, basicEnemy2)


print(battle1.battle())
print(battle2.battle())

