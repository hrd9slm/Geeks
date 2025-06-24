import random

class Player:
    def __init__(self, name):
        self.name = name

    def get_move(self):
        raise NotImplementedError("get_move doit être implémentée par une sous-classe.")

class HumanPlayer(Player):
    def get_move(self):
        move = input(f"{self.name}, choisis [rock, paper, scissors] : ").lower()
        while move not in ["rock", "paper", "scissors"]:
            move = input("Choix invalide. Recommence : ").lower()
        return move

class ComputerPlayer(Player):
    def get_move(self):
        return random.choice(["rock", "paper", "scissors"])
