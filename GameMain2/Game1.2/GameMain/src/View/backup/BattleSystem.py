import random
import math

class BattleSystem(object):
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    #Battle options for player
    def playerBattle(self):
        playerC = input("What would you like to do? Attack (a), Heal (h).")
        damage = random.randint(0, self.player.stats["Atk"]) - random.randint(0, self.enemy.stats["Def"])
        defend = random.randint(0, self.enemy.stats["Def"])
        if playerC.lower() == "a" or playerC.lower() == "attack":
            if damage < defend:
                self.enemy.stats["HP"] -= 0
                print("You hit a 0. The enemy has " + str(self.enemy.stats["HP"]) + " HP left.")
            else:
                self.enemy.stats["HP"] -= damage
                print("You hit a " + str(damage) + ". The enemy has " + str(self.enemy.stats["HP"]) + " HP left.")
        elif playerC.lower() == "h" or playerC.lower() == "heal":
            if self.player.stats["HP"] + self.player.stats["Heal"] > self.player.stats["MaxHP"]:
                self.player.stats["HP"] = self.player.stats["MaxHP"]
                print("You have healed " + str(self.player.stats["Heal"]) + " HP. Your current HP is " + str(self.player.stats["HP"]) + " HP.")
            else:
                self.player.stats["HP"] += self.player.stats["Heal"]
                print("You have healed " + str(self.player.stats["Heal"]) + " HP. Your current HP is " + str(self.player.stats["HP"]) + " HP.")

    #Battle for ai
    def enemyBattle(self):
        #use random int to choose what action the enemy will do
        options = [self.enemy.stats["Atk"], self.enemy.stats["HP"]]
        damage = random.randint(0, self.enemy.stats["Atk"])
        defend = random.randint(0, self.player.stats["Def"])
        if self.enemy.stats["HP"] == self.enemy.stats["MaxHP"] or self.enemy.stats["Heal"] == 0:
            if damage <= defend:
                self.player.stats["HP"] -= 0
                print("The enemy has hit a 0. " + str(self.player.name) + " has " + str(self.player.stats["HP"]) + " HP left. \n")
            else:
                self.player.stats["HP"] -= damage
                print("Ememy has hit a " + str(damage) + ". " + str(self.player.name) + " has " + str(self.player.stats["HP"]) + " HP left. \n")
        else:
            choice = random.randint(0, len(options) - 1)
            if choice == 0:
                if damage <= defend:
                    self.player.stats["HP"] -= 0
                    print("The enemy has hit a 0. " + str(self.player.name) + " has " + str(self.player.stats["HP"]) + " HP left.")
                else:
                    self.player.stats["HP"] -= damage
                    print("Ememy has hit a " + str(damage) + ". " + str(self.player.name) + " has " + str(self.player.stats["HP"]) + " HP left.")
            elif choice == 1:
                if self.enemy.stats["HP"] + self.enemy.stats["Heal"] > self.enemy.stats["MaxHP"]:
                    self.enemy.stats["HP"] = self.enemy.stats["MaxHP"]
                    print("The enemy have healed " + str(self.enemy.stats["Heal"]) + " HP. The enemy current HP is " + str(self.enemy.stats["HP"]) + " HP.")
            else:
                self.enemy.stats["HP"] += self.enemy.stats["Heal"]
                print("The enemy has healed " + str(self.enemy.stats["Heal"]) + " HP. The enemy's current HP is " + str(self.enemy.stats["HP"]) + " HP.")

    #Check if enemy is dead
    def enemyDead(self):
        if self.enemy.stats["HP"] <= 0:
            self.player.stats["XP"] += self.enemy.stats["XPDrop"]
            if self.player.stats["XP"] >= self.player.xpReset:
                print("\nEnemy Defeeated!" + "\n" + "Stats: " + str(self.player.stats) + "\n")
                self.levelUp()
            else:
                print("\nEnemy Defeeated!" + "\n" + "Stats: " + str(self.player.stats) + "\n")


    #Check if player is dead
    def playerDead(self):
        if self.player.stats["HP"] <= 0:
            print("Oh dear, you are dead!" + "\n")

    #The battle system which takes all the methods from before and make a functional battle system
    def battle(self):
        while self.player.stats["HP"] > 0 or self.enemy.stats["HP"] > 0:
            self.playerBattle()
            if self.enemy.stats["HP"] <= 0:
                self.enemyDead()
                return "Stats: " + str(self.player.stats) + "\n"
            self.enemyBattle()
            if self.player.stats["HP"] <= 0:
                self.playerDead()
                self.player.stats["HP"] = 0
                return "Stats: " + str(self.player.stats) + "\n"

    #Function for player to level up
    def levelUp(self):
        choice = input("\nCongratulations, " + self.player.name + " has leveled up to level " + str(self.player.stats["Level"] + 1) + "."
                "What would you like to level up? HP, Attack (a), Defense (d), Heal (h).")
        self.player.stats["XP"] -= self.player.xpReset
        if choice.lower() == "hp":
            self.player.stats["MaxHP"] += 1
            self.player.stats["Level"] += 1
            if self.player.stats["XP"] >= self.player.xpReset:
                self.player.xpReset *= 1.5
                self.player.xpReset = math.ceil(self.player.xpReset)
                self.levelUp()
        elif choice.lower() == "attack" or choice.lower() == "a":
            self.player.stats["Atk"] += 1
            self.player.stats["Level"] += 1
            if self.player.stats["XP"] >= self.player.xpReset:
                self.player.xpReset *= 1.5
                self.player.xpReset = math.ceil(self.player.xpReset)
                self.levelUp()
        elif choice.lower() == "defense" or choice.lower() == "d":
            self.player.stats["Def"] += 1
            self.player.stats["Level"] += 1
            if self.player.stats["XP"] >= self.player.xpReset:
                self.player.xpReset *= 1.5
                self.player.xpReset = math.ceil(self.player.xpReset)
                self.levelUp()
        elif choice.lower() == "heal" or choice.lower() == "h":
            self.player.stats["Heal"] += 1
            self.player.stats["Level"] += 1
            if self.player.stats["XP"] >= self.player.xpReset:
                self.player.xpReset *= 1.5
                self.player.xpReset = math.ceil(self.player.xpReset)
                self.levelUp()
        else:
            self.levelUp()
