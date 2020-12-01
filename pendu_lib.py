'''
Sujet : CS-DEV TP 2
Auteur : Maxime Curral
Date de creation : 01/12/2020
'''

def choix_mot():
    fichier = open('mots.txt',r)
    nombre_lignes = 0
    for ligne in fichier:
        nombre_lignes += 1
    n = randint(0,)