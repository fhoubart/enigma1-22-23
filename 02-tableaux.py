"""
Manipulation de listes (tableaux)
Création de fonctions simples
"""

########################
## Listes (tableaux)
########################

# Création d'un tableau en initialisant ses valeurs
variableTableau = ['pomme', 'poire', 'fraise']

# Les tableaux sont indexés à partir de 0
print(variableTableau[0]) # -> pomme
print(variableTableau[1]) # -> poire
print(variableTableau[2]) # -> fraise

# On ne peut pas accéder à un index plus grand que le nombre d'éléments du tableau
#variableTableau[3] = 'banane' # Erreur, tableau à 3 éléments, l'index 4 n'existe pas

# On peut ajouter un nouvel élément à la fin d'une liste avec la méthode 'append'
variableTableau.append('banane')
print(variableTableau)

# Modifier un élément du tableau
variableTableau[1] = "cerise"

# Longueur (taille) d'un tableau -> fonction len
print(len(variableTableau))

# Attention, l'index du dernier élément du tableau est len(tableau)-1


########################
## Boucles for
########################

## Boucles sur les tableaux
# La variable fruit va prendre successivement à chaque itération toutes les valeurs de tous les élements du tableau
for fruit in variableTableau:
    print(fruit)

print("")
## Générer des 'range' d'entiers pour itérer dessus
print("## Ranges ##")

# Range qui contient toutes les valeurs de 0 (inclus) à 5 (non inclus)
print(range(0,5))
for i in range(0,5):
    print(i)

# Range qui contient toutes les valeurs de 2 (inclus) à 8 (non inclus)
print(range(2,8))
for i in range(2,8):
    print(i)

# Range qui contient toutes les valeurs de 2 (inclus) à 8 (non inclus) par pas de 2
print(range(2,8,2))
for i in range(2,8,2):
    print(i)

# Range qui contient toutes les valeurs de 2 (inclus) à 8 (non inclus) par pas de 3
print(range(2,8,3))
for i in range(2,8,3):
    print(i)

# Utilisation d'un range pour boucler sur un index
print("Boucler de 0 à 4")
for index in range(0,5):
    print("L'index est "+str(index))


# Entrer des noms d'utilisateur
#nbJoueurs = int(input("Combien de joueurs ? "))


# Boucler autant de fois que de joueurs

    # Demander le nom du joueur
    # l'enregistrer dans le tableau


#print(joueurs[0]) # nom du 1er joueur
#print(joueurs[1]) # nom du 2ème joueur


############################
## Définition de Fonctions
############################

# Fonction qui calcule la moyenne de trois valeurs passées en paramètres
def moyenneVariables(var1, var2, var3):
    resultat = (var1 + var2 + var3) / 3
    return resultat

variable = moyenneVariables(2,4,6)
print("La moyenne de 2, 4 et 6 est " + str(variable))


def min(tableau):
    """Calcule la valeur minimal contenue dans un tableau
    :param tableau: le tableau dans lequel on cherche le minimum
    :return: la plus petite valeur contenue dans le tableau, ou 0 si le tableau est vide
    """
    if len(tab) == 0:
        return 0
    minValue = tableau[0]
    for index in range(0,len(tableau)):
        if tableau[index] < minValue:
            minValue = tableau[index]
    return minValue

def max(tableau):
    """Calcule la valeur maximale contenue dans un tableau
        :param tableau: le tableau dans lequel on cherche le maximum
        :return: la plus grande valeur contenue dans le tableau
    """
    maxValue = tableau[0]
    for elt in tableau:
        if elt > maxValue:
            maxValue = elt
    return maxValue

def moyenne(tableau):
    """Calcule la moyenne de toutes les valeurs contenues dans un tableau
        :param tableau: le tableau pour lequel on veut calculer la moyenne
        :return: la moyenne de toutes les valeurs du tableau
    """
    resultat = 0
    for elt in tableau:
        resultat = resultat + elt
    return resultat/len(tableau)

tab = [3,5,2,6,7,4]
print(min(tab))
print(max(tab))
print(moyenne(tab))

print("")











print("a", end=" ")
print("b", end=" ")

print()








for i in range(0,10):
    for i in range(0,10):
        print("x", end=" ")
    print()

print()



for i in range(1,9):
    print(str(i),end=" ")
    for j in range(1,9):
        r = i*j
        if(r < 10):
            text = " "+str(r)
        else:
            text = str(r)
        print(text, end=" ")
    print()


