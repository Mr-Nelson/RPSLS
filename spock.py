from gestures import Gestures

class Spock(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        "Spock".__gt__("scissors")
        "Spock".__gt__("rock")