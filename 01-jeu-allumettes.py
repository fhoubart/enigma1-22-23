"""
JEU DES ALLUMETTES
Le jeu consiste à chacun son tour retirer un certain nombres d'allumettes, celui qui prend la dernière à gagné.
- Variante simple : à chaque tour, on ne peut retirer que 1, 2 ou 3 allumettes
"""

import random

print("""
     #######################################
     ###        JEU DES ALLUMETTES       ###
     #######################################
""")

# Variables d'initialisation
nbAllumettesDebut = random.randint(20,30)  # Nombre d'allumettes de la partie
nbAllumettesMaXRetirees = 3  # Nombre maximum d'allumettes que l'on peut retirer dans un tour
nbJoueur = int(input("Combien de joueurs? "))  # Nombres de joueurs

# Etat de la boucle
partieTerminee = False  # Passera à True lorsque quelqu'un a gagné et la partie est terminée
gagnant = 0  # Contiendra le numéro du joueur gagant
joueurEnCours = 0  # Numéro du joueur dont c'est le tour
nbAllumettes = nbAllumettesDebut  # Nombre d'allumettes restantes à chaque tour de jeu

# On joue tant que personne n'a gagné
while not partieTerminee:

    # Un peu d'affichage
    print("Tour du joueur " + str(joueurEnCours+1)) # +1 car les joueurs sont numérotés à partir de 0
    print("Il reste " + str(nbAllumettes) + " allumettes"   )

    # Demander combien d'allumettes retirer, il faut boucler tant que la valeur est invalide
    nbAllumettesRetirees = 0
    while nbAllumettesRetirees <= 0 or nbAllumettesRetirees > nbAllumettesMaXRetirees:
        try:
            nbAllumettesRetirees = int(input("Combien d'allumettes retirer (1 - "+str(nbAllumettesMaXRetirees)+") ? "))
        except ValueError:
            nbAllumettesRetirees = 0

    # On retire les allumettes
    nbAllumettes = nbAllumettes - nbAllumettesRetirees

    # On vérifie si on a gagné
    if nbAllumettes <= 0:
        gagnant = joueurEnCours
        partieTerminee = True

    # C'est le tour du joueur suivant
    joueurEnCours = (joueurEnCours + 1) % nbJoueur

    # Un petit retour à la ligne pour faire joli
    print("")

print("La partie est terminée")
print("Le gagant est le joueur " + str(gagnant+1))  # +1 car les joueurs sont numérotés à partir de 0
