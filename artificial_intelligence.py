import random
from player import Player

class Artificial_Intelligence(Player):
    def __init__(self, name):
        super().__init__(name)
        self.gestures = [0, 1, 2, 3, 4]

    def choose_gesture(self):
        ai_input = random.choice(self.gestures)
        self.chosen_gesture = int(ai_input)
        self.get_name()