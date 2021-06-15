from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__()

    def chose_gesture(self):
        human_choice = input("Choose your gesture.")