import unittest
from player_damage import p_dmg_disappear as p_dmg

class TestDamage(unittest.TestCase):
    def testing(self):
        hp = 50
        status = "alive"
        self.assertEqual(p_dmg.p_dmg_disappear(status, hp, 5), 45)

    def testing2(self):
        hp = 50
        status = "alive"
        self.assertEqual(p_dmg.p_dmg_disappear(status, hp, 50), "dead")

    def testin3(self):
        hp = 50
        status = "alive"
        self.assertEqual(p_dmg.p_dmg_disappear(status, hp, 0), 50)