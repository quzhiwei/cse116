import unittest
import p_dmg_disappear as pdd

class TestBattleInterface(unittest.TestCase):

    def testing(self):
        playerPos = {
            "player0": {
                "playerPos": (205, 330),
                "pointerPos": (230, 300),
                "textPos": (250, 310),
                "healPos": (250, 290),
                "playerText": '',
                "status": "player",
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
                "status": "player",
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
                "status": "player",
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
                "status": "player",
                "atk": 10,
                "heal": 10,
                "hp": 50,
                "max_hp": 50,
                "hp_pos": (850 - 35, 290 + 160)
            }
        }

        self.assertEqual(ppd.p_dmg_disappear("player0", 5), playerPos["player0"]["hp"] == 45)