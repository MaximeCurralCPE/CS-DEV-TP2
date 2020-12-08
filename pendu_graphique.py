'''
Sujet : CS-DEV TP 2 : pendu (interface graphique)
Auteur : Maxime Curral
Date de creation : 01/12/2020
'''
from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry
import pendu_graphique_lib


def recuperation_lettre():
    return entree_texte.get()

def affichage_mot(mot):
    mot = Label(frameAffichage, text = mot)
    mot.pack()

def affichage_image(numero):
    image_pendu = PhotoImage(file = 'images/bonhomme' + str(numero) + '.gif')
    canvas = Canvas(mw, width = 100, height = 100)
    item = canvas.create_image(0,0, image = image_pendu)
    canvas.pack(side = 'right', padx = 10, pady = 10)




mw = Tk()
mw.title('Pendu')
mw.geometry('1000x300+100+200')
mw['bg'] = 'mediumaquamarine'



frameAffichage = Frame(mw)
frameAffichage.pack(side = 'top')
frameAffichage['bg'] = 'red'

frameEntree = Frame(mw)
frameEntree.pack(side = 'left')
frameEntree['bg'] = 'red'

entree_texte = Entry(frameEntree)
entree_texte.pack()

bouton = Button(frameEntree, text = "Proposer", bg = 'red', command = recuperation_lettre)
bouton.pack()



affichage('bonjour', [0,4,5])
affichage_image(6)



mw.mainloop()

