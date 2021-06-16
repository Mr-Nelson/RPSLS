class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = 0
        self.score = 0
    def choose_gesture(self):
        return int(self.chosen_gesture)