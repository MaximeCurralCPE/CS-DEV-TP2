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
    lettres_decouvertes = []
    i = 0
    for i in range(len(mot)):
        if lettre == mot[i]:
            lettres_decouvertes.append(i)
    return lettres_decouvertes

def affichage(mot,lettres_decouvertes):
    mask=""
    for i in range(len(mot)):
        if i in lettres_decouvertes:
            mask += mot[i]
        else:
            mask=mask+' _ '
    return mask
