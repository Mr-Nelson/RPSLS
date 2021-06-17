from human import Human
from artificial_intelligence import ArtificialIntelligence

class Gestures:

    def __init__(self):
        self.gesture_names = ["rock", "paper", "scissors", "lizard", "Spock"]
        self.player_one = Human("name")
        self.player_one.score = 0
        self.player_two = Human("name") or ArtificialIntelligence()
        self.player_two.score = 0

    def get_hierarchy(self):
        if self.player_one == self.gesture_names and self.player_two == self.gesture_names:
            self.player_one.score +=1