from gestures import Gestures

class Spock(Gestures):
    def __init__(self):
        super().__init__()

    def get_heirarchy(self):
        "Spock".__lt__("scissors")
        "Spock".__lt__("rock")