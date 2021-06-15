class Player:
    def __init__(self, name):
        self.name = name
        self.chose_gesture = ""

    def chose_gesture(self):
        gestures_index = 1
        gestures = ("rock", "paper", "scissors", "lizard", "spock")