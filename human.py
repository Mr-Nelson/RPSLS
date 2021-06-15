from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        gesture_index = 1
        print("Choose {gesture_index} for {self.gestures}.")
        gesture_index += 1
        human_choice = input("Choose your gesture.")