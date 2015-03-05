__author__ = 'anthony'

import unittest
from BowlingGame import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def testAllGuttersReturns0(self):
        self.rollTimes(0, 20)
        self.assertEquals(0, self.game.score())

    def testAll1sReturns20(self):
        self.rollTimes(1, 20)
        self.assertEquals(20, self.game.score())

    def testItHandlesSpares(self):
        self.rollSpare()
        self.game.roll(5)

        self.rollTimes(0, 17)
        self.assertEquals(20, self.game.score())

    def rollSpare(self):
        self.game.roll(1)
        self.game.roll(9)

    def rollTimes(self, pins_toppled, times):
        for _ in range(times):
            self.game.roll(pins_toppled)

if __name__ == '__main__':
    unittest.main()
