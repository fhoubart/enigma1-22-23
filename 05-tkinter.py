# On commence par importer les librairies tkinter
from tkinter import *

# https://python.doctor/page-tkinter-interface-graphique-python-tutoriel

# La fenêtre contient tout le reste
fenetre = Tk()

# On crée ensuite les différents composants de la fenêtre
label = Label(fenetre, text="Hello World")
label.pack()

bouton=Button(fenetre, text="Fermer", command=fenetre.quit) # Commande est une fonction qui est appelée lorsque l'on clique sur le bouton
bouton.pack()

monCanvas = Canvas(fenetre, width=500, height=500, bg='ivory', borderwidth=0, highlightthickness=0)
monCanvas.pack()

# Dessin dans le canvas
line = monCanvas.create_line(0, 0, 30, 30, width=2, fill="#ff0000")
rect = monCanvas.create_rectangle(50,300,450,350, fill="red", activefill="yellow", outline="blue", width=5)
text = monCanvas.create_text(180, 310, text="Tkinter",
                fill="black",
                font="Times 10 bold")

oval = monCanvas.create_oval([100,100], (200,200), fill='light blue', outline='red', width=2)

def keyPressed(event):
    offset = 0
    if event.char == "j":
        offset = -10
    elif event.char == "k":
        offset = 10
    monCanvas.move(oval,offset,0)

# Ajout d'évènement sur les touches
fenetre.bind("<Key>",keyPressed)


oval = monCanvas.create_oval([200,200], (300,300), fill='black', outline='black', width=2)

print("avant le mainloop")

# On active la fenêtre pour déclencher la gestion des évènements
fenetre.mainloop()

# Le mainloop équivaut à peut de chose prèt à :
#while True:
#    if le bouton est cliqué :
#        pass
#    if la souris est sur le rectangle:
#        pass
#    if la fenetre est redimensionnée:
#        pass

print("après le mainloop")

