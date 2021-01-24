from app.models.player import Player
import random

class Game:

    def play_game(self, player_1, player_2):

        if player_1.choice == "rock" and player_2.choice == "scissors":
            return "You WIN!"
        elif player_1.choice == "rock" and player_2.choice == "rock":
            return "It's a DRAW!"
        elif  player_1.choice == "paper" and player_2.choice == "rock":
            return "You WIN!"
        elif player_1.choice == "paper" and player_2.choice == "paper":
            return "It's a DRAW!"
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return "You WIN!"
        elif player_1.choice == "scissors" and player_2.choice == "scissors":
            return "It's a DRAW!"
        else:
            return "You LOSE!"

    def gen_computer_player(self):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        computer = Player("Computer", computer_choice)

        