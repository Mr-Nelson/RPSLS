from gestures import Gestures

class Lizard(Gestures):
    def __init__(self):
        super().__init__()

    def get_heirarchy(self):
        "lizard".__lt__("Spock")
        "lizard".__lt__("paper")
