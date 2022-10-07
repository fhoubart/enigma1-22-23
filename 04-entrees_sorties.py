## Lecture d'une entrée utilisateur:

nom = input("Quel est ton nom ? ")
print("Je m'appelle "+nom)

## Lecture à partir d'un fichier
file = open("01-entrees_sorties.py","r")
lines = file.readlines()
for line in lines:
    print(line) # attention cela affiche aussi le \n à la fin de la chaine


## Manipulation des chaines de caractères
print(nom.upper())
print(nom.lower())
print(len(nom))



