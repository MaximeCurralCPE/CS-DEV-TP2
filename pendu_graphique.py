'''
Sujet : CS-DEV TP 2 : pendu (console) version 2
Auteur : Maxime Curral
Date de creation : 01/12/2020
'''


from random import randint
from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry, StringVar


def recuperation_lettre():
    lettre = str(entree_texte.get())
    entree_texte.delete(0, 'end')
    test_lettre(lettre, mot_mystere, lettres_connues, lettres_saisies, lettres_decouvertes)

def affichage_mot(mot):
    texte.set(mot)
    fenetre.pack()

def affichage_coups(coups_restants):
    coups.set('nombre de coups restants : ' + str(coups_restants))
    fenetre_coups.pack()

def affichage_image(numero):
    global canvas
    global images
    canvas.create_image(0,0, image = images[numero], anchor = 'nw')
    
def affichage_lettres_tentees(liste):
    lettres_tentees.set(liste)
    fenetre_lettres.pack()

def choix_mot():
    # Retourne un mot au hasard du fichier mots.txt
    fichier = open('mots.txt','r')
    contenu = fichier.readline()
    liste_mots = contenu.split(' ')
    n = randint(0,len(liste_mots))
    mot = liste_mots[n-1]
    fichier.close
    return mot


def check_lettre(lettre,mot):
    # Retourne une liste contenant les indexs pour lesquels la lettre entrée par le joueur est dans le mot mystère.
    lettres_decouvertes = []
    i = 0
    for i in range(len(mot)):
        if lettre == mot[i]:
            lettres_decouvertes.append(i)
    return lettres_decouvertes


def affichage(mot,lettres_decouvertes):
    # Affiche le mot mystère avec des '_' à la place  des lettres non découvertes.
    affichage_masque = ""
    for i in range(len(mot)):
        if int(i) in lettres_decouvertes:
            affichage_masque += mot[i]
        else:
            affichage_masque += ' _ '
    affichage_mot(affichage_masque)
    return affichage_masque


def check_input(lettre):
    # Vérifie que la saisie est bien une seule lettre.
    if isinstance(lettre,str) and len(lettre) == 1 and lettre.isnumeric() == False:
        return True
    else:
        return False


def check_meilleur_score(score):
    # Interroge le fichier score pour comparer le score de la partie et le meilleur score réalisé, et le met à jour si besoin.
    fichier = open('score.txt','r')
    meilleur_score = fichier.readline()
    fichier.close
    if int(meilleur_score) < score:
        fichier = open('score.txt','w')
        fichier.write(str(score))
        fichier.close
        return score
    else:
        return meilleur_score


def test_lettre(lettre, mot_mystere, lettres_connues, lettres_saisies, lettres_decouvertes):
    # Détermine si la lettre est dans le mot à trouver.
    global chances
    if check_input(lettre):
        if lettre in lettres_saisies:
            print("vous avez deja saisi la lettre")
        lettres_saisies.append(lettre)
        affichage_lettres_tentees(lettres_saisies)

        if check_lettre(str(lettre), str(mot_mystere)) == []:
            chances -= 1
            affichage_coups(chances)
            affichage_image(chances)

        else:
            for val in check_lettre(str(lettre), str(mot_mystere)):
                lettres_connues.append(val)

        print(affichage(mot_mystere,lettres_connues))
        affichage_image(chances)
        print('Il vous reste encore ' + str(chances) + ' chances')

    else:
        print('***Saisie non valide***')
        
    if chances > 0 and len(lettres_connues) == len(mot_mystere):
        print('Vous avez gagné, le mot était : ' + mot_mystere)                         
        score = chances
        print('Votre score est : ' + str(score) + '\n' + 'Le meilleur score est : ' + str(check_meilleur_score(score)))

    if len(lettres_connues) != len(mot_mystere) and chances == 0:
        print('Dommage, le mot était : ' + mot_mystere)


# initialisation des variables de jeu
chances = 7
mot_mystere = choix_mot()
lettres_connues = []
lettres_saisies = []
lettres_decouvertes = []
images = []

# création de la fenêtre
mw = Tk()
mw.title('Pendu')
mw.geometry('800x500+100+200')
mw['bg'] = 'mediumaquamarine'

# on crée une liste avec les images de pendu, on les charge et on affiche la première
for i in range(1,9):
    images.append(PhotoImage(file = 'images/bonhomme' + str(i) + '.gif'))

image_pendu = images[7]
canvas = Canvas(mw, width = 300, height = 300)
canvas.create_image(0,0, image = image_pendu, anchor = 'nw')
canvas.pack(side = 'right', padx = 10, pady = 10)

# frame pour affichage
frameAffichage = Frame(mw)
frameAffichage.pack(side = 'top')
frameAffichage['bg'] = 'red'

# frame pour saisie du texte
frameEntree = Frame(mw)
frameEntree.pack(side = 'left')
frameEntree['bg'] = 'red'

# zone de saisie du texte
entree_texte = Entry(frameEntree)
entree_texte.pack()

# affichage du mot à découvrir
texte = StringVar()
texte.set('Quel est le mot mystère ?')
fenetre = Label(frameAffichage, textvariable = texte)
fenetre.pack()

# affichage du nombre de coups restants
coups = StringVar()
coups.set('nombre de coups restants : 7')
fenetre_coups = Label(frameAffichage, textvariable = coups)
fenetre_coups.pack()

# affichage des lettres déjà essayées
lettres_tentees = StringVar()
lettres_tentees.set('lettres tentées : ')
fenetre_lettres = Label(frameAffichage, textvariable = lettres_tentees)
fenetre_lettres.pack()

# bouton pour tester une lettre
bouton = Button(frameEntree, text = "Proposer", bg = 'red', command = recuperation_lettre)
bouton.pack()

mw.mainloop()
