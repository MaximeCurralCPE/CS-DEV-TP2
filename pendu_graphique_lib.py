'''
Sujet : CS-DEV TP 2 : pendu (console) version 2
Auteur : Maxime Curral
Date de creation : 01/12/2020
'''


from random import randint
from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas, Entry





def recuperation_lettre():
    lettre = str(entree_texte.get())
    entree_texte.delete(0, -1)
    print(lettre)
    test_lettre(lettre, chances, mot_mystere, lettres_connues, lettres_saisies, lettres_decouvertes)

def affichage_mot(mot):
    mot = Label(frameAffichage, text = mot)
    mot.pack()

def affichage_image(numero):
    image_pendu = PhotoImage(file = 'images/bonhomme' + str(numero) + '.gif')
    canvas = Canvas(mw, width = 100, height = 100)
    item = canvas.create_image(0,0, image = image_pendu)
    canvas.pack(side = 'right', padx = 10, pady = 10)



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




def replay():
    # Demande au joueur s'il veut faire une autre partie.
    replay = input('Voulez-vous rejouer ? (o/n)')
    if replay == 'o':                                                                       # S'il veut rejouer, le jeu se relance.
        jeu()
    elif replay == 'n':                                                                     # Sinon, le programme s'arrête.
        exit()
    else:                                                                                   # Si la saisie est invalide, la fonction recommence.
        replay()

def test_lettre(lettre, chances, mot_mystere, lettres_connues, lettres_saisies, lettres_decouvertes):
    if check_input(lettre):
    
            while lettre in lettres_saisies:
                print("vous avez deja saisi la lettre")
                lettre = input('Tapez votre lettre :')
            lettres_saisies.append(lettre)
    
            if check_lettre(str(lettre), str(mot_mystere)) == []:
                chances -= 1
    
            else:
                for val in check_lettre(str(lettre), str(mot_mystere)):
                    lettres_connues.append(val)

            print(affichage(mot_mystere,lettres_connues))
            print('Il vous reste encore ' + str(chances) + ' chances')

    else:
        print('***Saisie non valide***')
        
        if chances > 0 and len(lettres_connues) == len(mot_mystere):
            print('Vous avez gagné, le mot était : ' + mot_mystere)                         
            score = chances
            print('Votre score est : ' + str(score) + '\n' + 'Le meilleur score est : ' + str(check_meilleur_score(score)))            
            #replay()

    if len(lettres_connues) != len(mot_mystere) and chances == 0:
        print('Dommage, le mot était : ' + mot_mystere)
        #replay()

    elif len(lettres_connues) == len(mot_mystere):
        print('Bien joué !')
        #replay()

chances = 8
mot_mystere = choix_mot()
lettres_connues = []
lettres_saisies = []
lettres_decouvertes = []


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



mw.mainloop()
