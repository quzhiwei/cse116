import pygame, sys
from pygame.locals import *
import os
import random
import View.gameMain


class Battle(object):

    def __init__(self):
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Hello World")

        self.battleStage = pygame.image.load(os.path.join('img', "battleStage.png"))
        self.pointer = pygame.transform.scale(pygame.image.load(os.path.join('img', 'pointer.png')), (16, 16))
        self.red_pointer = pygame.transform.scale(pygame.image.load(os.path.join('img', 'red_pointer.png')), (16, 16))
        self.player = pygame.transform.scale(pygame.image.load(os.path.join('img/characters/oldMan', 'tile037.png')), (64, 96))
        self.enemy = pygame.transform.scale(pygame.image.load(os.path.join('img/characters/blondeGuy', 'tile049.png')), (64, 96))
        self.white_box = pygame.image.load(os.path.join('img', 'white_box.png'))

        self.dead = pygame.image.load(os.path.join('img', 'dead.png'))

        self.action_text_pos = ()

        self.playerPos = {
            "player0": {
                "playerPos": (205, 330),
                "pointerPos": (230, 300),
                "textPos": (250, 310),
                "healPos": (250, 290),
                "playerText": '',
                "status": self.player,
                "atk": 10,
                "heal": 10,
                "hp": 50,
                "max_hp": 50,
                "hp_pos": (215, 450)
            },
            "player1": {
                "playerPos": (380, 370),
                "pointerPos": (380 + 25, 370 - 30),
                "textPos": (425, 350),
                "healPos": (425, 330),
                "playerText": '',
                "status": self.player,
                "atk": 10,
                "heal": 10,
                "hp": 50,
                "max_hp": 50,
                "hp_pos": (425 - 35, 330 + 160)
            },
            "player2": {
                "playerPos": (625, 370),
                "pointerPos": (625 + 25, 370 - 30),
                "textPos": (670, 350),
                "healPos": (670, 330),
                "playerText": '',
                "status": self.player,
                "atk": 10,
                "heal": 10,
                "hp": 50,
                "max_hp": 50,
                "hp_pos": (670 - 35, 330 + 160)
            },
            "player3": {
                "playerPos": (805, 330),
                "pointerPos": (805 + 25, 330 - 30),
                "textPos": (850, 310),
                "healPos": (850, 290),
                "playerText": '',
                "status": self.player,
                "atk": 10,
                "heal": 10,
                "hp": 50,
                "max_hp": 50,
                "hp_pos": (850 - 35, 290 + 160)
            }
        }

        self.enemyPos = {
            "enemy0": {
                "enemyPos": (795, 90),
                "pointerPos": (795 + 25, 90 - 30),
                "textPos": (850, 70),
                "healPos": (850, 90),
                "enemyText": '',
                "status": self.enemy,
                "atk": 5,
                "heal": 5,
                "hp": 10,
                "max_hp": 10,
                "hp_pos": (850 - 35, 90 + 115)
            },
            "enemy1": {
                "enemyPos": (620, 50),
                "pointerPos": (620 + 25, 50 - 30),
                "textPos": (665, 30),
                "healPos": (665, 50),
                "enemyText": '',
                "status": self.enemy,
                "atk": 5,
                "heal": 5,
                "hp": 10,
                "max_hp": 10,
                "hp_pos": (665 - 35, 50 + 115)
            },
            "enemy2": {
                "enemyPos": (370, 50),
                "pointerPos": (370 + 25, 50 - 30),
                "textPos": (415, 30),
                "healPos": (415, 50),
                "enemyText": '',
                "status": self.enemy,
                "atk": 5,
                "heal": 5,
                "hp": 10,
                "max_hp": 10,
                "hp_pos": (415 - 35, 50 + 115)
            },
            "enemy3": {
                "enemyPos": (195, 90),
                "pointerPos": (195 + 25, 90 - 30),
                "textPos": (195 + 45, 90 - 20),
                "healPos": (195 + 45, 90),
                "enemyText": '',
                "status": self.enemy,
                "atk": 5,
                "heal": 5,
                "hp": 10,
                "max_hp": 10,
                "hp_pos": (195 + 45 - 35, 90 + 115)
            }
        }

        # Random number from 1 to 4
        self.enemy_num = random.randint(1, 4)
        # Enemy party
        self.enemy_party = []

        # party testing
        self.party = ["Ralph", "BangYu", "Zhiwei", "TA"]

        self.player_alive = []
        for y in range(len(self.party)):
            self.player_alive.append("player" + str(y))

        self.enemy_alive = []
        for i in self.enemy_party:
            self.enemy_alive.append(i)

        self.set_x = -1
        self.set_y = -1

    def text_to_screen(self, screen, text, pos, size, color, font_type='fonts/Marvelous-Sans-Demo.ttf'):
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        return screen.blit(text, pos)

    # Show what players can do
    def show_options(self):
        self.text_to_screen(self.DISPLAYSURF, "Attack (a)", (820, 600), 30, (000, 000, 000))
        self.text_to_screen(self.DISPLAYSURF, "Heal (h)", (820, 630), 30, (000, 000, 000))

    # show hp
    def show_player_hp(self, party_size):
        for num in range(party_size):
            self.text_to_screen(self.DISPLAYSURF, str(self.playerPos["player" + str(num)]["hp"]) + "/" + str(
                self.playerPos["player" + str(num)]["max_hp"]), self.playerPos["player" + str(num)]["hp_pos"], 18,
                           (000, 000, 000))

    def show_enemy_hp(self, party_size):
        for num in range(party_size):
            self.text_to_screen(self.DISPLAYSURF,
                           str(self.enemyPos["enemy" + str(num)]["hp"]) + "/" + str(self.enemyPos["enemy" + str(num)]["max_hp"]),
                           self.enemyPos["enemy" + str(num)]["hp_pos"], 18, (000, 000, 000))

    # Makes damage disappear after 0.6 seconds for players
    def p_dmg_disappear(self, player_n, enemy_dmg):
        player_x = self.playerPos[str(player_n)]
        player_x["hp"] -= enemy_dmg
        if player_x["hp"] <= 0:
            player_x["status"] = self.dead
        self.text_to_screen(self.DISPLAYSURF, "-" + str(enemy_dmg) + "HP", player_x["textPos"], 20,
                       (200, 000, 000))  # 20 = size (200, 000 ,000) = red
        pygame.display.update()
        pygame.time.wait(600)
        self.text_to_screen(self.DISPLAYSURF, player_x["playerText"], player_x["textPos"], 20, (200, 000, 000))

    # Makes healing number disappear after 0.6 seconds for players
    def p_heal_disappear(self, player_n, player_heal):
        player_x = self.playerPos[str(player_n)]
        if player_x["hp"] >= player_x["max_hp"]:
            player_x["hp"] = player_x["max_hp"]
        else:
            player_x["hp"] += player_heal
        self.text_to_screen(self.DISPLAYSURF, "+" + str(player_heal) + "HP", player_x["healPos"], 20, (000, 200, 000))
        pygame.display.update()
        pygame.time.wait(600)
        self.text_to_screen(self.DISPLAYSURF, player_x["playerText"], player_x["healPos"], 20, (000, 200, 000))

    # Makes damage disappear after 0.6 seconds for enemies
    def e_dmg_disappear(self, enemy_n, player_dmg):
        enemy_x = self.enemyPos[str(enemy_n)]
        enemy_x["hp"] -= player_dmg
        if enemy_x["hp"] <= 0:
            enemy_x["status"] = self.dead
        self.text_to_screen(self.DISPLAYSURF, "-" + str(player_dmg) + "HP", enemy_x["textPos"], 20,
                       (200, 000, 000))  # 20 = size (200, 000 ,000) = red
        pygame.display.update()
        pygame.time.wait(600)
        self.text_to_screen(self.DISPLAYSURF, enemy_x["enemyText"], enemy_x["textPos"], 20, (200, 000, 000))

    # Makes healing number disappear after 0.6 seconds for enemies
    def e_heal_disappear(self, enemy_n, enemy_heal):
        enemy_x = self.enemyPos[str(enemy_n)]
        if enemy_x["hp"] >= enemy_x["max_hp"]:
            enemy_x["hp"] = enemy_x["max_hp"]
        else:
            enemy_x["hp"] += enemy_heal
        self.text_to_screen(self.DISPLAYSURF, "+" + str(enemy_heal) + "HP", enemy_x["healPos"], 20, (000, 200, 000))
        pygame.display.update()
        pygame.time.wait(800)
        self.text_to_screen(self.DISPLAYSURF, enemy_x["enemyText"], enemy_x["healPos"], 20, (000, 200, 000))

    # Randomly generate amount of enemies
    def gen_enemy(self, enemy_num):
        for i in range(enemy_num):
            self.DISPLAYSURF.blit(self.enemyPos["enemy" + str(i)]["status"], self.enemyPos["enemy" + str(i)]["enemyPos"])

    # Making the party for enemy
    def gen_enemy_party(self, enemy_num):
        for i in range(enemy_num):
            self.enemy_party.append("enemy" + str(i))

    # Generate amount of players
    def gen_players(self, party):
        party_size = len(party)
        for i in range(party_size):
            self.DISPLAYSURF.blit(self.playerPos["player" + str(i)]["status"], self.playerPos["player" + str(i)]["playerPos"])

    # turns

    def check_enemies_status(self, enemy_party):
        enemy_dead_count = 0
        for i in range(len(enemy_party)):
            if self.enemyPos["enemy" + str(i)]["status"] == self.dead:
                enemy_dead_count += 1
        if enemy_dead_count == len(enemy_party):
            return "dead"
        else:
            return "alive"

    def check_player_status(self, party):
        player_dead_count = 0
        for i in range(len(party)):
            if self.playerPos["player" + str(i)]["status"] == self.dead:
                player_dead_count += 1
        if player_dead_count == len(party):
            return "dead"
        else:
            return "alive"

    '''
    player_alive = []
    for y in range(len(party)):
        player_alive.append("player" + str(y))

    enemy_alive = []
    for i in enemy_party:
        enemy_alive.append(i)
    '''

    def enemy_dead(self, e_count):
        if self.enemyPos["enemy" + str(e_count)]["status"] == self.dead:
            self.enemy_alive.remove("enemy" + e_count)

    def player_dead(self, p_count):
        if self.playerPos["player" + str(p_count)]["status"] == self.dead:
            self.player_alive.remove("player" + p_count)

    def BattleMain(self):

        #self.set_x = set_x
        #self.set_y = set_y

        current = 0

        # Getting ready with pre-made items
        self.gen_enemy_party(self.enemy_num)

        player_count = len(self.party)
        p_count = 0
        enemy_count = len(self.enemy_party)
        e_count = 0

        # main loop for the game
        while self.check_player_status(self.party) == "alive" and self.check_enemies_status(self.enemy_party) == "alive":
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit

            self.DISPLAYSURF.blit(self.battleStage, (0, 0))

            self.gen_enemy(self.enemy_num)
            self.gen_players(self.party)
            self.show_options()

            # turn here
            if p_count >= player_count:
                p_count = 0

            if e_count >= enemy_count:
                e_count = 0

            if current >= enemy_count:
                current = 0

            if current < 0:
                current = len(self.enemy_party) - 1

            if self.playerPos["player" + str(p_count)]["status"] == self.player:
                self.text_to_screen(self.DISPLAYSURF, self.party[p_count] + "'s turn.", (260, 630), 30, (000, 000, 000))
                self.DISPLAYSURF.blit(self.pointer, self.playerPos["player" + str(p_count)]["pointerPos"])
                self.DISPLAYSURF.blit(self.red_pointer, self.enemyPos["enemy" + str(e_count)]["pointerPos"])
                self.DISPLAYSURF.blit(self.pointer, self.enemyPos["enemy" + str(current)]["pointerPos"])
                for event in pygame.event.get():
                    if event.type == KEYDOWN:

                        if event.key == pygame.K_e:
                            session = View.gameMain.Game()
                            while True:
                                session.session_setup()
                                session.update_session()



                        if event.key == pygame.K_LEFT:
                            current += 1
                        if event.key == pygame.K_RIGHT:
                            current -= 1
                        if event.key == pygame.K_a:
                            self.e_dmg_disappear("enemy" + str(current),
                                            random.randint(0, self.playerPos["player" + str(p_count)]["atk"]))
                            p_count += 1
                            if self.enemyPos["enemy" + str(e_count)]["status"] == self.dead:
                                e_count += 1
                            else:
                                choice = random.randint(1, 2)
                                if choice == 1:
                                    chosen_player = self.player_alive[random.randint(0, len(self.player_alive) - 1)]
                                    self.p_dmg_disappear(chosen_player,
                                                    random.randint(0, self.enemyPos['enemy' + str(e_count)]["atk"]))
                                    e_count += 1
                                else:
                                    self.e_heal_disappear("enemy" + str(e_count),
                                                     random.randint(0, self.enemyPos["enemy" + str(e_count)]["heal"]))
                                    e_count += 1
                        if event.key == pygame.K_h:
                            self.p_heal_disappear("player" + str(p_count),
                                             random.randint(0, self.playerPos["player" + str(p_count)]["heal"]))
                            p_count += 1
                            if self.enemyPos["enemy" + str(e_count)]["status"] == self.dead:
                                e_count += 1
                            else:
                                choice = random.randint(1, 2)
                                if choice == 1:
                                    chosen_player = self.player_alive[random.randint(0, len(self.player_alive) - 1)]
                                    self.p_dmg_disappear(chosen_player, random.randint(0, 100))
                                    e_count += 1
                                else:
                                    self.e_heal_disappear("enemy" + str(e_count),
                                                     random.randint(0, self.enemyPos["enemy" + str(e_count)]["heal"]))
                                    e_count += 1

            self.show_player_hp(len(self.party))
            self.show_enemy_hp(len(self.enemy_party))
            pygame.display.flip()

            pygame.display.update()

