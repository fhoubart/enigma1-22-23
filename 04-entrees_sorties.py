"""
Utilisation des chaines de caractères et gestion des entrée/sorties
(interaction utilisateur et lecture de fichiers)
"""

## Lecture d'une entrée utilisateur: fonction "input(msg)"

nom = input("Quel est ton nom ? ")
print("Je m'appelle "+nom)



# Utilisation des chaines comme des tableaux
chaine = "Quel est ton nom ?"
print(chaine)    # Quel est ton nom ?
print(chaine[0]) # Q
print(chaine[5]) # e
print(chaine[0:4]) # Quel
print(chaine[:8]) # equivalent à chaine[0:8] -> Quel est
print(chaine[10:]) # on nom ?
print(chaine[-3:]) # m ? (3ème en partant de la fin jusqu'à la fin)
print(chaine[-5:-2]) # nom (5ème en partant de la fin jusqu'au 2ème en partant de la fin)
print(chaine[-5:16]) # nom (le même car le 16ème caractère est le même que le 2ème en partant de la fin)


# Codage simple : ASCII
# Le code Ascii correspond à la valeur encodée sur 1 octet d'un caractère
# La fonction ord(char) renvoie le code ascii d'un caractère
print("""
####################
## Encodage ASCII ##
####################
""")

# Encode en code ascii : ord
print(ord("Q")) # affiche 81

# Décodage d'un code ascii : chr
print(chr(81))

## Codage de "Quel est ton nom" en ascii :
## -> 81 117 101 ...

def encodage_ascii(text):
    """ Renvoie une autre chaine qui correspond aux codes ascii de chaque lettre
    séparés par des espaces
    """
    resultat = ""
    for lettre in text:
        code = ord(lettre)
        resultat = resultat + str(code) + " "
    return resultat

def encodage_ascii_compact(text):
    return " ".join([str(ord(x)) for x in text])

def decodage_ascii(textEncode):
    """
    Renvoyer le texte d'origine encodé dans le paramètre en ascii
    :param text: une suite de code ascii séparés par des espaces (par exemple " 66 111 110 106 111 117 114")
    :return: la chaine de caractère décodée
    """
    textDecode = ""
    tableauDeCodes = textEncode.strip().split(" ") # carateres est un tableau de chaines de caractères qui représentent chacun un code ascii
    # tableauDeCodes contient ['66', '111', '110', '106', '111', '117', '114']
    for code in tableauDeCodes:
        # On récupère le caractère encodé
        char = chr(int(code))
        # On concatene le caractère décodé au résultat
        textDecode = textDecode + char

    return textDecode

def decodage_ascii_compact(textEncode):
    return "".join([chr(int(x)) for x in textEncode.strip().split(" ")])

# Test de la fonction d'encodage
print(encodage_ascii("Bonjour"))
print(encodage_ascii("Une petite phrase à encoder"))

# Petit exemple d'utilisation de l'encodage
entree = input("Quel texte encoder ? ")
codage = encodage_ascii(entree)
print("Le texte encodé est :")
print(codage)
decodage = decodage_ascii(codage)
print("Le texte décodé est :")
print(decodage)

###
# Cryptage de Cesar
# On décale chaque caractère de la chaine à encoder avec le même décalage.
# Ex. : si le décalage est 2, A->C, B->D, etc...
#
# On utilise les codes ascii qu'on peut facilement décaler. Attention si on sort de la plage : le Z décalé de 1 donne A.
# Utiliser pour cela les modulo en transposant la plage de code [65,90] (majuscules) et [97,122] (minuscule) dans
# [0,15] pour pouvoir utiliser le modulo.
# On n'encodera pas les caractères autres que a-z et A-Z

print("""
#######################
## Cryptage de César ##
#######################
""")
def decaleLettre(lettre,offset):
    """
    Appliquer le décalage d'offset sur une lettre
    :param lettre: Une lettre (une chaine avec un seul caractère)
    :param offset: le nombre de lettres de déclage
    :return: la nouvelle lettre qui correspond au décalage
    """
    # Récupère le code ascii de la lettre
    codeAscii = ord(lettre)

    # En fonction des cas majuscule/minuscule/autre, on applique la bonne formule de décalage
    if codeAscii >= 65 and codeAscii <= 90:
        # Majuscule
        codeTransforme = (codeAscii-65+offset)%26 + 65
    elif codeAscii >= 97 and codeAscii <= 122:
        # Minuscule
        codeTransforme = (codeAscii - 97 + offset) % 26 + 97
    else:
        # Autre
        codeTransforme = codeAscii

    # On renvoie la lettre associé au code transformé
    return chr(codeTransforme)


def cesar(text,offset):
    """
    Encode avec le cryptage de César la chaine passée en paramètre
    :param text: Le text à encoder
    :param offset: Le décalage en nombre de lettres. Ex. si offset = 1, A devient B. Si offset = 5, A devient F
    :return:
    """
    resultat = ""
    # On applique le décalage sur chacune des lettres du text
    for lettre in text:
        resultat = resultat + decaleLettre(lettre,offset)

    return resultat

entree = input("Quel text chiffrer: ")
offset = int(input("Quel décalage ? "))
print(cesar(entree,offset))
print()

### Manipulation avancée de tableaux
print("""
#############################
## Générateurs de tableaux ##
#############################
""")

# Génération de tableau à la volée
chaine = "abc" # Déclaration d'une chaine de caratères
tab2 = [x for x in chaine] # Création d'un tableau avec tous les caractères de la variable chaine, pris tel quel
tab2 = [ord(x) for x in chaine]  # Tableau avec tous les codes ascii des caractères de la variable chaine (on met ord(x) dans le tableau)
print([ord(x) for x in "Bonjour"])  # Affiche [66, 111, 110, 106, 111, 117, 114]

# Génération d'une chaine à partir d'un tableau
print("-".join(['a','b','c'])) # Affiche a-b-c
# Si on veut juste concaténer les valeurs du tableau, on utilise une chaine vide pour séparateur
print("".join(['a','b','c'])) # Affiche abc

# Génération d'un tableau à partir des éléments d'une chaine de caractères
tab = "85 110 101 32 112 101".split(" ") # Le séparateur est un espace, tab = ['85', '110', '101', '32', '112', '101']
tab = "a-b-c".split("-") # Le séparateur est un tiret, tab = ['a', 'b', 'c']


print()



exit()


## Lecture à partir d'un fichier
file = open("01-entrees_sorties.py","r")
lines = file.readlines()
for line in lines:
    print(line) # attention cela affiche aussi le \n à la fin de la chaine


## Manipulation des chaines de caractères
print(nom.upper())
print(nom.lower())
print(len(nom))



