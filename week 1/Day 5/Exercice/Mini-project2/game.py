from player import HumanPlayer, ComputerPlayer
from logic import determine_winner

def play_game():
    player1 = HumanPlayer("Joueur")
    player2 = ComputerPlayer("Ordinateur")

    while True:
        move1 = player1.get_move()
        move2 = player2.get_move()

        print(f"{player1.name} a choisi : {move1}")
        print(f"{player2.name} a choisi : {move2}")

        result = determine_winner(move2,move1)
        print("Résultat :", result)

        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != "o":
            break

if __name__ == "__main__":
    play_game()
