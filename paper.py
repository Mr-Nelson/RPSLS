from gestures import Gestures

class Paper(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        "paper".__gt__("rock")
        "paper".__gt__("Spock")