import random
from player import Player

class ArtificialIntelligence(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.player_gestures)
        return self.chosen_gesture
