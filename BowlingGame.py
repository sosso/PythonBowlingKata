__author__ = 'anthony'


class BowlingGame(object):
    def __init__(self):
        self.pins_toppled = 0

    def roll(self, pins_toppled):
        self.pins_toppled += pins_toppled

    def score(self):
        return self.pins_toppled