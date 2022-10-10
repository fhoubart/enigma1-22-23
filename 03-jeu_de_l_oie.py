import random

nbJoueurs = 10
positionsJoueurs = [0]*nbJoueurs


nbCases = 10

partieFini = False

joueurEnCours = 0

def printPlateau():
    for i in range(0, nbCases):
        print("+---", end="")
    print("+")

    for j in range(0, nbJoueurs):
        for i in range(0, nbCases):
            if positionsJoueurs[j] == i:
                print("| " + str(j) + " ", end="")
            else:
                print("|   ", end="")
        print("|")

    for i in range(0, nbCases):
        print("+---", end="")
    print("+")


while not partieFini:

    printPlateau()

    print()
    input("Tour du joueur "+str(joueurEnCours+1)+", appuyer sur Entrée pour lancer le dé")
    de = random.randint(1,3)
    print(" ---> " + str(de)+" !")
    input("Appuyer sur Entrée pour avancer et passer au joueur suivant")
    positionsJoueurs[joueurEnCours] = positionsJoueurs[joueurEnCours] + de
    if positionsJoueurs[joueurEnCours] >= nbCases:
        positionsJoueurs[joueurEnCours] = nbCases-1

    if(positionsJoueurs[joueurEnCours] == nbCases-1):
        partieFini = True

    joueurEnCours = (joueurEnCours + 1)%2

printPlateau()
print("La partie est finie")
