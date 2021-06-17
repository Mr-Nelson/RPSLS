from gestures import Gestures

class Lizard(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        if self.player_one == "lizard" and self.player_two == "Spock":
            self.player_one.score +=1
        if self.player_one == "lizard" and self.player_two == "paper":
            self.player_one.score +=1
        if self.player_two == "lizard" and self.player_one == "Spock":
            self.player_two.score +=1
        if self.player_two == "lizard" and self.player_one == "paper":
            self.player_two.score +=1
        "lizard".__gt__("Spock")
        "lizard".__gt__("paper")
