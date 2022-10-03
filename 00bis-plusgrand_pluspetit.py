## Jeu du plus grand / plus petit

## Initialiser un nombre aléatoire
from random import randint
nombreATrouve = randint(1,10) # Type de la variable -> int

# Demander si le joueur est un garçon ou une fille (pour conjuguer les verbes)
filleGarcon = input("Garçon ou fille ?").lower()
if filleGarcon == "f" or filleGarcon == "fille":
    estUneFille = True
else:
    estUneFille = False

## Initialiser la variable qui stocke le nombre de coups
nombreCoup = 0

## Initialiser une entrée utilisateur "bidon" pour démarrer la boucle
entreeUtilisateur = 0

## Tant que l'entrée utilisateur est différente du nombre aléatoire
while entreeUtilisateur != nombreATrouve:

    ## Entrée utilisateur
    entreeUtilisateur = int(input("Entrez un chiffre: ")) # type de entreeUtilisateur -> int
    nombreCoup = nombreCoup + 1

    # Comparer l'entrée utilisateur avec le nombre aléatoire
    # et afficher le message qui va bien
    if entreeUtilisateur == nombreATrouve:
        # L'utilisateur à trouvé la bonne réponse
        print("Bonne réponse !")
    elif entreeUtilisateur > nombreATrouve:
        # L'entrée est plus grande que le nombre à trouver
        print("Trop grand !")
    elif entreeUtilisateur < nombreATrouve:
        # L'entrée est plus petite que le nombre à trouver
        print("Trop petit !")

coupPluriel = "s"
if nombreCoup == 1: coupPluriel = ""

arriveFeminin = ""
if estUneFille: arriveFeminin = "e"

print("Vous y êtes arrivé" + arriveFeminin + " en " + str(nombreCoup) + " coup"+coupPluriel)



