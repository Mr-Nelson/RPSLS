import random
from player import Player

class Artificial_Intelligence(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        random.choices(self.gestures)
        return self.chosen_gesture