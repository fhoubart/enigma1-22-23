from tkinter import *

fenetre = Tk()

monCanvas = Canvas(fenetre, width=501, height=501, bg='ivory', borderwidth=0, highlightthickness=0)
monCanvas.pack()

fill = 0

posX = 5
posY = 4

for j in range(0,10):
    # Iteration pour chaque ligne
    compteurCases = j%2
    for i in range(0,10):
        # Iteration pour chaque case d'une ligne
        if compteurCases % 2 == 0:
            fillColor = "white"
        else:
            fillColor = "grey"

        rect = monCanvas.create_rectangle(i*50,50*j,(i+1)*50,(j+1)*50, fill=fillColor, activefill="yellow", outline="black", width=1)
        compteurCases = compteurCases + 1

personnage = monCanvas.create_oval([posX*50,posY*50], ((posX+1)*50,(posY+1)*50), fill='light blue', outline='red', width=1)

def keyPressed(event):
    global posY
    global posX
    # La lettre appuyée est dans event.char
    if event.char == 'z' and posY > 0:
        # monter
        monCanvas.move(personnage,0,-50)
        posY = posY + 1
    elif event.char == 's' and posY < 10:
        # descendre
        monCanvas.move(personnage,0,50)
        posY = posY - 1
    elif event.char == 'q' and posX > 0:
        # gauche
        monCanvas.move(personnage,-50,0)
        posX = posX + 1
    elif event.char == 'd' and posX < 10:
        # droite
        monCanvas.move(personnage,50,0)
        posX = posX - 1


fenetre.bind("<Key>",keyPressed)

fenetre.mainloop()