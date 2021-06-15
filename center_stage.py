from human import Human
from artificial_intelligence import Artificial_Intelligence

class Center_Stage:
    def __init__(self):
        self.player_one = Human("name")
        self.player_two = None
        self.player_one_score = 0
        self.player_two_score = 0

    def run_game(self):
        # Intro
        # Display Welcome
        # Instructions

        self.choose_game_mode()
        self.player_one_choice()
        self.player_two_choice()
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

    def player_one_choice(self):
        self.player_one.choose_gesture()

    def player_two_choice(self):
        if self.player_two == Human(""):
            self.player_two.choose_gesture()
        else:
            self.Artificial_Intelligence.choose_gesture()

    def showdown(self):
        "rock" > "scissors" and "rock" > "lizard"
        "scissors" > "paper" and "scissors" > "lizard"
        "paper" > "rock" and "paper" > "spock"
        "lizard" > "spock" and "lizard" > "paper"
        "spock" > "scissors" and "spock" > "rock"
        while self.player_one_score < 2 and self.player_two_score < 2:
            if self.player_one_choice() > self.player_two_choice():
                self.player_one_score += 1
            if self.player_one_choice() < self.player_two_choice():
                self.player_two_score += 1

    def display_winner(self):
        if self.player_one_score == 2:
            print(f"{self.player_one.name} has won!")
        if self.player_two_score == 2:
            print(f"{self.player_two.name} has won!")
