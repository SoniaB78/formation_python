#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     13/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Pendu:
    def __init__ (self, theme, mot):
        self.theme = theme
        self.mot = mot

    def generationAlphabet(self):
        """Boucle qui génère une liste contenant l'alphabet"""
        alphabet = []
        for i in range(65,65+26):
            alphabet.append(chr(i))
        return alphabet

    def selection_mot(self):
        """Tirage d’un mot aléatoire lu dans un csv
        Retourne le mot et le lien de l’image
        """
        ligne_selectionnee = randint(1,323) #Attention au randint qui correspond au nombre de lignes
        with open("index.csv", encoding='utf-8') as f :
            for ligne in range(ligne_selectionnee):
                ligne_recuperee = f.readline()
        nom, lien = ligne_recuperee.split(";")
        lien = lien.replace("\n","")
        return str(nom), lien

    def creation_fenetre(self):
        """Initialisation d’une fenêtre à taille rentrée en dur et non redimensionnable"""
        fenetre = Tk()
        fenetre.title("PENDU")
        fenetre.geometry("1024x720")
        fenetre.resizable(width=False, height=False)
        return fenetre

    def lettrePresente(self,mot,lettre):
        """Retourne vrai si la lettre est présente
        Entrée : Mot + la lettre rentrée
        Retourne Vrai ou Faux
        """
        if lettre in mot:
            return True
        else:
            return False

    def affichageMot(self,mot,lettre):
        """Affichage du mot
        /!\ : from random import randint
        Entrée : le mot à trouver et les lettres tapées
        Sortie : Une liste avec des “-” ou la lettre présente
        """

        listeMotAAficher = []
        present = False
        for lettreMot in mot:
            for lettreATester in lettreTappees:
                if lettreMot == lettreATester:
                    present = True
                    break
                else:
                    present = False
            if present:
                listeMotAAficher.append(lettreATester)
            else:
                listeMotAAficher.append("-")
        return listeMotAAficher



    # LISTE DES FONCTIONS A APPELES POUR CHAQUE BOUTON(LETTRE)

def lettreTappeeA():
    print('A')
    return 'A'
def lettreTappeeB():
    print('B')
    return 'B'
def lettreTappeeC():
    print('C')
    return 'C'
def lettreTappeeD():
    print('D')
    return 'D'
def lettreTappeeE():
    print('E')
    return 'E'
def lettreTappeeF():
    print('F')
    return 'F'
def lettreTappeeG():
    print('G')
    return 'G'
def lettreTappeeH():
    print('H')
    return 'H'
def lettreTappeeI():
    print('I')
    return 'I'
def lettreTappeeJ():
    print('J')
    return 'J'
def lettreTappeeK():
    print('K')
    return 'K'
def lettreTappeeL():
    print('L')
    return 'L'
def lettreTappeeM():
    print('M')
    return 'M'
def lettreTappeeN():
    print('N')
    return 'N'
def lettreTappeeO():
    print('O')
    return 'O'
def lettreTappeeP():
    print('P')
    return 'P'
def lettreTappeeQ():
    print('Q')
    return 'Q'
def lettreTappeeR():
    print('R')
    return 'R'
def lettreTappeeS():
    print('S')
    return 'S'
def lettreTappeeT():
    print('T')
    return 'T'
def lettreTappeeU():
    print('U')
    return 'U'
def lettreTappeeV():
    print('V')
    return 'V'
def lettreTappeeW():
    print('W')
    return 'W'
def lettreTappeeX():
    print('X')
    return 'X'
def lettreTappeeY():
    print('Y')
    return 'Y'
def lettreTappeeZ():
    print('Z')
    return 'Z'

#DEBUT PROGRAMME PRINCIPAL


from tkinter import *
fenetre = Tk()
Button(fenetre, text="A", borderwidth=1,height=2, width=2,command=lettreTappeeA).grid(row=0, column=0)
Button(fenetre, text="B", borderwidth=1,height=2, width=2,command=lettreTappeeB).grid(row=0, column=1)
Button(fenetre, text="C", borderwidth=1,height=2, width=2,command=lettreTappeeC).grid(row=0, column=2)
Button(fenetre, text="D", borderwidth=1,height=2, width=2,command=lettreTappeeD).grid(row=0, column=3)
Button(fenetre, text="E", borderwidth=1,height=2, width=2,command=lettreTappeeE).grid(row=0, column=4)
Button(fenetre, text="F", borderwidth=1,height=2, width=2,command=lettreTappeeF).grid(row=0, column=5)
Button(fenetre, text="G", borderwidth=1,height=2, width=2,command=lettreTappeeG).grid(row=0, column=6)
Button(fenetre, text="H", borderwidth=1,height=2, width=2,command=lettreTappeeH).grid(row=0, column=7)
Button(fenetre, text="I", borderwidth=1,height=2, width=2,command=lettreTappeeI).grid(row=0, column=8)
Button(fenetre, text="J", borderwidth=1,height=2, width=2,command=lettreTappeeJ).grid(row=0, column=9)
Button(fenetre, text="K", borderwidth=1,height=2, width=2,command=lettreTappeeK).grid(row=0, column=10)
Button(fenetre, text="L", borderwidth=1,height=2, width=2,command=lettreTappeeL).grid(row=0, column=11)
Button(fenetre, text="M", borderwidth=1,height=2, width=2,command=lettreTappeeM).grid(row=0, column=12)
Button(fenetre, text="N", borderwidth=1,height=2, width=2,command=lettreTappeeN).grid(row=1, column=0)
Button(fenetre, text="O", borderwidth=1,height=2, width=2,command=lettreTappeeO).grid(row=1, column=1)
Button(fenetre, text="P", borderwidth=1,height=2, width=2,command=lettreTappeeP).grid(row=1, column=2)
Button(fenetre, text="Q", borderwidth=1,height=2, width=2,command=lettreTappeeQ).grid(row=1, column=3)
Button(fenetre, text="R", borderwidth=1,height=2, width=2,command=lettreTappeeR).grid(row=1, column=4)
Button(fenetre, text="S", borderwidth=1,height=2, width=2,command=lettreTappeeS).grid(row=1, column=5)
Button(fenetre, text="T", borderwidth=1,height=2, width=2,command=lettreTappeeT).grid(row=1, column=6)
Button(fenetre, text="U", borderwidth=1,height=2, width=2,command=lettreTappeeU).grid(row=1, column=7)
Button(fenetre, text="V", borderwidth=1,height=2, width=2,command=lettreTappeeV).grid(row=1, column=8)
Button(fenetre, text="W", borderwidth=1,height=2, width=2,command=lettreTappeeW).grid(row=1, column=9)
Button(fenetre, text="X", borderwidth=1,height=2, width=2,command=lettreTappeeX).grid(row=1, column=10)
Button(fenetre, text="Y", borderwidth=1,height=2, width=2,command=lettreTappeeY).grid(row=1, column=11)
Button(fenetre, text="Z", borderwidth=1,height=2, width=2,command=lettreTappeeZ).grid(row=1, column=12)

fenetre.mainloop()
# INTEGRER :

# Ouverture de la fenêtre TkInter ou pygame ou panda?

# affichage nom du jeu règles bouton

#action bouton jouer => envoie page 2

# conditions en fonction du parcourt utilisateur
# ==> choix theme passage du theme choisi pour la page 3

#déroulement du jeu s'aider du diagramme de Phuong



# Passage du mot aléatoirement choisit et du résultat de la partie (gagnée / perdu) à la page 4




