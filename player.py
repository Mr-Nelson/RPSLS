class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = ""
    def choose_gesture(self):
        print("This method is overridden.")