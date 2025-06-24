def determine_winner(move1, move2):
    if move1 == move2:
        return "Égalité"
    elif (move1 == "rock" and move2 == "scissors") or (move1 == "scissors" and move2 == "paper") or (move1 == "paper" and move2 == "rock"):
        return "Joueur 1 gagne"
    else:
        return "Joueur 2 gagne"
