from healing import healing as heal
import unittest

class TestHeal(unittest.TestCase):
    def test1(self):
        hp = 20
        max_hp = 50
        status = "alive"
        self.assertEqual(heal.p_heal_disappear(hp, max_hp, status, 5), 25)

    def test2(self):
        hp = 50
        max_hp = 50
        status = "alive"
        self.assertEqual(heal.p_heal_disappear(hp, max_hp, status, 5), 50)

    def test3(self):
        hp = 0
        max_hp = 50
        status = "alive"
        self.assertEqual(heal.p_heal_disappear(hp, max_hp, status, 5), "dead")

    def test4(self):
        hp = -50
        max_hp = 50
        status = "alive"
        self.assertEqual(heal.p_heal_disappear(hp, max_hp, status, 5), "dead")