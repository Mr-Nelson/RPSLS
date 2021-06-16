from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        gesture_index = 0
        for gesture in self.gestures:
            print(f"Choose {gesture_index} for {gesture}.")
            gesture_index += 1
        input("Choose your gesture.")
        return self.chosen_gesture