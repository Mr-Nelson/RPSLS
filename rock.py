from gestures import Gestures


class Rock(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        "rock".__gt__("scissors")
        "rock".__gt__("lizard")

