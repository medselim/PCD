# -*- coding: utf-8 -*-

#une fonction qui permet de chercher un mot particulier d'une liste loin de moins d'un diametre d'un autre mot
def find_in_diam(liste,adj,cible,diametreav):
    i=liste.index(cible)
    for j in range (diametreav):
        if(liste[i-j].find(adj)!=-1):
            return True
    return False