__author__ = 'anthony'


class BowlingGame(object):

    def __init__(self):
        self.pins_toppled = 0
        self.rolls = []

    def roll(self, pins_toppled):
        self.rolls.append(pins_toppled)

    def score(self):
        return sum(self.rolls)