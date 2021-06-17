class Player:
    def __init__(self, name):
        self.name = name
        self.player_gestures = ["rock", "paper", "scissors", "lizard", "Spock"]
        self.chosen_gesture = ""
        self.score = 0




    def choose_gesture(self):

        gesture_index = 0
        for gesture in self.player_gestures:
            print(f"Press {gesture_index} for {gesture}.")
            gesture_index += 1
        self.chosen_gesture = input("Choose your gesture.")
        if int(self.chosen_gesture) > 4:
            print("Sorry, choose zero through four.")
            self.choose_gesture()
        self.chosen_gesture = self.player_gestures[int(self.chosen_gesture)]
        return self.chosen_gesture

