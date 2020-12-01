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
    for i in range(len(mot)):
        if lettre == mot[i]

check_lettre('a','aukb')

def affichage():
    mot=choix_mot()
    mask=""
    for i in mot:
        mask=mask+'_'