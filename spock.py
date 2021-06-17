from gestures import Gestures

class Spock(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        if self.player_one == "Spock" and self.player_two == "scissors":
            self.player_one.score +=1
        if self.player_one == "Spock" and self.player_two == "rock":
            self.player_one.score +=1
        if self.player_two == "Spock" and self.player_one == "scissors":
            self.player_two.score +=1
        if self.player_two == "Spock" and self.player_one == "rock":
            self.player_two.score +=1
        "Spock".__gt__("scissors")
        "Spock".__gt__("rock")