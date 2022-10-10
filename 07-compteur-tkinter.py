import tkinter

## Model
compteur = 0

def incrementer():
    global compteur
    compteur = compteur + 1

def decrementer():
    global compteur
    compteur = compteur - 1
    print(compteur)

def initialiser(valeur):
    global compteur
    compteur = valeur



## Vue
def updateLabel():
    labelCompteur['text'] = str(compteur)

def clickBoutonPlus():
    incrementer()
    updateLabel()

def clickBoutonMoins():
    decrementer()
    updateLabel()

def keyPressed(event):
    if event.char == "p":
        incrementer()
        updateLabel()
    elif event.char == "m":
        decrementer()
        updateLabel()

def clickBoutonInit():
    entree = entry.get()
    entree = int(entree)
    initialiser(entree)
    updateLabel()

fenetre = tkinter.Tk()

label = tkinter.Label(fenetre, text="Compteur")
labelCompteur = tkinter.Label(fenetre, text="0")
entry=tkinter.Entry(fenetre)
entry.pack(side=tkinter.BOTTOM)
boutonInit=tkinter.Button(fenetre, text="init", command=clickBoutonInit) # Commande est une fonction qui est appelée lorsque l'on clique sur le bouton
boutonInit.pack(side=tkinter.BOTTOM)

label.pack(side=tkinter.TOP)
labelCompteur.pack(side=tkinter.TOP)

boutonPlus=tkinter.Button(fenetre, text="+", command=clickBoutonPlus) # Commande est une fonction qui est appelée lorsque l'on clique sur le bouton
boutonMoins=tkinter.Button(fenetre, text="-", command=clickBoutonMoins) # Commande est une fonction qui est appelée lorsque l'on clique sur le bouton
boutonPlus.pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT)
boutonMoins.pack(fill=tkinter.BOTH, expand=True, side=tkinter.RIGHT)



fenetre.bind("<Key>",keyPressed)

fenetre.mainloop()


