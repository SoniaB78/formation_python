from random import randint
from time import sleep
import pygame
from pygame.locals import *

class Pendu():

    def __init__(self):

        self.nbDeCoupsRestants = 7
        self.lettreTappees = []
        self.lettreTappeesSTR = ""
        self.motAAfficher = []

    def creationListeDeMots(self,theme):
        "Création de la liste des mots en fonction du theme en attribut"
        self.affichageComplet
        self.listeDeMots = []

        if theme == "chiens":
            fichier = ".\\chiens\\index.csv"
        elif theme == "pays":
            fichier = ".\\pays\\index.csv"
        elif theme == "instruments":
            fichier = ".\\instruments\\index.csv"
        elif theme == "fruits":
            fichier = ".\\fruits\\index.csv"
        with open(fichier, encoding='utf-8') as f :
            for ligne in f:
                ligne_recuperee = f.readline()
                ligne_coupee = ligne_recuperee.split(";")


                mot = ligne_coupee[0]
                #image = ligne_coupee[1]
                #lien  = ligne_coupee[2]
                self.listeDeMots.append(mot)


    def selectionMot(self):
        "Tire un mot au hasard dans la liste listeDeMots"
        self.motATrouver = self.listeDeMots[randint(0,len(self.listeDeMots)-1)]

        return self.motATrouver

    def lettreJoueePresente(self,lettreJouee):
        "Vérifie si la lettre est présente dans le mot"

        if lettreJouee != "" and not lettreJouee in self.lettreTappees:
            self.lettreTappees.append(lettreJouee)
            self.lettreTappeesSTR += lettreJouee


        if lettreJouee in self.motATrouver:
            return True
        else:
            self.nbDeCoupsRestants -= 1
            return False

    def partiePerdue(self):
        "Vérifie si perdu"
        if self.nbDeCoupsRestants <= 0:
            return True
        else:
            return False

    def partieGagnee(self):
        "Vérifie si gagné"
        if "-" in self.motAAfficher:
            return False
        else:
            return True

    def affichageMot(self):
        "Crée le mot a afficher avec des '-' si la lettre n'a pas été tentée"
        self.motAAfficher = []
        for lettreMot in self.motATrouver:
            if lettreMot in self.lettreTappees:
                self.motAAfficher.append(lettreMot)
            elif lettreMot == " " or lettreMot == "-":
                self.motAAfficher.append("  ")
            else:
                self.motAAfficher.append("-")

        motEnStr = ""
        for lettre in self.motAAfficher:
            motEnStr += lettre

        self.motAAfficher = motEnStr

        return self.motAAfficher

    def affichageComplet(self):
        print("Il reste",self.nbDeCoupsRestants,"coups")
        print("Lettre jouées :",self.lettreTappees)
        print(self.affichageMot())







##  Programme Principal

pygame.init()
police = pygame.font.SysFont("impact", 50)
fenetre = pygame.display.set_mode((1080,720))


jeu = Pendu()




continuerChoixTheme = True

while continuerChoixTheme:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        #Gestion des appuis touche (+ conversion QWERTY => AZERTY)
        if event.type == KEYDOWN:
            carac= event.dict['unicode']
            if carac == '1' :
                jeu.creationListeDeMots("chiens")
                continuerChoixTheme = False
            elif carac == '2':
                jeu.creationListeDeMots("fruits")
                continuerChoixTheme = False
            elif carac == '3':
                jeu.creationListeDeMots("instruments")
                continuerChoixTheme = False
            elif carac == '4':
                jeu.creationListeDeMots("pays")
                continuerChoixTheme = False


    texte = police.render("1:Chiens  2:Fruits  3:Instruments  4:Pays", 1, (255,0,0))

    fenetre.blit(texte, (100,300))
    pygame.display.flip()

    sleep(0.2)



jeu.selectionMot()

jeu.affichageComplet()
lettreATester = list()
#BOUCLE DE JEU
continuerJeu = True
while continuerJeu :
    #Gestion des évenement (fermer et appui touche)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        #Gestion des appuis touche (+ conversion QWERTY => AZERTY)
        if event.type == KEYDOWN:
            carac= event.dict['unicode']
            if carac == 'A' or carac == 'a':
                jeu.lettreJoueePresente('A')
            elif carac == 'B' or carac == 'b':
                jeu.lettreJoueePresente('B')
            elif carac == 'C' or carac == 'c':
                jeu.lettreJoueePresente('C')
            elif carac == 'D' or carac == 'd':
                jeu.lettreJoueePresente('D')
            elif carac == 'E' or carac == 'e':
                jeu.lettreJoueePresente('E')
            elif carac == 'F' or carac == 'f':
                jeu.lettreJoueePresente('F')
            elif carac == 'G' or carac == 'g':
                jeu.lettreJoueePresente('G')
            elif carac == 'H' or carac == 'h':
                jeu.lettreJoueePresente('H')
            elif carac == 'I' or carac == 'i':
                jeu.lettreJoueePresente('I')
            elif carac == 'J' or carac == 'j':
                jeu.lettreJoueePresente('J')
            elif carac == 'K' or carac == 'k':
                jeu.lettreJoueePresente('K')
            elif carac == 'L' or carac == 'l':
                jeu.lettreJoueePresente('L')
            elif carac == 'M' or carac == 'm':
                jeu.lettreJoueePresente('M')
            elif carac == 'N' or carac == 'n':
                jeu.lettreJoueePresente('N')
            elif carac == 'O' or carac == 'o':
                jeu.lettreJoueePresente('O')
            elif carac == 'P' or carac == 'p':
                jeu.lettreJoueePresente('P')
            elif carac == 'Q' or carac == 'q':
                jeu.lettreJoueePresente('Q')
            elif carac == 'R' or carac == 'r':
                jeu.lettreJoueePresente('R')
            elif carac == 'S' or carac == 's':
                jeu.lettreJoueePresente('S')
            elif carac == 'T' or carac == 't':
                jeu.lettreJoueePresente('T')
            elif carac == 'U' or carac == 'u':
                jeu.lettreJoueePresente('U')
            elif carac == 'V' or carac == 'v':
                jeu.lettreJoueePresente('V')
            elif carac == 'W' or carac == 'w':
                jeu.lettreJoueePresente('W')
            elif carac == 'X' or carac == 'x':
                jeu.lettreJoueePresente('X')
            elif carac == 'Y' or carac == 'y':
                jeu.lettreJoueePresente('Y')
            elif carac == 'Z' or carac == 'z':
                jeu.lettreJoueePresente('Z')

            #   S'éxécute uniquement quand j'appuie sur une touche

            jeu.affichageComplet()

    fenetre.fill(0x009900)

    lettreTap = police.render(str(jeu.lettreTappeesSTR), 1, (255,255,0))
    mot = police.render(jeu.motAAfficher, 1, (255,0,0))
    nbDeCoupsRestants = police.render(str(jeu.nbDeCoupsRestants), 1, (0,0,255))

    fenetre.blit(lettreTap, (100,150))
    fenetre.blit(mot, (100,300))

    fenetre.blit(nbDeCoupsRestants, (100,500))
    pygame.display.flip()

    sleep(0.5)


    if jeu.partieGagnee() or jeu.partiePerdue() : continuerJeu = False


continuerFin = True
while continuerFin:
    if jeu.partieGagnee():
        couleur = 0x00FF00
        texteDeFin = "GAGNE"

    if jeu.partiePerdue():
        couleur = 0xFF0000
        texteDeFin = "PERDU"

    for event in pygame.event.get():
        if event.type == QUIT:
            continueFin = False
            pygame.quit()



    fenetre.fill(couleur)
    mot = police.render(jeu.motATrouver, 1, (255,0,255))
    texteDeFin = police.render(texteDeFin, 1, (255,255,255))

    fenetre.blit(mot, (200,250))
    fenetre.blit(texteDeFin, (500,500))

    pygame.display.flip()

    sleep(0.5)

pygame.quit()







