import unittest
import random
from generate import generate_entity as gen

class TestGeneration(unittest.TestCase):
    def test1(self):
        num = 5
        self.assertEqual(gen.generate(num), [0, 1, 2, 3, 4])

    def test2(self):
        num = 0
        self.assertEqual(gen.generate(num), [])

    def test3(self):
        num = random.randint(0, 10)
        test = gen.generate(num)
        expected = []
        for x in range(num):
            expected.append(x)
        self.assertEqual(test, expected)
        self.assertEqual(gen.get_len(test), len(expected))

    def test4(self):
        num = 0
        test = gen.generate(num)
        self.assertEqual(gen.get_len(test), 0)