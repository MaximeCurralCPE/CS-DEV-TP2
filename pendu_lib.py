'''
Sujet : CS-DEV TP 2
Auteur : Maxime Curral et Hien Nguyen
Date de creation : 01/12/2020
'''

from random import randint

def choix_mot():
    #retourne un mot au hasard dans mots.txt
    fichier = open('mots.txt','r')
    contenu = fichier.readline()

    liste_mots = contenu.split(' ')
    n = randint(0,len(liste_mots))
    mot = liste_mots[n-1]
    return mot

def check_lettre(lettre,mot):
    #retourne une liste contenant les indexs pour lesquels la
    # lettre entrée par le joueur est dans le mot mystère.
    lettres_decouvertes = []
    i = 0
    for i in range(len(mot)):
        if lettre == mot[i]:
            lettres_decouvertes.append(i)
    return lettres_decouvertes

def affichage(mot,lettres_decouvertes):
    #affiche le mot mystère avec des '_' à la place 
    # des lettres non découvertes.
    mask=""
    for i in range(len(mot)):
        if int(i) in lettres_decouvertes:
            mask += mot[i]
        else:
            mask += ' _ '
    return mask

def jeu():
    mot_mystere = choix_mot()
    lettres_connues = []
    print(mot_mystere)
    while len(lettres_connues) != len(mot_mystere):
        lettre = input('Tapez votre lettre :')
        for val in check_lettre(str(lettre), str(mot_mystere)):
            lettres_connues.append(val)
    print('Vous avez gagné, le mot était' + mot_mystere)