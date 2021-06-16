from human import Human
from artificial_intelligence import Artificial_Intelligence

class Center_Stage:
    def __init__(self):
        self.player_one = Human("name")
        self.player_two = None

    def run_game(self):

        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

        print("Instructions:")
        print("1.Choose how many players.")
        print("2.Enter your name(s).")
        print("3.Select a gesture.")
        print("4.Winner is best of three!")

        self.choose_game_mode()
        self.showdown()
        self.display_winner()

    def choose_game_mode(self):
        number_of_players = int(input("How many players?"))
        if number_of_players > 2 or number_of_players == 0:
            print("There can only be one or two players.")
            self.choose_game_mode()
        self.player_one.name = input("Enter player one's name.")
        if number_of_players == 2:
            self.player_two = Human(input("Enter player two's name."))
        else:
            self.player_two = Artificial_Intelligence("Chappie")

    def showdown(self):
        # choices switched to integers [rock=0, paper=1, scissors=2, lizard=3, spock=4]
        while (0 > 2 and 0 > 3, 2 > 1 and 2 > 3, 1 > 0 and 1 > 4, 3 > 4 and 3 > 1, 4 > 2 and 4 > 0):
            while self.player_one.score < 2 and self.player_two.score < 2:
                self.player_one_choice()
                self.player_two_choice()
                if self.player_one.chosen_gesture > self.player_two.chosen_gesture:
                    self.player_one.score += 1
                    print(f"{self.player_one.name} won with {self.player_one.gesture_name}!")
                    print(f"{self.player_one.name}:{self.player_one.score} {self.player_two.name}:{self.player_two.score}")
                    self.showdown()
                if self.player_one.chosen_gesture < self.player_two.chosen_gesture:
                    self.player_two.score += 1
                    print(f"{self.player_two.name} won with {self.player_two.gesture_name}!")
                    print(f"{self.player_one.name}:{self.player_one.score} {self.player_two.name}:{self.player_two.score}")
                    self.showdown()
                if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                    print("It was a tie!")
                    self.showdown()
            break
    def player_one_choice(self):
        self.player_one.choose_gesture()
        if self.player_one.chosen_gesture > 4:
            print("Sorry, choose zero through four.")
            self.player_one_choice()
        print(f"{self.player_one.name} chooses {self.player_one.gesture_name}.")

    def player_two_choice(self):
        if self.player_two == Human(""):
            self.player_two.choose_gesture()
            print(f"{self.player_two.name} chooses {self.player_two.gesture_name}.")
        else:
            self.player_two.choose_gesture()
            print(f"{self.player_two.name} chooses {self.player_two.gesture_name}.")

    def display_winner(self):
        if self.player_one.score == 2:
            print(f"{self.player_one.name} has won!")
        if self.player_two.score == 2:
            print(f"{self.player_two.name} has won!")
