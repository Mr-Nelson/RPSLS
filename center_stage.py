from human import Human
from artificial_intelligence import Artificial_Intelligence

class Center_Stage:
    def __init__(self):
        self.import_player_one: Human("Kirk")
        self.import_player_two: Artificial_Intelligence("Chappie")

    def run_game(self):
        self.player_one_choice()
        self.player_two_choice()
        self.showdown()
        self.display_winner()

    def player_one_choice(self):
        print(f"Press {Human.chose_gesture.gesture_index} for {Human.chose_gesture()}.")
        print("Player one choose your gesture.")
        self.Human.chose_gesture()
        chosen_gesture = int(input())

    def player_two_choice(self):
        if self.import_player_two: Human()
            print(f"Press {Human.chose_gesture.gesture_index} for {Human.chose_gesture()}.")
            print("Player one choose your gesture.")
            self.Human.chose_gesture()
            chosen_gesture = int(input())
        if self.import_player_two: Artificial_Intelligence()
            self.Artificial_Intelligence.chose_gesture()

    def showdown(self):
        pass

    def display_winner(self):
        pass