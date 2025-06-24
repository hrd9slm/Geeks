def afficher_tic_tac_toe(Tab): 
    for i in range(3):  
        for ligne in range(3):  
            for j in range(3):  
                if ligne == 1:
                    contenu = Tab[i][j] if Tab[i][j] not in ["X", "O"] else Tab[i][j]
                    print(f" {contenu} ", end="")  
                else:
                    print("   ", end="") 
                if j < 2:
                    print("|", end="") 
            print()  
        if i < 2:
            for j in range(3):
                print("---", end="")  
                if j < 2:
                    print("|", end="")  
            print()  


def num_vers_position(num):
    if 1 <= num <= 9:
        ligne = (num - 1) // 3
        colonne = (num - 1) % 3
        return (ligne, colonne)
    else:
        raise ValueError("Le nombre doit être entre 1 et 9.")
    
def verifier_victoire(grille):

    for ligne in grille:
        if ligne[0] != "" and ligne[0] == ligne[1] == ligne[2]:
            return True

    for col in range(3):
        if grille[0][col] != "" and grille[0][col] == grille[1][col] == grille[2][col]:
            return True

 
    if grille[0][0] != "" and grille[0][0] == grille[1][1] == grille[2][2]:
        return True

 
    if grille[0][2] != "" and grille[0][2] == grille[1][1] == grille[2][0]:
        return True

    return False

tableau = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

joueur = "O"
tour = 0 
while True:
    afficher_tic_tac_toe(tableau)
    try:
        choix = int(input(f"Joueur {joueur}, entrez un nombre (1-9) : "))
        ligne, colonne = num_vers_position(choix)
        
        if tableau[ligne][colonne] in ["X", "O"]:
            print("Cette case est déjà occupée.")
            continue

        tableau[ligne][colonne] = joueur
        tour += 1

        if verifier_victoire(tableau):
            afficher_tic_tac_toe(tableau)
            print(f"Joueur {joueur} a gagné !")
            break

        if tour == 9:
            afficher_tic_tac_toe(tableau)
            print("🤝 Match nul !")
            break

        joueur = "X" if joueur == "O" else "O"

    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre de 1 à 9.")
