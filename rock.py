from gestures import Gestures


class Rock(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        if self.player_one == "rock" and self.player_two == "scissors":
            self.player_one.score +=1
        if self.player_one == "rock" and self.player_two == "lizard":
            self.player_one.score +=1
        if self.player_two == "rock" and self.player_one == "scissors":
            self.player_two.score +=1
        if self.player_two == "rock" and self.player_one == "lizard":
            self.player_two.score +=1
        "rock".__gt__("scissors")
        "rock".__gt__("lizard")

