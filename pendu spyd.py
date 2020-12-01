# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:47:20 2020

@author: hienn
"""

from random import randint

mots = ["bison","alpine","accablant","anticorps","dimension","habitacle","dictionnaire","disproportion","anticonstitutionnellement"]


def choix_mot(liste_mots):
    n=randint(0,len(liste_mots))
    mot =liste_mots[n-1]
    return mot

def pendu(liste_mots,essais):
    choix=choix_mot(liste_mots)
    cache=""
    for i in choix:
        cache=cache + " _ "

    #while essais > 0:


    print(" notre pendu ")

print (choix_mot(mots))