from gestures import Gestures

class Paper(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        if self.player_one == "paper" and self.player_two == "rock":
            self.player_one.score +=1
        if self.player_one == "paper" and self.player_two == "Spock":
            self.player_one.score +=1
        if self.player_two == "paper" and self.player_one == "rock":
            self.player_two.score +=1
        if self.player_two == "paper" and self.player_one == "Spock":
            self.player_two.score +=1
        "paper".__gt__("rock")
        "paper".__gt__("Spock")