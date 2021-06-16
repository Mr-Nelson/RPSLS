class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["rock", "paper", "scissors", "lizard", "Spock"]
        self.chosen_gesture = 0
        self.gesture_name = ""
        self.score = 0
    def choose_gesture(self):
        return int(self.chosen_gesture)
    def get_name(self):
        self.gesture_name = self.gestures[self.chosen_gesture]