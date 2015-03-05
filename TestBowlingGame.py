__author__ = 'anthony'

import unittest
from BowlingGame import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def testAllGuttersReturns0(self):
        for _ in range(20):
            self.game.roll(0)
        self.assertEquals(0, self.game.score())

if __name__ == '__main__':
    unittest.main()
