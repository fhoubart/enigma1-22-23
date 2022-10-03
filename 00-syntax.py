## Variables
varChaine = "valeur" # varChaine prend le type chaine de caractères
varNumeric = 1
# Opérateurs sur les valeurs numériques
varCalcul = varNumeric + 2  # Addition
varCalcul = varNumeric - 2  # Sousctration
varCalcul = varNumeric * 2  # Multiplication
varCalcul = varNumeric / 2  # Division
varCalcul = varNumeric // 2  # Division entière (quotien de la division)
varCalcul = varNumeric % 2  # Modulo (reste de la division)
varCalcul = varNumeric ** 4 # Puissance 4
# 7 = 3*2 + 1 = 3*(7//2) + (7%2)

# Opérateurs sur les chaines de caractères
varChaine = "bon" + "jour" # Concatention
varChaine = "bon" + str(3) # Concatenation (converti 3 en chaine)
varNumeric = int("2") + 3 # Addition
varChaine = "bon" * 4 # bonbonbonbon => 4 fois la chaine

varNumeric = varNumeric + 1 # Incrementation

entree = 1
utilisateur = 2
entree_utilisateur = 3
entree_joueur_1 = 4
entreeJoueur2 = 4 # CamelCase


## Initialiser un nombre aléatoire

import random

varAleatoire = random.randint(1,5)
print("Le nombre aléatoire est ", varAleatoire)
print("Le nombre aléatoire est " + str(varAleatoire))

## Entrées utilisateur
entreeUtilisateur = input("Dites moi quelque chose: ")
print("Vous avez tapé " + entreeUtilisateur)

entreeNumeric = int(input("Entrez un chiffre: ")) # Attention, on lit un entier avec le int()
print(entreeNumeric*2)


## Conditions
if entree > 10:
    # Ce code est dans le if
    # Celui la aussi
    print("je suis toujous dans le if")
else:
    print("Je suis maintenant dans le else")

## Opérateurs conditionnels :
entree == 10
entree > 10
entree < 10
entree >= 10
entree <= 10
entree != 10

if entree > 10:
    print("entree est supérieur à 10")
else:
    if entree > 5:
        print("entree est compris entre 6 et 10")
    else:
        print("entree est compris entre 0 et 5")

# equivalent à

if entree > 10:
    print("entree est supérieur à 10")
elif entree > 5:
    print("entree est compris entre 6 et 10")
else:
    print("entree est compris entre 0 et 5")


print("je ne suis plus dans le if")



# Boucles
n = 1
while n <= 1000:
    print(n, end=" ")
    n = n + 1
