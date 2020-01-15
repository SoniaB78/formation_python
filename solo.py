#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      python
#
# Created:     15/01/2020
# Copyright:   (c) python 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import Tk
class Pendu:
    def __init__(self,lettre):
        self.lettre = lettre
        self.lettreCliquee = False

    def afficheLettre(self):
        "Affiche la lettre tapée et la retourne"
        print(self.lettre)
        return self.lettre

    def lettreTentee(self):
        "Converti la lettre tentee en True"
        print(self.lettre,self.lettreCliquee)
        self.lettreCliquee = True
        print(self.lettre,self.lettreCliquee)

    def creationAlphabet():
        "Génération 26 objets pour 26 lettres"
        listeLettres = list()
        for i in range(26):
            caractere = chr(65+i)
            lettre = Pendu(caractere)
            listeLettres.append(lettre)
        return listeLettres

class Fenetre:
    def __init__(self):
        "Initialisation des "
        self.largeur = 800
        self.hauteur = 600
        self.title = "Pendu de Florent"

    def creationFenetre(self):
        self.fenetre = Tk()
        self.fenetre.configure(width=self.largeur,height=self.hauteur)
        self.fenetre.mainloop()


#   PROGRAMME PRINCIPAL
listeLettres = Pendu.creationAlphabet()

fenetre = Fenetre()
fenetre.creationFenetre()

for i in listeLettres:
    print("------------------------------")
    i.afficheLettre()
    i.lettreTentee()