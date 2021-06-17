class Gestures:

    def __init__(self):
        self.gesture_names = ["rock", "paper", "scissors", "lizard", "Spock"]

    def get_gesture_names(self):
        return self.gesture_names

    def get_hierarchy(self):
        if "subclass_one" > "subclass_two":
            pass
