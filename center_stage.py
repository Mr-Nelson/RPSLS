from human import Human
from artificial_intelligence import ArtificialIntelligence
from rock import Rock
from scissors import Scissors
from paper import Paper
from lizard import Lizard
from spock import Spock

class CenterStage:
    def __init__(self):
        self.player_one = Human("name")
        self.player_two = None
        self.player_one.chosen_gesture = Rock()
        self.player_one.chosen_gesture.get_hierarchy()
        self.player_one.chosen_gesture = Scissors()
        self.player_one.chosen_gesture.get_hierarchy()
        self.player_one.chosen_gesture = Paper()
        self.player_one.chosen_gesture.get_hierarchy()
        self.player_one.chosen_gesture = Lizard()
        self.player_one.chosen_gesture.get_hierarchy()
        self.player_one.chosen_gesture = Spock()
        self.player_one.chosen_gesture.get_hierarchy()

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
            self.player_two = ArtificialIntelligence("Chappie")

    def showdown(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one_choice()
            self.player_two_choice()
            if self.player_one.chosen_gesture.__gt__(self.player_two.chosen_gesture):
                self.player_one.score += 1
                print(f"{self.player_one.name} won with {self.player_one.chosen_gesture}!")
                print(f"{self.player_one.name}:{self.player_one.score} {self.player_two.name}:{self.player_two.score}")
                self.showdown()
            if self.player_one.chosen_gesture.__lt__(self.player_two.chosen_gesture):
                self.player_two.score += 1
                print(f"{self.player_two.name} won with {self.player_two.chosen_gesture}!")
                print(f"{self.player_one.name}:{self.player_one.score} {self.player_two.name}:{self.player_two.score}")
                self.showdown()
            if self.player_one.chosen_gesture.__eq__(self.player_two.chosen_gesture):
                print("It was a tie!")
                self.showdown()

    def player_one_choice(self):
        self.player_one.choose_gesture()
        print(f"{self.player_one.name} chooses {self.player_one.chosen_gesture}.")

    def player_two_choice(self):
        if self.player_two == Human(""):
            self.player_two.choose_gesture()
            print(f"{self.player_two.name} chooses {self.player_two.chosen_gesture}.")
        else:
            self.player_two.choose_gesture()
            print(f"{self.player_two.name} chooses {self.player_two.chosen_gesture}.")

    def display_winner(self):
        if self.player_one.score == 2:
            print(f"{self.player_one.name} has won!")
        if self.player_two.score == 2:
            print(f"{self.player_two.name} has won!")
