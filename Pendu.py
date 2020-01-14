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

    def generationAlphabet():
        """Boucle qui génère une liste contenant l'alphabet"""
        alphabet = []
        for i in range(65,65+26):
            alphabet.append(chr(i))
        return alphabet

    def selection_mot():
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

    def creation_fenetre():
        """Initialisation d’une fenêtre à taille rentrée en dur et non redimensionnable"""
        fenetre = Tk()
        fenetre.title("PENDU")
        fenetre.geometry("1024x720")
        fenetre.resizable(width=False, height=False)
        return fenetre

    def lettrePresente(mot,lettre):
        """Retourne vrai si la lettre est présente
        Entrée : Mot + la lettre rentrée
        Retourne Vrai ou Faux
        """
        if lettre in mot:
            return True
        else:
            return False

    def affichageMot(mot,lettre):
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
        return "A"
    def lettreTappeeB():
        return "B"
    def lettreTappeeC():
        return "C"
    def lettreTappeeD():
        return "D"
    def lettreTappeeE():
        return "E"
    def lettreTappeeF():
        return "F"
    def lettreTappeeG():
        return "G"
    def lettreTappeeH():
        return "H"
    def lettreTappeeI():
        return "I"
    def lettreTappeeJ():
        return "J"
    def lettreTappeeK():
        return "K"
    def lettreTappeeL():
        return "L"
    def lettreTappeeM():
        return "M"
    def lettreTappeeN():
        return "N"
    def lettreTappeeO():
        return "O"
    def lettreTappeeP():
        return "P"
    def lettreTappeeQ():
        return "Q"
    def lettreTappeeR():
        return "R"
    def lettreTappeeS():
        return "S"
    def lettreTappeeT():
        return "T"
    def lettreTappeeU():
        return "U"
    def lettreTappeeV():
        return "V"
    def lettreTappeeW():
        return "W"
    def lettreTappeeX():
        return "X"
    def lettreTappeeY():
        return "Y"
    def lettreTappeeZ():
        return "Z"


"""

DEBUT PROGRAMME PRINCIPAL

"""

# INTEGRER :

# Ouverture de la fenêtre TkInter ou pygame ou panda?

# affichage nom du jeu règles bouton

#action bouton jouer => envoie page 2

# conditions en fonction du parcourt utilisateur
# ==> choix theme passage du theme choisi pour la page 3

#déroulement du jeu s'aider du diagramme de Phuong



# Passage de du theme choisit et du résultat de la partie (gagnée / perdu) à la page 4




