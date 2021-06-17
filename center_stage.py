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
        self.rock = Rock()
        self.scissors = Scissors()
        self.paper = Paper()
        self.lizard = Lizard()
        self.spock = Spock()

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
            if self.rock.get_hierarchy(self.player_one, self.player_two):
                self.showdown()
            elif self.scissors.get_hierarchy(self.player_one, self.player_two):
                self.showdown()
            elif self.paper.get_hierarchy(self.player_one, self.player_two):
                self.showdown()
            elif self.lizard.get_hierarchy(self.player_one, self.player_two):
                self.showdown()
            elif self.spock.get_hierarchy(self.player_one, self.player_two):
                self.showdown()
            elif self.player_one.chosen_gesture == self.player_two.chosen_gesture:
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
