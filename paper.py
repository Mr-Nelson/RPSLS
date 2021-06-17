from gestures import Gestures

class Paper(Gestures):
    def __init__(self):
        super().__init__()

    def get_heirarchy(self):
        "paper".__lt__("rock")
        "paper".__init__("Spock")