from gestures import Gestures


class Scissors(Gestures):
    def __init__(self):
        super().__init__()

    def get_hierarchy(self):
        if self.player_one == "scissors" and self.player_two == "paper":
            self.player_one.score +=1
        if self.player_one == "scissors" and self.player_two == "lizard":
            self.player_one.score +=1
        if self.player_two == "scissors" and self.player_one == "paper":
            self.player_two.score +=1
        if self.player_two == "scissors" and self.player_one == "lizard":
            self.player_two.score +=1
        "scissors".__gt__("paper")
        "scissors".__gt__("lizard")